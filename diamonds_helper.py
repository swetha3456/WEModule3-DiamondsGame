import pygame, random

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

IMAGE_FOLDER = "images"

# Set the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set card dimensions
CARD_WIDTH = 60
CARD_HEIGHT = 90

# Set font
FONT = pygame.font.Font(None, 36)

# Dictionary mapping cards to their values
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

card_names = {
    '2': "2",
    '3': "3",
    '4': "4",
    '5': "5",
    '6': "6",
    '7': "7",
    '8': "8",
    '9': "9",
    'T': "10",
    'J': "jack",
    'Q': "queen",
    'K': "king",
    'A': "ace"
}

suits = {
    "diamonds" : dict(zip(card_names.keys(), [c + "_of_diamonds.png" for c in list(card_names.values())])),
    "clubs" : dict(zip(card_names.keys(), [c + "_of_clubs.png" for c in list(card_names.values())])),
    "hearts" : dict(zip(card_names.keys(), [c + "_of_hearts.png" for c in list(card_names.values())])),
    "spades" : dict(zip(card_names.keys(), [c + "_of_spades.png" for c in list(card_names.values())]))
}

class Card:
    def __init__(self, suit, value, image_path):
        self.suit = suit
        self.value = CARD_VALUES[value]  # Use defined dictionary for value
        self.image = pygame.image.load("images/" + suits[suit][value])

    def draw(self, screen, position):
        card_text = FONT.render(str(self.value), True, WHITE)
        screen.blit(card_text, (position[0] + 10, position[1] + 10))
        image = pygame.transform.scale(self.image, (50, 80))
        screen.blit(image, position)

class Deck:
    def __init__(self, cards):
        self.cards = cards.copy()  # Create a copy to avoid modifying original list

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, number):
        if number > len(self.cards):
            raise ValueError("Cannot deal more cards than remaining in deck")
        dealt_cards = self.cards[:number]
        del self.cards[:number]  # Remove dealt cards from the deck
        return dealt_cards

    def is_empty(self):
        return len(self.cards) == 0

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.score = 0

    def bid(self):
        # Implement bidding logic here (could be random or user input)
        # For now, return a random card from the deck
        return random.choice(self.deck)