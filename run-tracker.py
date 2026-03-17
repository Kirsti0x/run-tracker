runs = [
    {"day": "Day 1", "distance": 2.0, "time": 25, "notes": "Felt tired, but could run longer"},
    {"day": "Day 2", "distance": 2.2, "time": 26, "notes": "Less tired, sprinted out the last half minute"}
]

print("Run Tracker")
print("-" * 20)

total_miles = 0

for run in runs:
    print(f"{run['day']}:")
    print(f"  Distance: {run['distance']} miles")
    print(f"  Time: {run['time']} minutes")
    print(f"  Notes: {run['notes']}")
    print()
    total_miles += run["distance"]

print(f"Total miles logged: {total_miles}")

print("Feature branch update")

print("Pull request change")