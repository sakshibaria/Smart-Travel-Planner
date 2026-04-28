<div align="center">

# ✈️ Smart Travel Planner

### *Intelligent Multi-Modal Route Optimization System*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Status](https://img.shields.io/badge/Status-In_Development-orange?style=for-the-badge)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> **Stop overpaying for travel.** Most platforms only show you direct flights from one airport.  
> Smart Travel Planner thinks like a seasoned traveler — combining trains, flights, and nearby airports  
> to find routes you never knew existed.

<br/>

![Travel Planner Banner](https://img.shields.io/badge/🗺️_Multi--Modal-Route_Optimization-blueviolet?style=flat-square&labelColor=1a1a2e)
![Graph Engine](https://img.shields.io/badge/🧠_Graph--Based-Dijkstra's_Algorithm-blue?style=flat-square&labelColor=1a1a2e)
![India Focus](https://img.shields.io/badge/🇮🇳_India-IRCTC_+_Airport_Data-orange?style=flat-square&labelColor=1a1a2e)

</div>

---

## 📌 Table of Contents

- [🧠 What is Smart Travel Planner?](#-what-is-smart-travel-planner)
- [🎯 The Problem We're Solving](#-the-problem-were-solving)
- [💡 Our Solution](#-our-solution)
- [🏗️ System Architecture](#️-system-architecture)
- [🧩 How It Works](#-how-it-works)
- [✅ Current Progress](#-current-progress)
- [⚙️ Getting Started](#️-getting-started)
- [📡 API Reference](#-api-reference)
- [⚠️ Known Limitations](#️-known-limitations)
- [🔧 Roadmap](#-roadmap)
- [🚀 Future Scope](#-future-scope)
- [🤝 Contributing](#-contributing)

---

## 🧠 What is Smart Travel Planner?

**Smart Travel Planner** is an intelligent backend system that computes optimized travel routes across **multiple transportation modes** — flights, trains, buses, and cabs — by building a graph of all possible connections and running shortest-path algorithms over it.

The core insight: **your cheapest route might not be a direct flight from your city.** It could be a short train ride to a nearby city + a budget flight from there. We find that for you — automatically.

```
Example:
  Surat → Mumbai (train, ₹250, 2.5h) → Delhi (flight, ₹2,800, 2h)
  vs.
  Surat → Delhi (flight, ₹5,200, 2h)

  Savings: ₹2,150 🎉
```

---

## 🎯 The Problem We're Solving

Traditional travel platforms have a fundamental blind spot:

| Problem | Impact |
|--------|--------|
| 🔴 Only check departure airport = your city | Miss cheaper flights from nearby airports |
| 🔴 No multi-modal combinations | Train + Flight combos ignored entirely |
| 🔴 No total journey cost view | Hidden costs and layovers not surfaced |
| 🔴 User must compare across 5+ platforms | Wasted time, decision fatigue |

**Result:** Users consistently overpay or overlook better routes that exist right in front of them.

---

## 💡 Our Solution

Smart Travel Planner addresses every one of those gaps:

- 🗺️ **Nearby Airport Discovery** — Finds alternative airports within a configurable radius of your departure city
- 🚆 **Multi-Modal Graph** — Integrates IRCTC train routes + flight connections into a single unified graph
- 🧠 **Dijkstra's Algorithm** — Computes the globally cheapest path across all possible route combinations
- 📦 **Structured API** — Returns clean, ranked route recommendations via a FastAPI backend
- 🔌 **API-Ready Design** — Built to plug in real-time flight APIs (Amadeus, Skyscanner) when ready

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   Smart Travel Planner                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   User Request                                          │
│       │                                                 │
│       ▼                                                 │
│  ┌─────────────┐                                        │
│  │  FastAPI     │  ← REST API Layer                     │
│  │  Backend     │                                       │
│  └──────┬──────┘                                        │
│         │                                               │
│         ▼                                               │
│  ┌─────────────────────────────────────────┐            │
│  │           Route Engine                  │            │
│  │  ┌───────────┐    ┌──────────────────┐  │            │
│  │  │  Airport  │    │  Train Service   │  │            │
│  │  │  Service  │    │  (IRCTC Data)    │  │            │
│  │  └─────┬─────┘    └────────┬─────────┘  │            │
│  │        │                  │             │            │
│  │        └────────┬─────────┘             │            │
│  │                 ▼                       │            │
│  │       ┌──────────────────┐              │            │
│  │       │   Graph Engine   │              │            │
│  │       │  (Nodes + Edges) │              │            │
│  │       └────────┬─────────┘              │            │
│  │                ▼                        │            │
│  │       ┌──────────────────┐              │            │
│  │       │   Dijkstra's     │              │            │
│  │       │   Algorithm      │              │            │
│  │       └────────┬─────────┘              │            │
│  └────────────────┼────────────────────────┘            │
│                   ▼                                     │
│           Optimized Route Response                      │
└─────────────────────────────────────────────────────────┘
```

### 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+, FastAPI |
| **Algorithm** | Dijkstra's (Priority Queue) |
| **Data** | Airport Dataset (India), IRCTC Train Routes |
| **Frontend** | Streamlit / React *(planned)* |
| **Flight API** | Amadeus / Skyscanner *(planned)* |

---

## 🧩 How It Works

### Step 1 — Build the Graph

Every city, station, and airport becomes a **node**. Every transport connection becomes an **edge** with three attributes:

```python
edge = {
    "from": "Surat",
    "to": "Mumbai",
    "cost": 250,       # ₹
    "time": 150,       # minutes
    "mode": "train"    # train | flight | bus | cab
}
```

### Step 2 — Find Nearby Airports

Given a source city, the system scans all Indian airports within a configurable radius using lat/long distance calculation, expanding the graph with reachable departure points.

### Step 3 — Run Dijkstra's Algorithm

The graph is traversed using a **priority queue-based Dijkstra** that finds the minimum-cost path from source to destination, considering all multi-hop combinations.

```
Source City
    ↓ (train/cab/bus)
Nearby Airport
    ↓ (flight)
Destination Airport
    ↓ (cab/bus)
Destination City
```

### Step 4 — Return Structured Results

```json
{
  "source": "Surat",
  "destination": "Delhi",
  "total_cost": 3050,
  "total_time": 310,
  "route": [
    { "from": "Surat", "to": "Mumbai", "mode": "train", "cost": 250 },
    { "from": "Mumbai", "to": "Delhi", "mode": "flight", "cost": 2800 }
  ]
}
```

---

## ✅ Current Progress

| Component | Status | Notes |
|-----------|--------|-------|
| 🗂️ Repository Structure | ✅ Done | FastAPI + modular services |
| ✈️ Airport Dataset Integration | ✅ Done | IATA codes, lat/long, city names |
| 🚆 IRCTC Train Dataset | ✅ Done | Source, destination, distance, cost |
| 🧠 Graph Engine | ✅ Done | Nodes, edges, multi-modal support |
| 🔁 Dijkstra's Algorithm | ✅ Done | Priority queue, returns cost + path |
| 📡 API Endpoints | ✅ Done | `/route` and `/airports` live |
| 🔗 City ↔ Station Mapping | ⚠️ In Progress | Node name mismatch being resolved |
| 💰 Real Flight Cost Data | 🚧 Planned | Currently using dummy values |
| 🖥️ Frontend UI | 🚧 Planned | Streamlit / React |

---

## ⚙️ Getting Started

### Prerequisites

```bash
Python 3.10+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/smart-travel-planner.git
cd smart-travel-planner

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the backend server
uvicorn app.main:app --reload
```

The API will be live at `http://localhost:8000` 🚀

### Project Structure

```
smart-travel-planner/
├── app/
│   ├── main.py               # FastAPI entry point
│   ├── routes/
│   │   └── travel.py         # Route endpoints
│   └── services/
│       ├── airport_service.py   # Airport data + nearby lookup
│       ├── train_service.py     # IRCTC data + train edges
│       └── graph_service.py     # Graph engine + Dijkstra
├── data/
│   ├── airports.csv          # India airport dataset
│   └── irctc_trains.csv      # Train routes dataset
├── requirements.txt
└── README.md
```

---

## 📡 API Reference

### `GET /route`

Find the optimized route between two cities.

**Query Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `source` | `string` | Departure city name |
| `destination` | `string` | Arrival city name |

**Example Request:**
```
GET /route?source=Surat&destination=Delhi
```

**Example Response:**
```json
{
  "source": "Surat",
  "destination": "Delhi",
  "total_cost": 3050,
  "total_time": 310,
  "route": [
    { "from": "Surat", "to": "Mumbai", "mode": "train", "cost": 250, "time": 150 },
    { "from": "Mumbai", "to": "Delhi", "mode": "flight", "cost": 2800, "time": 120 }
  ]
}
```

---

### `GET /airports`

Returns all available airports in the dataset.

**Example Response:**
```json
[
  { "city": "Mumbai", "iata": "BOM", "lat": 19.0896, "lng": 72.8656 },
  { "city": "Delhi", "iata": "DEL", "lat": 28.5562, "lng": 77.1000 }
]
```

---

## ⚠️ Known Limitations

> These are actively being worked on in the next development cycle.

- **Node Name Mismatch** — Train nodes use station names (e.g., `"ST"`) while flight nodes use city names (e.g., `"Surat"`). This breaks graph connectivity and is the top priority fix.
- **Dummy Flight Costs** — Flight edges currently use estimated/placeholder values. Real-time API integration is planned.
- **No Bus/Cab Routes** — Only trains and flights are modeled. Road transport is future scope.
- **No Time Optimization** — Currently optimizes only for cost. A* algorithm for time-based routing is planned.

---

## 🔧 Roadmap

### 🏃 Immediate (Next Sprint)

- [ ] Build a **city ↔ station mapping layer** to resolve node name inconsistency
- [ ] Merge airport and train nodes properly in the graph
- [ ] Improve graph connectivity and add validation tests

### 🔜 Short Term

- [ ] Integrate **Amadeus / Skyscanner API** for real flight prices
- [ ] Add **A\* algorithm** for time-optimized routing
- [ ] Add configurable radius for nearby airport search

### 🔮 Long Term

- [ ] Bus and cab route estimation
- [ ] AI-based price prediction model
- [ ] Full frontend UI (React or Streamlit)
- [ ] Deploy as a hosted web application

---

## 🚀 Future Scope

| Feature | Description |
|---------|-------------|
| 🤖 AI Price Prediction | Predict optimal booking windows using historical data |
| 🗺️ Interactive Map UI | Visualize routes on a map with cost breakdowns |
| 🚌 Bus & Cab Routes | Complete door-to-door multi-modal coverage |
| ⏱️ Time Optimization | A* algorithm for fastest-route queries |
| 🔔 Price Alerts | Notify users when their saved route drops in price |
| 🌍 Beyond India | Expand dataset to international routes |

---

## 🤝 Contributing

Contributions are welcome! Here's how to get involved:

```bash
# Fork the repo, then:
git checkout -b feature/your-feature-name
git commit -m "feat: add your feature"
git push origin feature/your-feature-name
# Open a Pull Request 🙌
```

Please follow standard commit conventions and open an issue before starting large features.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with ❤️ to make smarter travel accessible to everyone**

*If this project helped you, consider giving it a ⭐ on GitHub!*

</div>
