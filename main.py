import pygame
import sys
from constants import SCREEN_HEIGHT,SCREEN_WIDTH,LINE_WIDTH,PLAYER_SHOOT_SPEED
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
from shot import Shot



def main():
    pygame.init()
    print(f'Starting Asteroids with pygame version: {pygame.version.ver}')
    print(f'Screen width: {SCREEN_WIDTH}\Screen height: {SCREEN_HEIGHT} ')

    pygame.font.init()
    font = pygame.font.Font(None,36)
    score_value = 0
    score_surface = font.render(f'score: {score_value}',True,"white")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    text_rect = score_surface.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, 30)

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,drawable,updatable)

    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField( ) 

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        score_surface = font.render(f'score: {score_value}',True,"white")
        screen.fill("black")
        screen.blit(score_surface,text_rect)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide_with(shot):
                    log_event("asteroid_shot")
                    score_value += 1
                    asteroid.split()
                    shot.kill()
            if asteroid.collide_with(player):
                log_event("player_hit")
                print("Game over!")
                print(f'Your score: {score_value}')
                sys.exit()
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000

        




if __name__ == "__main__":
    main()
