trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": ["Chennai", "Vijayawada"],
        "days": {"Monday", "Friday"}
    },
    "12602": {
        "name": "Coimbatore Express",
        "stops": ["Chennai", "Salem"],
        "days": {"Tuesday", "Saturday"}
    }
}

station = input("Enter station: ")
day = input("Enter day: ")

for number, details in trains.items():
    if station in details["stops"] and day in details["days"]:
        print(number, details["name"])
