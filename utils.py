import json

def clean_text(text: str) -> str:
    return text.replace("```json", "").replace("```", "").strip()

def display_recipe(json_data: str):
    try:
        recipe = json.loads(json_data)
    except json.JSONDecodeError:
        print("\n❌ Failed to parse recipe. Raw output:")
        print(json_data)
        return

    print(f"\n✨ Recipe: {recipe['recipe_name']} ✨")
    print(f"⏱ Prep Time: {recipe['prep_time']}")
    print(f"🌍 Cuisine: {recipe['cuisine_type']}")

    print("\n🛒 Ingredients:")
    for item in recipe["ingredients"]:
        print(f"- {item}")

    print("\n👨‍🍳 Instructions:")
    for i, step in enumerate(recipe["instructions"], 1):
        print(f"{i}. {step}")
