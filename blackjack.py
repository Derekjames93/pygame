import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
    
    def blitme(self):
        self.screen.blit(self.image, self.rect.center)

class Show_Cards(Block):
    pass


def main():
    width = 400
    height = 400
    green_color = (0, 180, 0 )

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pete\'s Poker Place')
    clock = pygame.time.Clock()

    # create the rectangle for the bar down on the bottom
    ribbon = pygame.Rect(0, 340, 400, 80)
    ribbon_color = (100, 100, 100)

    # houses the pictures for the two decks
    deck = pygame.image.load('images/face_down.png').convert_alpha()

    
    # if dealer face up card == something then, we load the right card
    dealer_card_1 = pygame.image.load('images/heart_A.svg.png').convert_alpha()
    dealer_card_2 = pygame.image.load('images/face_down.png').convert_alpha()

    # show the players cards
    player_card_1 = pygame.image.load('images/spade_A.svg.png').convert_alpha()
    player_card_2 = pygame.image.load('images/heart_J.svg.png').convert_alpha()


    # the two decks for shuffling
    deck_1 = Show_Cards(deck, [180, 200])
    deck_2 = Show_Cards(deck, [220, 200])
    deck_group = pygame.sprite.Group()
    deck_group.add(deck_1, deck_2)

    # The showing the dealers top card and hiding his second card after
    # the he has finishing shuffling all the decks
    dealer_1 = Show_Cards(dealer_card_1, [180, 100])
    dealer_2 = Show_Cards(dealer_card_2, [220, 100])
    dealer_card_group = pygame.sprite.Group()
    dealer_card_group.add(dealer_1, dealer_2)

    # Showing both of the players cards face up
    player_1 = Show_Cards(player_card_1, [180, 300])
    player_2 = Show_Cards(player_card_2, [220, 300])
    player_card_group = pygame.sprite.Group()
    player_card_group.add(player_1, player_2)

    
    # Game initialization

    stop_game = False
    while not stop_game:
        # looks at every event in the queue
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True

            # checks if a key was entered
            if event.type == pygame.KEYDOWN:
                # if the Esc key is pressed, then exit the main loop
                if event.key == pygame.K_ESCAPE:
                    stop_game = True

                # if the y key is pressed, then we add a card to our user hand
                if event.key == pygame.K_LEFT:
                    # print these only after we have shuffled
                    dealer_card_group.draw(screen)
                    player_card_group.draw(screen)
                    pygame.display.update()

                # if the n key is pressed, then the we go into the dealers actions
                if event.key == pygame.K_n:
                    pass
       
        # gets all the keys currently pressed
        keys = pygame.key.get_pressed()
        # Game logic
        
        # Draw background
        screen.fill(green_color)

        # Game display
        # pre-shuffled deck
        deck_group.draw(screen) ## want to add in some sort of shuffle animation that goes before the player and dealer cards are dealt
        pygame.draw.rect(screen, ribbon_color, ribbon)


        pygame.display.update()
        clock.tick(60)

        # Game display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
