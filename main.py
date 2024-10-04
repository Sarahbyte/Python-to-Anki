import genanki

# Base class for managing Anki decks
class AnkiDeck:
    def __init__(self, deck_id, deck_name, model_id, model_name, fields, templates):
        # Initialize the deck with a unique ID and name
        self.deck = genanki.Deck(
            deck_id=deck_id,
            name=deck_name
        )
        # Define the model (template) for the notes (cards)
        self.model = genanki.Model(
            model_id,
            model_name,
            fields=fields,
            templates=templates
        )

    # Method to create a note (card) using front and back content
    def create_note(self, front, back):
        return genanki.Note(
            model=self.model,
            fields=[front, back]
        )

    # Method to add a list of cards (notes) to the deck
    def add_cards(self, cards):
        for front, back in cards:
            self.deck.add_note(self.create_note(front, back))

    # Method to save the deck as a .apkg file
    def save_to_file(self, file_name):
        package = genanki.Package(self.deck)
        package.write_to_file(file_name)

# Create anki deck
class deckInstance(AnkiDeck):
    def __init__(self):
        # Predefined values for the Professional Ethics deck
        self.deck_id = 2059400110
        self.deck_name = "Professional Ethics in Computing"
        self.model_id = 1607392319
        self.model_name = "Simple Model"
        self.fields = [
            {"name": "Question"},
            {"name": "Answer"}
        ]
        self.templates = [
            {
                "name": "Card 1",
                "qfmt": "{{Question}}",
                "afmt": "{{FrontSide}}<hr id='answer'>{{Answer}}"
            }
        ]
    
        # Call the parent class constructor with the predefined values
        super().__init__(self.deck_id, self.deck_name, self.model_id, self.model_name, self.fields, self.templates)

# Creating an instance of the Professional Ethics deck
ethics_deck = deckInstance()

# List of cards (front, back) to be added to the deck
cards = [
    ("What is professional ethics in computing?", "Professional ethics is a branch of applied ethics that deals with the moral responsibilities of IT professionals."),
    ("What are the key functions of professional codes of ethics?", "They provide guidance, accountability, and set moral standards for professionals."),
]

# Add the cards to the deck
ethics_deck.add_cards(cards)

# Save the deck to a .apkg file
ethics_deck.save_to_file(f"{ethics_deck.deck_name}.apkg")
