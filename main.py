from prompts import RECIPE_PROMPT_TEMPLATE
from llm import generate_recipe
from utils import clean_text, display_recipe

def main():
    ingredients = input("What ingredients do you have? ")
    cuisine = input("Preferred cuisine? ")

    prompt = RECIPE_PROMPT_TEMPLATE.format(
        inventory=ingredients,
        cuisine=cuisine
    )

    print("\nChef is thinking... 👩‍🍳\n")

    raw_output = generate_recipe(prompt)
    cleaned = clean_text(raw_output)
    display_recipe(cleaned)

if __name__ == "__main__":
    main()
