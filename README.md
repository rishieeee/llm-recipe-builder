# LLM Recipe Builder (CLI)

A command-line tool that generates cuisine-specific recipes using available
ingredients, powered by Google's Gemini LLM.

## Why I Made This Project?

I built this project to move beyond tutorials and learn how to vibe code, design and ship a complete Python application that integrates an LLM API.

The focus was on:
- Clean CLI design
- Clear separation of concerns
- Prompt engineering as a first-class component
- Safe and configurable API usage via environment variables

This repository represents a foundational pattern for future Python + LLM projects.

## Why This Exists

Most recipe apps assume you’ll buy missing ingredients.
This tool does the opposite: it generates recipes strictly from what you already have, helping reduce food waste and decision fatigue.

## Tech Stack

- Python
- Google Gemini API
- Prompt Engineering
  
## Features

- CLI-based interface (no UI overhead)
- Cuisine-specific recipe generation
- Ingredient-constrained outputs
- Powered by Google Gemini LLM
- Extensible prompt templates

## Example

python main.py --ingredients "rice, eggs, onion" --cuisine "Indian"

Dish: Egg Fried Rice (Indian Style)
Ingredients:
- Rice
- Eggs
- Onion
- Spices

Steps:
1. Heat oil...

## Installation

git clone https://github.com/rishieeee/llm-recipe-builder

cd llm-recipe-builder

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

## Configuration

Create a `.env` file with: ```env

GEMINI_API_KEY=your_api_key_here

## Project Structure

- `main.py` – CLI entry point
- `llm.py` – Gemini API wrapper
- `prompts.py` – Prompt templates
- `utils.py` – Shared helpers

## Limitations

- Output quality depends on LLM responses
- No persistent storage of recipes
- Requires internet access

## Future Improvements

- Save generated recipes locally
- Add dietary constraints (vegan, keto)
- Support multiple LLM providers

## License

MIT
