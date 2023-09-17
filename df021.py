'''
Faça um programa em python que abra e reproduza o áudio em MP3.
Obs: pygame.init() init para iniciar o pygame
Obs: pygame.mixer.music.load('m001.mp3') para importar p arquivo
     pygame.mixer.music.play() para tocar a musica
     pygame.event.wait() para parar a musica 

'''
import pygame
pygame.init()
pygame.mixer.music.load('m001.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()






