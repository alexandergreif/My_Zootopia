import json

# Load the JSON file
file_path = "animals_data.json"

with open(file_path, "r", encoding="utf-8") as file:
    animals = json.load(file)

# Iterate through animals and print the required fields
for animal in animals:
    details = []

    if "name" in animal:
        details.append(f"Name: {animal['name']}")

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        details.append(f"Diet: {animal['characteristics']['diet']}")

    if "locations" in animal and len(animal["locations"]) > 0:
        details.append(f"Location: {animal['locations'][0]}")

    if "characteristics" in animal and "type" in animal["characteristics"]:
        details.append(f"Type: {animal['characteristics']['type']}")

    if details:
        print("\n".join(details))
        print()  # Print an empty line for separation

#print(animals_data)

