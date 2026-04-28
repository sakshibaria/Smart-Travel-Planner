"""
Route Routes
API endpoints for route optimization and travel planning.
"""

from fastapi import APIRouter, Query

router = APIRouter(prefix="/route", tags=["Routes"])

# Graph engine reference - set by main.py on startup
graph_engine = None


@router.get("/")
def find_route(
    source: str = Query(..., description="Source city name"),
    destination: str = Query(..., description="Destination city name")
):
    """
    Find the cheapest route between source and destination
    using multi-modal transportation (trains + flights).
    """
    if graph_engine is None:
        return {"error": "Graph engine not initialized. Server is still starting up."}

    # Normalize input to title case for matching
    source = source.strip().title()
    destination = destination.strip().title()

    # Check if cities exist in graph
    all_cities = graph_engine.get_all_cities()
    all_cities_lower = {c.lower(): c for c in all_cities}

    # Try to find matching city names (case-insensitive)
    matched_source = all_cities_lower.get(source.lower())
    matched_dest = all_cities_lower.get(destination.lower())

    if not matched_source:
        return {
            "error": f"Source city '{source}' not found in network",
            "suggestion": "Use /route/cities to see available cities"
        }

    if not matched_dest:
        return {
            "error": f"Destination city '{destination}' not found in network",
            "suggestion": "Use /route/cities to see available cities"
        }

    result = graph_engine.dijkstra(matched_source, matched_dest)
    return result


@router.get("/cities")
def list_cities():
    """List all cities/stations available in the travel network."""
    if graph_engine is None:
        return {"error": "Graph engine not initialized."}

    cities = graph_engine.get_all_cities()
    return {
        "count": len(cities),
        "cities": cities
    }


@router.get("/stats")
def graph_stats():
    """Return statistics about the travel graph."""
    if graph_engine is None:
        return {"error": "Graph engine not initialized."}

    return graph_engine.get_stats()
