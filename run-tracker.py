runs = [
    {"day": "Day 1", "distance": 2.0, "time": 25, "notes": "Felt tired, but could run longer"},
    {"day": "Day 2", "distance": 2.2, "time": 26, "notes": "Less tired, sprinted out the last half minute"}
]

print("Run Tracker")
print("-" * 20)

total_miles = 0
total_time = 0

for run in runs:
    print(f"{run['day']}:")
    print(f"  Distance: {run['distance']} miles")
    print(f"  Time: {run['time']} minutes")
    print(f"  Notes: {run['notes']}")
    print()

    total_miles += run["distance"]
    total_time += run["time"]

print(f"Total miles logged: {total_miles}")

average_pace = total_time / total_miles

print(f"Total time logged: {total_time} minutes")
print(f"Average pace: {average_pace:.2f} minutes per mile")