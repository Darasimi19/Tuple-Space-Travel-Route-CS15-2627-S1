mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)


print("Total Destinations:")

print(len(mission_route))

print("Missions route:")


for Destination in mission_route:

    print(Destination)


print("First Destination:")

print(mission_route[0])

print("Last Destination:")

print(mission_route[5])

if "Europa" in mission_route:

    print("Europa has now become apart of this amazing mission route.")


