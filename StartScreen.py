import pygame

#Font creator function provided by Tristan
def create_Font(t,s=22,c=(255, 0, 0), b=False,i=False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text


#The menu class
class menu:
    def __init__(self):
        self.image = pygame.image.load("Images/TITLE.png")
        self.image=pygame.transform.scale(self.image, (800, 600))
        self.rect = self.image.get_rect()
        self.button1colour = (255, 0, 0)
    #Defines the first button for the menu
    def button1(self,screen):
        self.button1set = pygame.draw.rect(screen, self.button1colour, (30, 200, 250, 100), 3, 5)
        return self.button1set
    #Checks if the mouse is clicking the start button for the game
    def mousecheck(self):
        self.button1colour = (255, 0, 0)
        currentpos = pygame.mouse.get_pos()
        if currentpos[0] >= 30 and currentpos[0] <= 280:
            if currentpos[1] >= 200 and currentpos[1] <= 300:
                self.button1colour = (255, 255, 102)
                check2 = pygame.mouse.get_pressed(num_buttons=3)
                if check2 == (True, False, False):
                    #Placeholder for calling level 1
                    Level = 1
                    return Level


showthis = menu()

