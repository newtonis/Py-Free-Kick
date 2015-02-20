import pygame
pygame.init

class sprite(pygame.sprite.Sprite):
    def __init__(self,imagen,x = 0,y = 0,rectangles = False):
        
        self.imagen = imagen
        self.originalImagen = self.imagen
        
        self.rect = self.imagen.get_rect()
        self.rects = []
        
        if rectangles != False:
            for x in range(len(rectangles)):
                self.rects.append(pygame.rect.Rect((rectangles[x][0],rectangles[x][1],rectangles[x][2],rectangles[x][3])))
       
        for num in range(len(self.rects)):
            x = self.rects[num].left
            y = self.rects[num].top
            h = self.rects[num].height
            w = self.rects[num].width
            #pygame.draw.lines(self.imagen,(200,100,200),True,((x,y),(x+w,y),(x+w,y+h),(x,y+h)),2)
        
        self.x = x
        self.y = y
        self.t = self.imagen.get_size()
    def cambiarXY(self,x,y):
        self.x = x
        self.y = y
    def moverIP(self,x,y):
        self.x+=x
        self.y+=y
    def aumentarTamanio(self,escala):
        actual1,actual2 = self.t
        self.imagen = pygame.transform.scale(self.imagen,(int(actual1*escala),int(actual2*escala)))
        self.t = self.imagen.get_size()
    def devolverPintadoEscala(self,escala,pantalla):  
        actual1,actual2 = self.t
        escalaImage = pygame.transform.scale(self.imagen,(int(actual1*escala),int(actual2*escala)))                                      
        h,w = int(actual1*escala),int(actual2*escala)
        top = self.y -w/2
        left = self.x -h/2
        pantalla.blit(escalaImage,(left,top))
    def setearHW(self,h,w):
        self.imagen = pygame.transform.scale(self.imagen,(int(h),int(w)))
    def devolverRotada(self,angulo,pantalla):
        
        rotadaImage = pygame.transform.rotate(self.originalImagen,angulo)   
        actual1,actual2 = rotadaImage.get_size()                       
        h,w = int(actual1),int(actual2)
        top = self.y -w/2
        left = self.x -h/2
        pantalla.blit(rotadaImage,(left,top))
    def pintar(self,pantalla):
        actual1,actual2 = self.t
        self.rect.top = self.y -actual2/2
        self.rect.left = self.x -actual1/2
        pantalla.blit(self.imagen,self.rect)
    def cambiarImagen(self,nuevaImagen):
        self.imagen = nuevaImagen
        self.rect = self.imagen.get_rect()
    def generarRotados(self):
        
        self.rotados = []
        for x in range(-90,90):
            imagen = pygame.transform.rotate(self.originalImagen,x)
            w,h = imagen.get_size()
            
            rectImagen =self.x- w/2,self.y -h/2
            
            self.rotados.append([imagen,rectImagen])
    def actualizarRotador(self,pantalla,rotado):
        pantalla.blit(self.rotados[rotado][0],self.rotados[rotado][1])
    def colicionar(self,objeto):
        
        for x in range(len(self.rects)):
            rectActual = pygame.rect.Rect((self.rects[x].left+self.rect.left,self.rects[x].top+self.rect.top,self.rects[x].width,self.rects[x].height))
            rectActualVecino = pygame.rect.Rect((objeto.rect.left,objeto.rect.top,objeto.rect.width,objeto.rect.height))
            
            if rectActual.colliderect(rectActualVecino) == True:
               
                return True
        
        
        return False
          
        
        
        
   