from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from models.model import TravelRequestModel
from fastapi import HTTPException
import json 
from fastapi.encoders import jsonable_encoder
from services.weather import get_weather
from services.currency import get_currency_rate
from services.places import get_place_details  

router = APIRouter(prefix="/stream", tags=["stream"])

async def stream_travel_plan_generator(travel_request: TravelRequestModel):
    """Simulate streaming of travel plan data"""
    yield format_sse({"travel_plan": "Starting travel plan stream"}, event="start")
    yield format_sse({"weather_data": "Fethcing weather data"}, event="weather")
    weather_data = await get_weather(travel_request.destination, str(travel_request.start_date), str(travel_request.end_date))
    yield format_sse({"weather_data": weather_data}, event="weather_complete")
    yield format_sse({"currency_data": "Fetching currency data"}, event="currency")
    currency_data = await get_currency_rate(travel_request.base_currency, "USD")
    yield format_sse({"currency_data": currency_data}, event="currency_complete")
    yield format_sse({"places_data": "Fetching places data"}, event="places")
    places_data = await get_place_details(travel_request.destination) 
    yield format_sse({"places_data": places_data}, event="places_complete")
    yield format_sse({"travel_plan": "Travel plan stream completed"}, event="end")  


def format_sse(data: dict, event: str| None) -> str:
    json_data = json.dumps(jsonable_encoder(data))
    if event:
        return f"event: {event}\ndata: {json_data}\n\n"
    return f"data: {json_data}\n\n"

@router.post("/")
async def stream_travel_plan(travel_request: TravelRequestModel):
    """Aggregate  Weather, Currency, and places data to create a comprehensive travel plan"""
    if travel_request.start_date > travel_request.end_date:
        raise HTTPException(status_code=400, detail="Start date cannot be after end date")
    
    trip_duration = (travel_request.end_date - travel_request.start_date).days
    if trip_duration <= 0:
        raise HTTPException(status_code=400, detail="Trip duration must be positive")
    if trip_duration > 14:
        raise HTTPException(status_code=400, detail="Trip duration cannot exceed 14 days")

    return StreamingResponse(
        stream_travel_plan_generator(travel_request),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"}
    )