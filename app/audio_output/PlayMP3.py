import pygame

class PlayMP3:
    def playMP3(self, file):
        file = '/Users/luciaschmidt/Workspace/themis-hunger-solutions/{}.mp3'.format(file)

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        pygame.event.wait()
