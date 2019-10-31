import pygame
import sys
import os

class PlayMP3:
    def playMP3(self, file):
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        file = '{}/{}.mp3'.format(path, file)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
