import pygame
import random
from random import randint

pygame.init()

# les constantes
WIDTH, HEIGHT = 600, 600
BACKGROUND_COLOR = (10, 10, 190)
FISH_COLOR = (255, 242, 0)
SHARK_COLOR = (237, 28, 36) 

UP = (0, -10)
DOWN = (0, 10)
LEFT = (-10, 0)
RIGHT = (10, 0)
STOP = (0, 0)
RANDOMNB = (randint(1, 59)*10)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WaTor!")

clock = pygame.time.Clock()

image1 = pygame.image.load("poisson1.png").convert_alpha()
image2 = pygame.image.load("shark.png").convert_alpha()

class Fish:
    """ Classe poisson"""
    def __init__(self, pos_x, pos_y, image, chronon = 1):
        self.image = image
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.chronon = chronon

    def draw_fish(self):
        SCREEN.blit(image1, (element.pos_x, element.pos_y))

    def check_color(self) : # renvoie les couleurs des positions adjacentes
        #######         UP              #######
        if self.pos_y - 10 >= 0 :
            newup = self.pos_y - 10
            couleurup = SCREEN.get_at((self.pos_x,newup))
        else :
            newup = self.pos_y - 10 + HEIGHT
            couleurup = SCREEN.get_at((self.pos_x,newup))
        
        #######         RIGHT            #######
        if self.pos_x + 10 + 10 <= WIDTH :
            newright = self.pos_x + 10
            couleurright = SCREEN.get_at((newright,self.pos_y))
        else :
            newright = self.pos_x + 10 + 10 - WIDTH
            couleurright = SCREEN.get_at((newright,self.pos_y))

        #######         DOWN            #######
        if self.pos_y + 10 + 10 <= HEIGHT :
            newdown = self.pos_y + 10
            couleurdown = SCREEN.get_at((self.pos_x,newdown))
        else :
            newdown = self.pos_y + 10 + 10 - HEIGHT
            couleurdown = SCREEN.get_at((self.pos_x,newdown))
    
        #######         LEFT            #######
        if self.pos_x - 10 >= 0 :
            newleft = self.pos_x - 10
            couleurleft = SCREEN.get_at((newleft,self.pos_y))  
        else :
            newleft = self.pos_x - 10 + WIDTH
            couleurleft = SCREEN.get_at((newleft,self.pos_y))
        
        return couleurup, couleurdown, couleurleft, couleurright


    def move_fish(self): # selon la couleur identifiée dans la méthode check_color(), permet de bouger le poisson
        couleurup, couleurdown, couleurleft, couleurright = self.check_color()

        liste_mouvement = [UP, DOWN, LEFT, RIGHT]
        if couleurup[0:3] == FISH_COLOR:
            liste_mouvement.remove(UP)
        elif couleurdown[0:3] == FISH_COLOR:
            liste_mouvement.remove(DOWN)
        elif couleurleft[0:3] == FISH_COLOR:
            liste_mouvement.remove(LEFT)
        elif couleurright[0:3] == FISH_COLOR:
            liste_mouvement.remove(RIGHT)

        if len(liste_mouvement) == 0:
            liste_mouvement.append(STOP)
        direction = random.choice(liste_mouvement)

        if direction == LEFT:
            if self.pos_x - 10 >= 0 :
                self.pos_x -= 10
            else :
                self.pos_x = self.pos_x - 10 + WIDTH
        
        if direction == RIGHT:
            if self.pos_x + 10 + 10 <= WIDTH :
                self.pos_x += 10
            else :
                self.pos_x = self.pos_x + 10 - WIDTH

        if direction == UP:
            if self.pos_y -10 >= 0 :
                self.pos_y -= 10
            else :
                self.pos_y = self.pos_y - 10 + HEIGHT

        if direction == DOWN:
            if self.pos_y + 10 + 10 <= HEIGHT :
                self.pos_y += 10
            else :
                self.pos_y = self.pos_y + 10 + 10 - HEIGHT
        
        self.chronon += 1
        

    def fish_multiply(self) : # multiplication des poissons 
        if self.chronon == 6:
            self.chronon = 1
            x = self.pos_x
            y = self.pos_y
            nom_poisson = Fish(x, y, image1)
            fish_list.append(nom_poisson)
            self.move_fish()
        

    def fish_die(self): # mort des poissons
        surrequin = SCREEN.get_at((self.pos_x,self.pos_y))
        if surrequin == SHARK_COLOR:
            fish_list.remove(self)

    def fish_score(self, len_liste): # peut afficher le nb de poissons sur l'écran
        font = pygame.font.SysFont('Arial', 15, 0)
        score_text = font.render(f"Nombre de poissons : {len_liste}", 1, (5,5,5))
        SCREEN.blit(score_text, (20,20))


