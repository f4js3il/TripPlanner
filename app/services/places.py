PLACES_DATABASE={
    "Eiffel Tower": {
        "name": "Eiffel Tower",
        "description": "An iconic symbol of Paris, offering panoramic views of the city.",
        "category": "Landmark",
        "rating": 4.7,
        "estimated_time_hours": 2,
        "entry_fee": 25.0
    },
    "Louvre Museum": {
        "name": "Louvre Museum",
        "description": "World's largest art museum, home to the Mona Lisa.",
        "category": "Museum",
        "rating": 4.8,
        "estimated_time_hours": 4,
        "entry_fee": 17.0
    },
    "Notre Dame Cathedral": {
        "name": "Notre Dame Cathedral",
        "description": "A historic Catholic cathedral known for its French Gothic architecture.",
        "category": "Landmark",
        "rating": 4.6,
        "estimated_time_hours": 1.5,
        "entry_fee": None
    },
    "Sacré-Cœur Basilica": {
        "name": "Sacré-Cœur Basilica",
        "description": "A famous basilica located at the highest point in Paris, offering stunning views of the city.",
        "category": "Landmark",
        "rating": 4.7,
        "estimated_time_hours": 1.5,
        "entry_fee": None
    },
    "Minnesota State Capitol": {
        "name": "Minnesota State Capitol",
        "description": "The seat of the government of the U.S. state of Minnesota, located in Saint Paul.",
        "category": "Landmark",
        "rating": 4.5,
        "estimated_time_hours": 1,
        "entry_fee": None
    },
    "Mall of America": {
        "name": "Mall of America",
        "description": "One of the largest shopping malls in the United States, located in Bloomington, Minnesota.",
        "category": "Shopping",
        "rating": 4.4,
        "estimated_time_hours": 3,
        "entry_fee": None
    },
    "Minneapolis Institute of Art": {
        "name": "Minneapolis Institute of Art",
        "description": "A major art museum in Minneapolis, Minnesota, featuring a wide range of art collections.",
        "category": "Museum",
        "rating": 4.7,
        "estimated_time_hours": 2,
        "entry_fee": None
    },
    "Walker Art Center": {
        "name": "Walker Art Center",
        "description": "A contemporary art center in Minneapolis, Minnesota, known for its modern art exhibitions and performances.",
        "category": "Museum",
        "rating": 4.6,
        "estimated_time_hours": 2,
        "entry_fee": None
    },
    "Paris": {
        "name": "Paris",
        "description": "The capital city of France, known for its art, fashion, and culture.",
        "category": "City",
        "rating": 4.8,
        "estimated_time_hours": 48,
        "entry_fee": None
    }
}

async def get_place_details(place_name):
    return {k.lower(): v for k, v in PLACES_DATABASE.items()}.get(place_name.lower(), None)