import json

# Constant variables to avoid magic values
ANIMALS_JSON_PATH = "animals_data.json"
TEMPLATE_FILE_PATH = "animals_template.html"
OUTPUT_FILE_PATH = "animals.html"
TEMPLATE_PLACEHOLDER = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Load a JSON file and return its content."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def serialize_title(animal_obj):
    """
    Serialize the animal's title.

    Returns a div element with the animal's name if available.
    """
    name = animal_obj.get("name")
    if name:
        return f'  <div class="card__title">{name}</div>\n'
    return ""


def serialize_characteristics(animal_obj):
    """
    Serialize the animal's characteristics: Diet, Location, and Type.

    Returns a string with the formatted characteristics.
    """
    output = ""
    characteristics = animal_obj.get("characteristics", {})

    # Serialize Diet if available
    diet = characteristics.get("diet")
    if diet:
        output += f'      <strong>Diet:</strong> {diet}<br/>\n'

    # Serialize the first Location if available
    locations = animal_obj.get("locations")
    if locations:
        output += f'      <strong>Location:</strong> {locations[0]}<br/>\n'

    # Serialize Type if available
    type_value = characteristics.get("type")
    if type_value:
        output += f'      <strong>Type:</strong> {type_value}<br/>\n'

    return output


def serialize_animal(animal_obj):
    """
    Serialize a single animal's data into an HTML list item.

    Combines the title and characteristics serialization.
    """
    output = '<li class="cards__item">\n'
    output += serialize_title(animal_obj)
    output += '  <p class="card__text">\n'
    output += serialize_characteristics(animal_obj)
    output += "  </p>\n"
    output += "</li>\n"
    return output


def generate_html(animals, template_file_path, output_file_path):
    """
    Generate an HTML file with animal information from a template.

    Serializes each animal's data and replaces the template placeholder.
    """
    # Build the HTML string using the serialize_animal function
    animals_output = "".join(serialize_animal(animal) for animal in animals)

    # Read the HTML template
    with open(template_file_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Replace the placeholder with the generated animal HTML
    new_html_content = template_content.replace(TEMPLATE_PLACEHOLDER, animals_output)

    # Write the new HTML content to the output file
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(new_html_content)

    print("The animals.html file has been created successfully!")


def main():
    """Load animal data and generate the HTML output."""
    animals = load_data(ANIMALS_JSON_PATH)
    generate_html(animals, TEMPLATE_FILE_PATH, OUTPUT_FILE_PATH)


if __name__ == "__main__":
    main()