class Shark(Fish):
    """ Classe requin : hérite de la class Fish avec ajout des points d'energie"""
    def __init__(self, pos_x, pos_y, image, chronon = 1, energie = 20):
        super().__init__(pos_x, pos_y, image, chronon)
        self.energie = energie

    def draw_shark(self): # attribue une image et la positionne sur l'écran
        SCREEN.blit(image2, (element.pos_x, element.pos_y))

    def move_shark(self): # selon la couleur identifiée dans la méthode check_color(), permet de bouger le requin
        couleurup, couleurdown, couleurleft, couleurright = self.check_color()  

        liste_mouvement = [UP, DOWN, LEFT, RIGHT]
        if couleurup[0:3] == SHARK_COLOR :
            liste_mouvement.remove(UP)
        elif couleurdown[0:3] == SHARK_COLOR :
            liste_mouvement.remove(DOWN)
        elif couleurleft[0:3] == SHARK_COLOR :
            liste_mouvement.remove(LEFT)
        elif couleurright[0:3] == SHARK_COLOR :
            liste_mouvement.remove(RIGHT)

        # if len(liste_mouvement) == 0:
        #     liste_mouvement.append(STOP)

        if couleurup[0:3] == FISH_COLOR :
            direction = UP
        elif couleurdown[0:3] == FISH_COLOR :
            direction = DOWN
        elif couleurleft[0:3] == FISH_COLOR :
            direction = LEFT
        elif couleurright[0:3] == FISH_COLOR :
            direction = RIGHT
        else:
            direction = random.choice(liste_mouvement)

        if direction == LEFT:
            if self.pos_x - 10 >= 0 :
                self.pos_x -= 10
            else :
                self.pos_x = self.pos_x - 10 + WIDTH 

        if direction == RIGHT:
            if self.pos_x + 10 + 10 <= WIDTH :
                self.pos_x += 10
            else :
                self.pos_x = self.pos_x + 10 - WIDTH 

        if direction == UP:
            if self.pos_y -10 >= 0 :
                self.pos_y -= 10
            else :
                self.pos_y = self.pos_y - 10 + HEIGHT

        if direction == DOWN:
            if self.pos_y + 10 + 10 <= HEIGHT :
                self.pos_y += 10
            else :
                self.pos_y = self.pos_y + 10 + 10 - HEIGHT

        self.chronon += 1
        self.energie -= 1 


    def eat_fish(self):
        surpoisson = SCREEN.get_at((self.pos_x,self.pos_y))
        if surpoisson == FISH_COLOR :
            self.energie += 1
    
    def shark_multiply(self):
        if self.chronon == 7 :
            self.chronon = 1
            x = self.pos_x
            y = self.pos_y
            nom_requin = Shark(x, y, image2)
            shark_list.append(nom_requin)
            self.move_shark()

    def shark_die(self):
        if self.energie == 0:
            shark_list.remove(self)

    def shark_score(self, len_liste):
        font = pygame.font.SysFont('Arial', 16, 0)
        score_text = font.render(f"Nombre de requins : {len_liste}", 1, (5,5,5))
        SCREEN.blit(score_text, (20,40))


shark_list = [] # on crée la liste des poissons
def creer_requin(nb_requin):
    for i in range(nb_requin):
        x = (randint(1, 59)*10)
        y = (randint(1, 59)*10)
        new = Shark(x, y, image2)
        shark_list.append(new)


fish_list = [] # on crée la liste des requins
def creer_poisson(nb_poisson):
    for i in range(nb_poisson):
        x = (randint(1, 59)*10)
        y = (randint(1, 59)*10)
        new = Fish(x, y, image1)
        fish_list.append(new)


creer_requin(10) # Nombre de requins qui vont apparaitre sur la map
creer_poisson(10) # Nombre de poissons qui vont apparaitre sur la map

pygame.mixer.music.load("babyshark.mp3") ### petite musique d'ambiance :-)
pygame.mixer.music.play(-1)
Running = True
while Running:
    clock.tick(1)
    SCREEN.fill(BACKGROUND_COLOR)

    for element in shark_list:
        #element.shark_score(len(shark_list))
        element.draw_shark()
        element.eat_fish()
        element.move_shark()
        element.shark_die()
        element.shark_multiply()
        
    for element in fish_list:
        #element.fish_score(len(fish_list))
        element.draw_fish()
        element.move_fish()
        element.fish_die()
        element.fish_multiply()
        
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            Running = False

pygame.quit()