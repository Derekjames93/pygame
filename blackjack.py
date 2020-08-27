import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Dealer(Block):
    pass

class Player(Block):
    pass

def main():
    width = 400
    height = 400
    green_color = (0, 180, 0 )

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pete\'s Poker Place')
    clock = pygame.time.Clock()

    # Load dealer image
    # if dealer face up card == something then, we load the right card
    dealer_card_1 = pygame.image.load('images/heart_A.svg.png').convert_alpha()
    dealer_card_2 = pygame.image.load('images/face_down.png').convert_alpha()


    # Our dealer
    dealer_1 = Dealer(dealer_card_1, [200, 100])
    dealer_group_1 = pygame.sprite.Group()
    dealer_group_1.add(dealer_1)

    # Our dealer2
    dealer_2 = Dealer(dealer_card_2, [250, 100])
    dealer_group_2 = pygame.sprite.Group()
    dealer_group_2.add(dealer_2)
    
    # Game initialization

    stop_game = False
    while not stop_game:
        # looks at every event in the queue
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        
        # Draw background
        screen.fill(green_color)

        # Game display
        dealer_group_1.draw(screen)
        dealer_group_2.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

        # Game display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
