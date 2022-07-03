travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

test_dict = {}


def add_new_country(nameOfCountry, numberOfVistes, nameOFcities):
    test_dict["country"] = nameOfCountry
    test_dict["visits"] = numberOfVistes
    test_dict["cities"] = nameOFcities

    travel_log.append(test_dict)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
