import pygame, random, os
from diamonds_helper import Card, Deck, Player

# Initialize Pygame
pygame.init()

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

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Diamonds Game")

        self.diamond_cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.player_deck = self.diamond_cards.copy()
        self.computer_deck = self.diamond_cards.copy()
        self.player_score = 0
        self.computer_score = 0
        self.round_number = 1

        self.background_image = pygame.image.load(os.path.join(IMAGE_FOLDER, "background.jpg"))
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def display_text(self, text, position, color):
        text_surface = FONT.render(text, True, color)
        self.screen.blit(text_surface, position)

    def run(self):
        running = True

        while self.diamond_cards and running:
            if not self.diamond_cards:
                break
            current_diamond = random.choice(self.diamond_cards)
            self.diamond_cards.remove(current_diamond)

            self.screen.blit(self.background_image, (0, 0))

            # Display the diamond card in the center of the screen
            card = Card("diamonds", current_diamond)
            card.draw(self.screen, (SCREEN_WIDTH // 2 - CARD_WIDTH // 2, SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2))

            # Display text asking for player's bid
            self.display_text("Choose a card to bid:", (10, SCREEN_HEIGHT - 120), WHITE)

            # Draw the player's deck
            for i, card in enumerate(self.player_deck):
                card_image = Card("diamonds", card)
                card_image.draw(self.screen, (i * CARD_WIDTH, SCREEN_HEIGHT - CARD_HEIGHT))

            # # Handle events
            # for event in pygame.event.get():
            # Display player and computer scores
            self.display_text(f"Player Score: {player_score}", (10, 10), WHITE)
            self.display_text(f"Computer Score: {computer_score}", (10, 50), WHITE)
            pygame.display.flip()

            while True:
                event = pygame.event.wait()

                if event.type == pygame.QUIT:
                    running = False
                    break

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_x, mouse_y = pygame.mouse.get_pos()

                        if SCREEN_HEIGHT - CARD_HEIGHT <= mouse_y <= SCREEN_HEIGHT:
                            selected_card_index = (mouse_x // CARD_WIDTH) % len(self.player_deck)
                            selected_card = self.player_deck.pop(selected_card_index)

                            # Computer's bid
                            computer_card = random.choice(self.computer_deck)
                            self.computer_deck.remove(computer_card)

                            # Determine winner of the round and update scores
                            if CARD_VALUES[computer_card[0]] > CARD_VALUES[selected_card[0]]:
                                computer_score += CARD_VALUES[current_diamond]
                                text = "Computer Won this round"
                            elif CARD_VALUES[computer_card[0]] == CARD_VALUES[selected_card[0]]:
                                computer_score += CARD_VALUES[current_diamond]//2
                                player_score += CARD_VALUES[current_diamond]//2
                                text = "This round is a tie"
                            else:
                                player_score += CARD_VALUES[current_diamond]
                                text = "You won this round"

                            # Display computer's bid and round result
                            self.display_text(f"Computer's bid: {card_names[computer_card]}   You bid: {card_names[selected_card]}", (10, SCREEN_HEIGHT - 200), WHITE)
                            self.display_text(text, (10, SCREEN_HEIGHT - 250), WHITE)
                            pygame.display.flip()
                            pygame.time.delay(3000)
                            break

            # Update round number
            round_number += 1

        # Display final scores and winner
        self.screen.fill(WHITE)
        self.screen.blit(self.background_image, (0, 0))

        self.display_text(f"Player Score: {player_score}", (10, 10), WHITE)
        self.display_text(f"Computer Score: {computer_score}", (10, 50), WHITE)

        if player_score > computer_score:
            text = "You won!"
        elif player_score == computer_score:
            text = "It's a tie!"
        else:
            text = "Computer won!"
    
        self.display_text(text, (SCREEN_WIDTH//2 - 50, SCREEN_HEIGHT//2), WHITE)

    pygame.display.flip()
    # Quit Pygame

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:    
            pygame.quit()
            break

if __name__ == "__main__":
    game = Game()
    game.run()


    
