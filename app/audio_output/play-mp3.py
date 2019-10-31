import pygame
file = '/Users/luciaschmidt/Workspace/themis-hunger-solutions/welcome.mp3'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()
