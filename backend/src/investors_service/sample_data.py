# Sample Data
from datetime import date

countries = [
    {"id": 1, "name": "Singapore"},
    {"id": 2, "name": "United States"},
    {"id": 3, "name": "United Kingdom"},
    {"id": 4, "name": "China"},
]

investor_types = [
    {"id": 1, "name": "fund manager"},
    {"id": 2, "name": "asset manager"},
    {"id": 3, "name": "wealth manager"},
    {"id": 4, "name": "bank"},
]

investors = [
    {
        "id": 1,
        "name": "Ioo Gryffindor fund",
        "investor_type_id": 1,
        "address": "",
        "country_id": 1,
        "date_added": date(2000, 8, 6),
        "last_updated": date(2024, 2, 21),
    },
    {
        "id": 2,
        "name": "Ibx Skywalker ltd",
        "investor_type_id": 2,
        "address": "",
        "country_id": 2,
        "date_added": date(1997, 7, 21),
        "last_updated": date(2024, 2, 21),
    },
    {
        "id": 3,
        "name": "Cza Weasley fund",
        "investor_type_id": 3,
        "address": "",
        "country_id": 3,
        "date_added": date(2002, 5, 29),
        "last_updated": date(2024, 2, 21),
    },
    {
        "id": 4,
        "name": "Mjd Jedi fund",
        "investor_type_id": 4,
        "address": "",
        "country_id": 4,
        "date_added": date(2010, 6, 8),
        "last_updated": date(2024, 2, 21),
    },
]
