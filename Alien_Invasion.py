import sys
import pygame
from settings import Settings
import ctypes


class AlienInvasion:
    """class for resource management and game behavior"""
    def __init__(self):
        """init game and build game resources"""
        pygame.init()

        # get screen size from users settings
        # user32 = ctypes.windll.user32
        # screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        # self.screen = pygame.display.set_mode(screensize)
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # assigning a background colour
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """start of main loop"""
        while True:
            # catch clicks by mouse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            # displaying the last drawn screen
            pygame.display.flip()


if __name__ == '__main__':
    # initiate and run the game
    ai = AlienInvasion()
    ai.run_game()
