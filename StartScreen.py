import pygame

#Font creator function provided by Tristan
def create_Font(t,s=22,c=(255, 0, 0), b=False,i=False):
    font = pygame.font.SysFont("Times New Roman", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text


#The menu class
class menu:
    def __init__(self):
        self.image = pygame.image.load("Images/TITLE.png")
        self.image=pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()
    #Defines the first button for the menu
    def button1(self,screen):
        self.button1set = pygame.draw.rect(screen, (255, 0, 0), (30, 200, 250, 100), 3, 5)
        return self.button1set


showthis = menu()

