import json

json_file_path = "animals_data.json"

with open(json_file_path, "r", encoding="utf-8") as file:
    animals = json.load(file)

# Build the HTML string, serializing each animal with the final design
animals_output = ""
for animal in animals:
    animal_item = '<li class="cards__item">\n'

    # Add the animal's name inside a div with class "card__title"
    if "name" in animal:
        animal_item += f'  <div class="card__title">{animal["name"]}</div>\n'

    animal_item += '  <p class="card__text">\n'

    # Add Diet if available, with a <strong> tag
    if "characteristics" in animal and "diet" in animal["characteristics"]:
        animal_item += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    # Add the first Location if available
    if "locations" in animal and len(animal["locations"]) > 0:
        animal_item += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    # Add Type if available, with a <strong> tag
    if "characteristics" in animal and "type" in animal["characteristics"]:
        animal_item += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    animal_item += "  </p>\n"
    animal_item += "</li>\n"

    animals_output += animal_item

# Read the HTML template file
template_file_path = "animals_template.html"
with open(template_file_path, "r", encoding="utf-8") as template_file:
    template_content = template_file.read()

# Replace the placeholder with the generated animals HTML
new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

# Write the new HTML content to a file
output_file_path = "animals.html"
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(new_html_content)

print("The animals.html file has been created successfully!")

