# Python-to-Anki Deck Generator

This project allows you to create and export custom Anki flashcard decks using Python and the `genanki` library. The deck generated in this project focuses on "Professional Ethics in Computing," but it can be customized for any subject or content.

## Features

- Create flashcard decks with custom questions and answers.
- Export decks as `.apkg` files for easy import into the Anki app.
- Object-oriented structure for easy reuse and customization.
- Predefined model and templates for simple front-back flashcards.

## Requirements

- Python 3.x
- `genanki` library (Install via pip)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Python-to-Anki.git
   cd Python-to-Anki
2. Install the required Python package:
  ```bash
    pip install genanki
--
## Installation

To install the required package, run:

```bash
pip install genanki
```

## Usage

To create your Anki deck, follow these steps:

1. Customize the `deckInstance` class with your desired deck name, model, fields, and card content.

2. Add the questions and answers for your flashcards to the `cards` list. For example:

    ```python
    cards = [
        ("What is professional ethics in computing?", "Professional ethics is a branch of applied ethics that deals with the moral responsibilities of IT professionals."),
        ("What are the key functions of professional codes of ethics?", "They provide guidance, accountability, and set moral standards for professionals.")
    ]
    ```

3. Run the `main.py` script to generate the `.apkg` file:

    ```bash
    python main.py
    ```

4. The generated deck file (`professional_ethics_cue_cards.apkg`) will be saved in the same directory. You can then import this file into Anki.

## Customization

### Changing Deck Name

You can modify the deck name by editing the `self.deck_name` variable in the `deckInstance` class.

```python
self.deck_name = "Your Custom Deck Name"
```

### Adding More Cards

You can add more cards by extending the `cards` list in the `main.py` script.

```python
cards = [
    ("Front of card 1", "Back of card 1"),
    ("Front of card 2", "Back of card 2"),
    # Add more cards here
]
```

### License

This project is under the MIT License.
