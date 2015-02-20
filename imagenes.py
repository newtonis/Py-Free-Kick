import pygame
pygame.init()


cancha = pygame.image.load("imagenes/cancha chica.png")
pelota = pygame.transform.scale(pygame.image.load("imagenes/pelota.png"),(15,15))
sombra = pygame.transform.scale(pygame.image.load("imagenes/sombra.png"),(15,15))
arco = pygame.image.load("imagenes/arco.png")
arco2 = pygame.image.load("imagenes/arco 2.png")
arco3 = pygame.image.load("imagenes/arco 3.png")
flecha = pygame.transform.rotozoom(pygame.image.load("imagenes/flecha.png"),0,0.5)
jugadores = []
for x in range(3):
    jugadores.append(pygame.transform.rotozoom(pygame.image.load(str("imagenes/jugador "+str(x+1)+".png")),0,0.35))
barra = pygame.image.load("imagenes/barra.png")
arqueros = []

arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 1.png"),0,0.25))
arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 2.png"),0,0.25))
arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 2 invertido.png"),0,0.25))
arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 3.png"),0,0.25))
arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 3 invertido.png"),0,0.25))
arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 4.png"),0,0.25))
arqueros.append(pygame.transform.rotozoom(pygame.image.load("imagenes/arquero 4 invertido.png"),0,0.25))