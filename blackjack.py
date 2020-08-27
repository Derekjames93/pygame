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
    width = 800
    height = 800
    green_color = (0, 180, 0 )

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pete\'s Poker Place')
    clock = pygame.time.Clock()

    # Load dealer image
    dealer_image = pygame.image.load('images/Playing_card_spade_3.svg').convert_alpha()


    # Our dealer
    dealer = Dealer(dealer_image, [400, 200])
    dealer_group = pygame.sprite.Group()
    dealer_group.add(dealer)
    
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
        dealer_group.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

        # Game display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
