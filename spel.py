import pygame
import os
import random
pygame.init()

pygame.display.set_caption("CKV spel")

WIDTH, HEIGHT = 1000, 800
FPS = 60
frame = 0
PLAYER_VEL = 200
LANE_1 = 465
LANE_2 = 530
LANE_3 = 595
LANE_4 = 640
LANE_5 = 695
LANE_6 = 760

window = pygame.display.set_mode((WIDTH, HEIGHT))
road = pygame.image.load(os.path.join('.','road_standing.png')).convert_alpha()
fence = pygame.image.load(os.path.join('.','background_fence_city.png')).convert_alpha()
city = pygame.image.load(os.path.join('.','backest_ground_city_3.png')).convert_alpha()
museum_background = pygame.image.load(os.path.join('.','museum_background.png')).convert_alpha()
jan_de_man = pygame.image.load(os.path.join('.','jan_de_man.png')).convert_alpha()
beeld_van_apa = pygame.image.load(os.path.join('.','beeld_van_aap.png')).convert_alpha()
sterrennacht = pygame.image.load(os.path.join('.','sterrennacht.png')).convert_alpha()
pindakaas_vloer = pygame.image.load(os.path.join('.','pindakaas_vloer.png')).convert_alpha()
car_top_down = pygame.image.load(os.path.join('.','car_top_down.png')).convert_alpha()
car_side_view = pygame.image.load(os.path.join('.','car_side_view.png')).convert_alpha()
car_thief = pygame.image.load(os.path.join('.','car_museum_thief.png')).convert_alpha()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
ADDENEMY = pygame.USEREVENT + 1
ADDPAINTING = pygame.USEREVENT + 1
def update_frame():
    pass

pygame.time.set_timer(ADDENEMY, 1000)
pygame.time.set_timer(ADDPAINTING, 3000)

bgX2 = road.get_width
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load(os.path.join('.','car_side_view.png')).convert_alpha()
        #self.surf.fill((0, 0, 0))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        lane_decision = random.randint(1, 6)
        if lane_decision == 1:
            lane_number = LANE_1
        elif lane_decision == 2:
            lane_number = LANE_2
        if lane_decision == 3:
            lane_number = LANE_3
        elif lane_decision == 3:
            lane_number = LANE_3
        if lane_decision == 4:
            lane_number = LANE_4
        elif lane_decision == 5:
            lane_number = LANE_5
        if lane_decision == 6:
            lane_number = LANE_6
        
        
        self.rect = self.surf.get_rect(

            center=(

                random.randint(1000 + 20, 1000 + 100),

                lane_number,

            )

        )

        self.speed = random.randint(5, 20)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
class Painting(pygame.sprite.Sprite):

    def __init__(self):
        super(Painting, self).__init__()
        self.surf = pygame.Surface((300, 500))
        self.surf.fill((0, 0, 0))
        
        
        
        self.rect = self.surf.get_rect(

            center=(

                random.randint(1000 + 300, 1000 + 400),

                300,

            )

        )

        self.speed = 10
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        


def main(window):
    jan_de_man_grabbed = False
    sterrennacht_grabbed = False
    aap_beeld_grabbed = False
    player = Player()
    enemies = pygame.sprite.Group()
    speed = 1
    all_sprites = pygame.sprite.Group()

    all_sprites.add(player)

    player.rect.x = 300
    player.rect.y = LANE_1
    lane_number = 1 
    clock = pygame.time.Clock()
    street_x = 0
    street_x_2 = street_x + 8000
    city_x = 0
    city_x_2 = city_x + 8000
    run = True
    event_status = 0
    jan_de_man_x = 1300
    sterrennacht_x = 1300
    aap_beeld_x = 1300
    car_museum_x = -25
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event_status == 0:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if jan_de_man_x > -300:
                            jan_de_man_grabbed = True
                        if jan_de_man_x <= -300 and sterrennacht_x > -300:
                            sterrennacht_grabbed = True
                        if sterrennacht_x <= -300 and aap_beeld_x > -300:
                            aap_beeld_grabbed = True
                         
            if event_status == 1:    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        if lane_number > 1:
                            lane_number = lane_number - 1
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        if lane_number < 6:
                            lane_number = lane_number + 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_EQUALS:
                        speed = speed + 5
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_MINUS:
                        speed = speed - 5
                if event.type == ADDENEMY:
                    if event_status == 1:
                        new_enemy = Enemy()

                        enemies.add(new_enemy)

                        all_sprites.add(new_enemy)
                    
        if event_status == 1:
            street_x = street_x - speed
            street_x_2 = street_x_2 - speed
            city_x = city_x - speed / 4
            city_x_2 = city_x_2 - speed / 4
            window.blit(city, (city_x, 0))
            window.blit(city, (city_x_2, 0))
            window.blit(fence, (street_x, 0))
            window.blit(fence, (street_x_2, 0))
            window.blit(road, (street_x, 0))
            window.blit(road, (street_x_2, 0))
            window.blit(player.surf, player.rect)
            for entity in all_sprites:
                window.blit(entity.surf, entity.rect)
            if pygame.sprite.spritecollideany(player, enemies):
                player.kill()
                run = False
            
            if lane_number == 1:
                player.rect.y = LANE_1
            if lane_number == 2:
                player.rect.y = LANE_2
            if lane_number == 3:
                player.rect.y = LANE_3
            if lane_number == 4:
                player.rect.y = LANE_4
            if lane_number == 5:
                player.rect.y = LANE_5
            if lane_number == 6:
                player.rect.y = LANE_6
            


            print(str(city_x) + "," + str(street_x))
            if street_x <= -8000:
                street_x = street_x_2 + 8000
            if street_x_2 <= -8000:
                street_x_2 = street_x + 8000
            if city_x <= -8000:
                city_x = city_x_2 + 8000
            if city_x_2 <= -8000:
                city_x_2 = city_x + 8000
            enemies.update()
        elif event_status == 0:
            if aap_beeld_x > -300:
                window.blit(museum_background, (0, 0))
            if aap_beeld_x <= -300:
                window.blit(pindakaas_vloer, (0, 0))
            if jan_de_man_x > -300:
                if not jan_de_man_grabbed:
                    window.blit(jan_de_man, (jan_de_man_x, 100))
                jan_de_man_x = jan_de_man_x - 10
                print(jan_de_man_x)
            if jan_de_man_x <= -300 and sterrennacht_x > -300:
                if not sterrennacht_grabbed:
                    window.blit(sterrennacht, (sterrennacht_x, 100))
                sterrennacht_x = sterrennacht_x - 10
                print(sterrennacht_x)
            if sterrennacht_x <= -300 and aap_beeld_x > -300:
                if not aap_beeld_grabbed:
                    window.blit(beeld_van_apa, (aap_beeld_x, 100))
                aap_beeld_x = aap_beeld_x - 10
                print(aap_beeld_x)
            if aap_beeld_x <= -300 and car_museum_x <= 1000:
                pygame.draw.rect(window, "BLACK", pygame.Rect(0, 405,car_museum_x , 5))
                pygame.draw.rect(window, "BLACK", pygame.Rect(0, 430,car_museum_x , 5))
                window.blit(car_top_down, (car_museum_x, 400))
                car_museum_x = car_museum_x + 10
            if car_museum_x >= 1000:
                event_status = 1
            if aap_beeld_x > -300:
                window.blit(car_thief, (125, 0))
                

        pygame.display.flip()
            
        
    pygame.quit()
    quit()

if __name__ == '__main__':
    main(window)