from fastapi import APIRouter, HTTPException
from models.model import TravelRequestModel
from services.weather import get_weather
from services.places import get_place_details
from services.currency import get_currency_rate
import asyncio

router = APIRouter(prefix="/plan", tags=["planner"])

@router.post("/")
async def create_travel_plan(travel_request: TravelRequestModel):
    """Aggregate  Weather, Currency, and places data to create a comprehensive travel plan"""
    if travel_request.start_date > travel_request.end_date:
        raise HTTPException(status_code=400, detail="Start date cannot be after end date")
    
    trip_duration = (travel_request.end_date - travel_request.start_date).days
    if trip_duration <= 0:
        raise HTTPException(status_code=400, detail="Trip duration must be positive")
    if trip_duration > 14:
        raise HTTPException(status_code=400, detail="Trip duration cannot exceed 14 days")

    # Here, you would typically call the services to aggregate the travel data (Weather, Currency, Places)
    # Weather Data, Currency Rates, and Places data would be fetched and aggregated into a single travel plan

    weather_data ,places_data, currency_data = await asyncio.gather(
        get_weather(
            destination=travel_request.destination,
            start_date=str(travel_request.start_date),
            end_date=str(travel_request.end_date)
        ),
        get_place_details(travel_request.destination),
        get_currency_rate(
            base_currency=travel_request.base_currency,
            target_currency="USD"
        )
    )

    return {
        "message": "Travel plan created successfully",
        "weather_data": weather_data,
        "places_data": places_data,
        "currency_data": currency_data
    }