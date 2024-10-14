import pygame

def music_play_whole():
    pygame.mixer.init()
    
    wf1 = 'musics\Hello.mp3'
    pygame.mixer.music.load(wf1)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

def music_play_eat():
    wf2 = pygame.mixer.Sound('musics\eat.wav')
    wf2.set_volume(5)
    wf2.play()
    
