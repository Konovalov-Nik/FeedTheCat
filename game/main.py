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

def load_assets():
    global CAT_IMAGE
    CAT_IMAGE = pygame.image.load(CAT_IMAGE_PATH)

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
    for food in FOOD_COORDS:
        if food[1] + FOOD_FISH_IMAGE.get_height() >= DISPALY_HEIGHT - CAT_IMAGE.get_height() \
            and food[0] + FOOD_FISH_IMAGE.get_width() >= CHARACTER_X \
            and food[0] <= CHARACTER_X + CAT_IMAGE.get_width():
            
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
    
    while pygame_eloop_running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame_eloop_running = False

            if event.type == pygame.KEYDOWN:
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
            draw_character(screen, CHARACTER_X, DISPALY_HEIGHT - CAT_IMAGE.get_height(), CAT_IMAGE)
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