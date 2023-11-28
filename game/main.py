import pygame
import random
import datetime

GAME_NAME = "Ням ням, вкусняшки"

DISPALY_WIDTH = 595
DISPALY_HEIGHT = 842

BACKGROUND_IMAGE_PATH = "assets/background.png"
BACKGROUND_IMAGE = None

ICON_IMAGE_PATH = "assets/icon.png"
ICON_IMAGE = None

CAT_IMAGE_PATH = "assets/cat.png"
CAT_IMAGE = None

POOP_UNICORN_IMAGE_PATH = "assets/poop_unicorn.png"
POOP_UNICORN_IMAGE = None

DOG_IMAGE_PATH = "assets/dog.png"
DOG_IMAGE = None

CAPYBARA_IMAGE_PATH = "assets/capybara.png"
CAPYBARA_IMAGE = None

BUNNY_IMAGE_PATH = "assets/bunny.png"
BUNNY_IMAGE = None

CAKE_IMAGE_PATH = "assets/cake.png"
CAKE_IMAGE = None

FOOD_FISH_IMAGE_PATH = "assets/fish.png"
FOOD_FISH_IMAGE = None

CHARACTER_X = 0
X_SPEED = 0

FOOD_DROP_SPEED = 6
MAX_FOOD_COUNT = 2

FOOD_COORDS = []

SCORE = 0
TARGET_SCORE = 20

START_TIME = None
END_TIME = None

GAME_IN_PROGRESS = False

SELECTED_CHARACTER = None

def load_assets():
    global CAT_IMAGE
    CAT_IMAGE = pygame.image.load(CAT_IMAGE_PATH)

    global POOP_UNICORN_IMAGE
    POOP_UNICORN_IMAGE = pygame.image.load(POOP_UNICORN_IMAGE_PATH)

    global DOG_IMAGE
    DOG_IMAGE = pygame.image.load(DOG_IMAGE_PATH)

    global CAPYBARA_IMAGE
    CAPYBARA_IMAGE = pygame.image.load(CAPYBARA_IMAGE_PATH)

    global BUNNY_IMAGE
    BUNNY_IMAGE = pygame.image.load(BUNNY_IMAGE_PATH)

    global CAKE_IMAGE
    CAKE_IMAGE = pygame.image.load(CAKE_IMAGE_PATH)

    global FOOD_FISH_IMAGE
    FOOD_FISH_IMAGE = pygame.image.load(FOOD_FISH_IMAGE_PATH)

    global BACKGROUND_IMAGE
    BACKGROUND_IMAGE = pygame.image.load(BACKGROUND_IMAGE_PATH)

    global ICON_IMAGE
    ICON_IMAGE = pygame.image.load(ICON_IMAGE_PATH)

def start_game():
    global CHARACTER_X
    CHARACTER_X = 0

    global X_SPEED
    X_SPEED = 0

    global FOOD_COORDS
    FOOD_COORDS = []

    global SCORE
    SCORE = 0

    global GAME_IN_PROGRESS
    GAME_IN_PROGRESS = True

    global START_TIME
    START_TIME = datetime.datetime.now()

    global END_TIME
    END_TIME = None

def draw_start_screen(screen):
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("Нажмите пробел чтобы начать игру", True, (0, 0, 0))
    screen.blit(text, (DISPALY_WIDTH / 2 - text.get_width() / 2, DISPALY_HEIGHT / 2 - text.get_height() / 2))

    draw_available_characters(screen)

def draw_character(screen, x, y, character=CAT_IMAGE):
    screen.blit(character, (x, y))

def update_food():
    global FOOD_COORDS
    for food in FOOD_COORDS:
        food[1] += FOOD_DROP_SPEED

    FOOD_COORDS = [food for food in FOOD_COORDS if food[1] < DISPALY_HEIGHT]

    if len(FOOD_COORDS) < MAX_FOOD_COUNT:
        FOOD_COORDS.append([random.randint(0, DISPALY_WIDTH - FOOD_FISH_IMAGE.get_width()), 0])

def draw_all_food(screen, food_img=FOOD_FISH_IMAGE):
    for food in FOOD_COORDS:
        draw_food(screen, food[0], food[1], food_img)

def draw_food(screen, x, y, food=FOOD_FISH_IMAGE):
    screen.blit(food, (x, y))

def draw_background(screen):
    screen.blit(BACKGROUND_IMAGE, (0, 0))

def draw_score(screen, score):
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (DISPALY_WIDTH / 2 - text.get_width() / 2, 0))

def check_collision_food():
    global SCORE
    global SELECTED_CHARACTER
    for food in FOOD_COORDS:
        if food[1] + FOOD_FISH_IMAGE.get_height() >= DISPALY_HEIGHT - SELECTED_CHARACTER.get_height() \
            and food[0] + FOOD_FISH_IMAGE.get_width() >= CHARACTER_X \
            and food[0] <= CHARACTER_X + SELECTED_CHARACTER.get_width():
            
            SCORE += 1
            FOOD_COORDS.remove(food)

def check_win():
    global SCORE
    global TARGET_SCORE
    if SCORE >= TARGET_SCORE:
        return True
    return False

def draw_win(screen):
    pretty_time_delta = str(END_TIME - START_TIME).split(".")[0]

    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Игра окончена! {pretty_time_delta} чтобы набрать {TARGET_SCORE} очков", True, (0, 0, 0))
    screen.blit(text, (DISPALY_WIDTH / 2 - text.get_width() / 2, DISPALY_HEIGHT / 2 - text.get_height() / 2))

    draw_available_characters(screen)

