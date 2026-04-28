"""
Airport Routes
API endpoints for airport data and nearby airport lookups.
"""

from fastapi import APIRouter, Query
from services.airport_service import get_airports, find_nearby_airports

router = APIRouter(prefix="/airports", tags=["Airports"])


@router.get("/")
def list_airports():
    """Return all loaded airports."""
    airports = get_airports()
    return {
        "count": len(airports),
        "airports": airports
    }


@router.get("/nearby")
def nearby_airports(
    city: str = Query(..., description="City name to search nearby airports for"),
    radius: float = Query(200, description="Search radius in km")
):
    """Find airports near a given city within a specified radius."""
    results = find_nearby_airports(city, radius_km=radius)
    if not results:
        return {
            "message": f"No airports found near '{city}' within {radius} km",
            "results": []
        }
    return {
        "city": city,
        "radius_km": radius,
        "count": len(results),
        "results": results
    }
