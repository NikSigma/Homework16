import pygame

pygame.init()


screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sigma")
red_color = (255, 0, 0)


font = pygame.font.SysFont(None, 48)
text_surface = font.render("Pygame!", True, (255, 255, 255))  
text_rect = text_surface.get_rect(center=(320, 240))  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(red_color)


    screen.blit(text_surface, text_rect)


    pygame.draw.circle(screen, (0, 255, 0), (500, 100), 30)   
    pygame.draw.circle(screen, (0, 0, 255), (320, 240), 30)   
    pygame.draw.circle(screen, (255, 255, 0), (140, 380), 30) 


    pygame.draw.rect(screen, (255, 0, 255), (50, 50, 40, 60))     
    pygame.draw.rect(screen, (0, 255, 255), (260, 190, 60, 40))  
    pygame.draw.rect(screen, (255, 165, 0), (460, 330, 80, 50))   

   
    pygame.display.flip()

pygame.quit()