def draw_available_characters(screen):
    max_height = get_max_character_height()
    
    draw_character(screen, 0, 0, CAT_IMAGE)
    #draw assigned number under image  
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("1", True, (0, 0, 0))
    screen.blit(text, (CAT_IMAGE.get_width() / 2 - text.get_width() / 2, max_height ))
    
    draw_character(screen, CAT_IMAGE.get_width(), 0, POOP_UNICORN_IMAGE)
    #draw assigned number under image  
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("2", True, (0, 0, 0))
    screen.blit(text, (CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() / 2 - text.get_width() / 2, max_height ))

    draw_character(screen, CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width(), 0, DOG_IMAGE)
    #draw assigned number under image
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("3", True, (0, 0, 0))
    screen.blit(text, (CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width() / 2 - text.get_width() / 2, max_height ))

    draw_character(screen, CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width(), 0, CAPYBARA_IMAGE)
    #draw assigned number under image
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("4", True, (0, 0, 0))
    screen.blit(text, (CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width() + CAPYBARA_IMAGE.get_width() / 2 - text.get_width() / 2, max_height ))

    draw_character(screen, CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width() + CAPYBARA_IMAGE.get_width(), 0, BUNNY_IMAGE)
    #draw assigned number under image
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("5", True, (0, 0, 0))
    screen.blit(text, (CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width() + CAPYBARA_IMAGE.get_width() + BUNNY_IMAGE.get_width() / 2 - text.get_width() / 2, max_height ))

    draw_character(screen, CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width() + CAPYBARA_IMAGE.get_width() + BUNNY_IMAGE.get_width(), 0, CAKE_IMAGE)
    #draw assigned number under image
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("6", True, (0, 0, 0))
    screen.blit(text, (CAT_IMAGE.get_width() + POOP_UNICORN_IMAGE.get_width() + DOG_IMAGE.get_width() + CAPYBARA_IMAGE.get_width() + BUNNY_IMAGE.get_width() + CAKE_IMAGE.get_width() / 2 - text.get_width() / 2, max_height ))

    draw_selected_character(screen)


def draw_selected_character(screen):
    max_character_height = get_max_character_height()
    
    global SELECTED_CHARACTER
    #draw in the middle widht above the characters
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("Выбран персонаж:", True, (0, 0, 0))
    screen.blit(text, (DISPALY_WIDTH / 2 - text.get_width() / 2, max_character_height * 2))

    draw_character(screen, DISPALY_WIDTH / 2 - SELECTED_CHARACTER.get_width() / 2, max_character_height * 2 + text.get_height(), SELECTED_CHARACTER)

def get_max_character_height():
    return max(CAT_IMAGE.get_height(), POOP_UNICORN_IMAGE.get_height(), DOG_IMAGE.get_height(), CAPYBARA_IMAGE.get_height(), BUNNY_IMAGE.get_height(), CAKE_IMAGE.get_height())

def main():
    load_assets()
    pygame.init()
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_icon(ICON_IMAGE)
    screen = pygame.display.set_mode((DISPALY_WIDTH, DISPALY_HEIGHT), vsync=1)
    clock = pygame.time.Clock()
    pygame_eloop_running = True

    global GAME_IN_PROGRESS

    global X_SPEED
    global CHARACTER_X

    global START_TIME
    START_TIME = datetime.datetime.now()

    global SELECTED_CHARACTER
    SELECTED_CHARACTER = CAT_IMAGE
    
    while pygame_eloop_running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame_eloop_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and not GAME_IN_PROGRESS:
                    SELECTED_CHARACTER = CAT_IMAGE
                if event.key == pygame.K_2 and not GAME_IN_PROGRESS:
                    SELECTED_CHARACTER = POOP_UNICORN_IMAGE 
                if event.key == pygame.K_3 and not GAME_IN_PROGRESS:
                    SELECTED_CHARACTER = DOG_IMAGE
                if event.key == pygame.K_4 and not GAME_IN_PROGRESS:
                    SELECTED_CHARACTER = CAPYBARA_IMAGE
                if event.key == pygame.K_5 and not GAME_IN_PROGRESS:
                    SELECTED_CHARACTER = BUNNY_IMAGE
                if event.key == pygame.K_6 and not GAME_IN_PROGRESS:
                    SELECTED_CHARACTER = CAKE_IMAGE
                
                if event.key == pygame.K_LEFT:
                    if CHARACTER_X > 5:
                        X_SPEED = -5
                    else:
                        X_SPEED = 0
                elif event.key == pygame.K_RIGHT:
                    if CHARACTER_X < DISPALY_WIDTH - CAT_IMAGE.get_width():
                        X_SPEED = 5
                    else:
                        X_SPEED = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    X_SPEED = 0 

                if event.key == pygame.K_SPACE and not GAME_IN_PROGRESS:
                    start_game()
            

        if X_SPEED > 0 and CHARACTER_X > DISPALY_WIDTH - CAT_IMAGE.get_width():
            X_SPEED = 0
        elif X_SPEED < 0 and CHARACTER_X < 0:
            X_SPEED = 0
         
        
        
        if check_win():
            if GAME_IN_PROGRESS:
                global END_TIME
                END_TIME = datetime.datetime.now()
                GAME_IN_PROGRESS = False
            draw_win(screen)

        draw_background(screen)

        if GAME_IN_PROGRESS:    
            CHARACTER_X += X_SPEED    
            check_collision_food()
            draw_character(screen, CHARACTER_X, DISPALY_HEIGHT - SELECTED_CHARACTER.get_height(), SELECTED_CHARACTER)
            update_food()
            draw_all_food(screen, FOOD_FISH_IMAGE)
            draw_score(screen, SCORE)
        else:
            if not END_TIME:
                draw_start_screen(screen)
            else:
                draw_win(screen)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    exit(main())