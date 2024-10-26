## INITIALIZE
import pygame
pygame.init()
pygame.display.set_mode((600,600))
running = True
####




## MAIN LOOP
while running:
    ## EVENTS
    events = pygame.event.get()
    for event in events:
        match event.type:
            case pygame.QUIT: running = False
    ####
    
    
####