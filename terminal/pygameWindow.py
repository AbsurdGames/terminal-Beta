from imports import *

X = 500
Y = 500

backgroundColor = "white"
pygameText = "[Type text in terminal]"
txtSize = 100

fontDisplay = pygame.font.SysFont('Arial', txtSize)

def mainUpdate():
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()


def window():
    screen = pygame.display.set_mode((X, Y))
    
    screen.fill(backgroundColor)

    txt = fontDisplay.render(pygameText, False, (255, 0, 0))

    while True:
        mainUpdate()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()

        screen.blit(txt, (10, 10))
