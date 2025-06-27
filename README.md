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

