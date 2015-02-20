import pygame
pygame.init()



class boton(pygame.sprite.Sprite):
    def __init__(self,imagen,imagenP,x,y,text = "",color = (0,0,0),imagenPuso = False):
        self.text = text
        if self.text != "":
            font1 = pygame.font.Font(None,20)
            self.texto = font1.render(self.text,0,color)    
        self.imagen = imagen
        self.originalImage = imagen
        if imagenPuso == False:
            self.imagenP = pygame.transform.rotozoom(imagen,0,1.1)
        else:
            self.imagenP = imagenP
        self.rect = self.imagen.get_rect()
        self.y = y
        self.x = x
        self.rectP = self.imagenP.get_rect()
        self.width = int(self.imagenP.get_width())
        self.height =  int(self.imagenP.get_height())
        self.rect.top =  (self.imagenP.get_height()-self.imagen.get_height())/2
        self.rect.left = (self.imagenP.get_width()-self.imagen.get_width())/2
        self.superficie = pygame.Surface((self.width,self.height))
    def mostrar(self,pantalla,tocado):    
        pantalla.blit(self.superficie,(self.x,self.y))
        if tocado == True and self.text != "":
            pantalla.blit(self.texto,(self.x+10,self.y+self.width))
    def actualizar(self,mouse,pantalla,color = (0,0,100),usarCual =False,cual = False):
        self.superficie.fill(color)
        mouseP,mouseX,mouseY = mouse
        presionado = False
        tocado = False
        if mouseX > self.x +self.rect.left and mouseX < self.x+self.rect.left+self.width:
            if mouseY > self.y +self.rect.top and mouseY < self.y +self.rect.top+self.height:
                if mouseP == True:
                    presionado = True
                tocado = True
       
           
        
        if tocado == True and usarCual == False:
            self.superficie.blit(self.imagenP,self.rectP)
        elif usarCual == False:
            self.superficie.blit(self.imagen,self.rect)
        elif usarCual == True:
            if cual == True:
                self.superficie.blit(self.imagen,self.rect)
            else:
                self.superficie.blit(self.imagenP,self.rectP)
        self.mostrar(pantalla,tocado)
        
        if presionado == True:
            return True
        else:
            return False
        
    def resetearImagen(self):
        self.imagen.blit(self.originalImage,(0,0))