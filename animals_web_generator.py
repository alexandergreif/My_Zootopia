import json

json_file_path = "animals_data.json"

with open(json_file_path, "r", encoding="utf-8") as file:
    animals = json.load(file)

animals_output = ""
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
        animals_output += "\n".join(details) + "\n\n"

# Read the HTML template file
template_file_path = "animals_template.html"
with open(template_file_path, "r", encoding="utf-8") as template_file:
    template_content = template_file.read()

# Replace the placeholder with the generated animals information
new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

# Write the new HTML content to a file
output_file_path = "animals.html"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(new_html_content)

print("The animals.html file has been created successfully!")