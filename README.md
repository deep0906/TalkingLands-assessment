 Spatial API Backend

- REST API to:
  - Add spatial points
  - Retrieve all points
  - Update spatial data (extendable)
- Uses `PostGIS` for geospatial support
- Async support with `FastAPI` and `SQLAlchemy`
- Swagger UI for API testing (`/docs`)

Tech Stack

- FastAPI
- PostgreSQL with PostGIS
- SQLAlchemy (async)
- GeoAlchemy2
- Pydantic


spatial_api/
├── main.py          # API routes
├── models.py        # DB models
├── schemas.py       # Pydantic schemas
├── database.py      # DB connection
├── requirements.txt # Python dependencies
└── README.md


- `POST /points` - Create new point
- `GET /points` - Get all points

- example polygon data used

{
  "name": "Montana",
  "density": 6.858,
  "geometry": {
    "type": "Polygon",
    "coordinates": [[[...], [...], ...]]
  }
}

- creating polygon 
json
{
  "name": "Montana",
  "density": 6.858,
  "coordinates": [
    [
      [-104.05, 48.99],
      [-97.22,  48.98],
      [-96.58,  45.94],
      [-104.03, 45.94],
      [-104.05, 48.99]
    ]
  ]
}

