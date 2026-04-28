"""
Smart Travel Planner - Main Application
Multi-Modal Route Optimization System
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.airport_service import load_airports
from services.train_service import load_trains
from services.graph_service import Graph

from app.routes import airport_routes, route_routes

app = FastAPI(
    title="Smart Travel Planner API",
    description="Multi-Modal Route Optimization System - Find the cheapest travel routes combining flights, trains, and more.",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup():
    """Initialize data and build the travel graph on server startup."""
    print("[STARTUP] Starting Smart Travel Planner...")

    # Load datasets
    load_airports()
    load_trains()

    # Build the multi-modal graph
    graph_engine = Graph()
    graph_engine.build_graph()

    # Share graph engine with route handlers
    route_routes.graph_engine = graph_engine

    print("[STARTUP] Smart Travel Planner ready!")


app.include_router(airport_routes.router)
app.include_router(route_routes.router)


@app.get("/", tags=["Health"])
def home():
    """Health check endpoint."""
    return {
        "message": "Smart Travel Planner API running",
        "docs": "/docs",
        "endpoints": {
            "airports": "/airports",
            "nearby_airports": "/airports/nearby?city=Mumbai",
            "find_route": "/route?source=Mumbai&destination=Delhi",
            "all_cities": "/route/cities",
            "graph_stats": "/route/stats"
        }
    }