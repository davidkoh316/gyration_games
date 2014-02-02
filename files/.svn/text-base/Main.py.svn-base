

def main():

    import pygame
    import InputManager
    import TitleScreen
    import Globals

    INTERVAL = 0.04
    TARGET_FPS = 60

    pygame.init()

    pygame.display.set_caption("Astoria")

    pyclock = pygame.time.Clock()

    size = Globals.WIDTH, Globals.HEIGHT = 800, 600

    Globals.SCREEN = pygame.display.set_mode(size)

    Globals.FONT = pygame.font.Font("font/artgothicbold.ttf", 130)

    Globals.STATE = TitleScreen.TitleScreen()

    fpsFont = pygame.font.Font(None, 22)

    currentTime = pygame.time.get_ticks()
    remainderTime = 0.0

    while(Globals.RUNNING):
        newTime = pygame.time.get_ticks()
        frameTime = (newTime - currentTime) / 1000.0
        currentTime = newTime

        if Globals.DEBUG_MODE:
            pyclock.tick()

        Globals.SCREEN.fill((0, 0, 0))  # remove this when unnecessary

        Globals.STATE.draw()

        if Globals.DEBUG_MODE:
            fpsSurface = fpsFont.render(
                "FPS: %3.4f" % (pyclock.get_fps()), True, (255, 0, 0))
            Globals.SCREEN.blit(fpsSurface, (20, 20))

        pygame.display.flip()

        remainderTime += frameTime
        while remainderTime > INTERVAL:
            InputManager.update()

            Globals.STATE.update(INTERVAL)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Globals.RUNNING = False

            remainderTime -= INTERVAL

    pygame.quit()

if __name__ == "__main__":
    main()
