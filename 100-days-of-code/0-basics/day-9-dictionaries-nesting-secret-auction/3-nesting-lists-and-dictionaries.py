capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "United Kingdom": "London",
}

traval_log = {
    "France": ["Paris", "Louvre", "Eiffel Tower"],
    "Germany": ["Berlin", "Brandenburg Gate", "Berlin Wall"],
    "Italy": ["Rome", "Colosseum", "Vatican City"],
    "Spain": ["Madrid", "Sagrada Familia", "Park Guell"],
    "Portugal": ["Lisbon", "Belem Tower", "Jerónimos Monastery"],
    "Netherlands": ["Amsterdam", "Rijksmuseum", "Van Gogh Museum"],
    "Belgium": ["Brussels", "Atomium", "Manneken Pis"],
    "Sweden": ["Stockholm", "Vasa Museum", "Gamla Stan"],
    "Norway": ["Oslo", "Vigeland Park", "Akershus Fortress"],
    "Finland": ["Helsinki", "Suomenlinna Fortress", "Helsinki Cathedral"],
    "Denmark": ["Copenhagen", "Tivoli Gardens", "Little Mermaid Statue"],
    "Iceland": ["Reykjavik", "Blue Lagoon", "Golden Circle"],
    "Ireland": ["Dublin", "Guinness Storehouse", "Trinity College"],
    "United Kingdom": ["London", "Big Ben", "Tower of London"],
}

print(traval_log["France"][1])


nested_list = ["A", "B", ["C", "D", ["E", "F"]], "G"]
print(nested_list[2][2][0])  # E

nested_dict = {
    "A": {
        "B": {
            "C": {
                "D": {
                    "E": {
                        "F": {
                            "G": "H"
                        }
                    }
                }
            }
        }
    }
}
print(nested_dict["A"]["B"]["C"]["D"]["E"]["F"]["G"])  # H

travel_log_2 = {
    "France": {
        "cities_visited": ["Paris", "Louvre", "Eiffel Tower"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Brandenburg Gate", "Berlin Wall"],
        "total_visits": 5,
    },
    "Italy": {
        "cities_visited": ["Rome", "Colosseum", "Vatican City"],
        "total_visits": 8,
    },
}

print(travel_log_2["Germany"]["cities_visited"][2])
