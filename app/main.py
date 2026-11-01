from fastapi import FastAPI
from routes import planner, stream



app = FastAPI(
    title="Trip Planner API", 
    description="Aggregate travel data from multiple sources to provide single plan with SSE support", 
    version="1.0.0"
    )


app.include_router(planner.router)
app.include_router(stream.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Trip Planner API",
        "version": "1.0.0",
        "endpoints": {
            "POST /plan": "Create a travel plan (Aggregated)",
            "GET /plan/stream": "Stream a travel plan (SSE)",
            "GET /plan/cache-stats": "View Cache statistics for travel plans",
            "DELETE /plan/cache": "Clear Cache for travel plans",
            "GET /stream": "Stream data endpoint"
        },
    }