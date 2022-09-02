import datetime
import pygame
import os
import time
import sys
pygame.font.init()


class Button:
    def __init__(self, pos, button_width, button_height, font_size, color, text=""):
        self.button_rect = pygame.Rect(pos, (button_width, button_height))
        self.text_font = pygame.font.SysFont("Comics Scans", font_size)
        
        self.text = text
        self.color = color
        self.pos = pos

    def draw(self, button_color, text_pos):
        pygame.draw.rect(WIN, button_color, self.button_rect, border_radius = 5)

        text_surface = self.text_font.render(self.text, False, self.color)
        center_text = text_surface.get_rect(center = text_pos)
        WIN.blit(text_surface, (center_text))


SCREEN_WIDTH, SCREEN_HEIGHT = (700, 550)
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(("MyCharacter"))

FPS = 60
clock = pygame.time.Clock()

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHT_BLUE = "#0288d1"
CYAN = (0, 255, 255)
DARKER_BLUE = "#3FA0EF"

background = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "futuristic_screen.jpg")), (SCREEN_WIDTH , SCREEN_HEIGHT))

human_body = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "human_silhouette.png")), (640, 365))

button_width = 23
button_height = 23
button_font_size = 45
add_button_x = 380
remove_button_x = 345

add_button1 = Button((add_button_x, 117), button_width, button_height, button_font_size, WHITE, "+")
add_button2 = Button((add_button_x, 187), button_width, button_height, button_font_size, WHITE, "+")
add_button3 = Button((add_button_x, 257), button_width, button_height, button_font_size, WHITE, "+")
add_button4 = Button((add_button_x, 327), button_width, button_height, button_font_size, WHITE, "+")
add_button5 = Button((add_button_x, 397), button_width, button_height, button_font_size, WHITE, "+")

remove_button1 = Button((remove_button_x, 117), button_width, button_height, button_font_size, WHITE, "-")
remove_button2 = Button((remove_button_x, 187), button_width, button_height, button_font_size, WHITE, "-")
remove_button3 = Button((remove_button_x, 257), button_width, button_height, button_font_size, WHITE, "-")
remove_button4 = Button((remove_button_x, 327), button_width, button_height, button_font_size, WHITE, "-")
remove_button5 = Button((remove_button_x, 397), button_width, button_height, button_font_size, WHITE, "-")

int_stat_loc = os.path.join("Assets", "int_stat.txt")
wis_stat_loc = os.path.join("Assets", "wis_stat.txt")
phys_stat_loc = os.path.join("Assets", "phys_stat.txt")
sd_stat_loc = os.path.join("Assets", "sd_stat.txt")    
conf_stat_loc = os.path.join("Assets", "conf_stat.txt")

def larger_add_button(button_x, button_y):
    larger_add_button = Button((button_x - 1.5, button_y - 1.5), button_width + 3, button_height + 3, button_font_size + 3, WHITE, "+")
    larger_add_button.draw(LIGHT_BLUE, (button_x + 11, button_y + 8))

def larger_remove_button(button_x, button_y):
    larger_remove_button = Button((button_x - 13.5, button_y - 11.5), button_width + 3, button_height + 3, button_font_size + 3, WHITE, "-")
    larger_remove_button.draw(LIGHT_BLUE, (button_x, button_y))

def days_counter():
    date_font = pygame.font.SysFont("Comics Scans", 73)

    start_date = 120
    days_left = datetime.date(2023, 1, 1) - datetime.date.today()
    days_left = str(days_left).split(",")
    days_left = days_left[0].split(" ")
    days_left = int(days_left[0])
    countdown_day = start_date - days_left

    date_text = date_font.render(f"Day {countdown_day}", 1, DARKER_BLUE)
    WIN.blit(date_text, (230 + 37.5, 32))


def add_button_click(button_rect1, button_rect2, button_rect3, button_rect4, button_rect5):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect1.collidepoint(mouse_pos):
        larger_add_button(add_button1.pos[0], add_button1.pos[1])

        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect1 == add_button1.button_rect:
                with open(int_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        tx.write("1")
                    else:
                        with open(int_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data += 1
                                f.close()
                        with open(int_stat_loc, "w") as file:
                            file.write(str(data))

    if button_rect2.collidepoint(mouse_pos):
        larger_add_button(add_button2.pos[0], add_button2.pos[1])
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect2 == add_button2.button_rect:
                with open(wis_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        tx.write("1")
                    else:
                        with open(wis_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data += 1
                                f.close()
                        with open(wis_stat_loc, "w") as file:
                            file.write(str(data))

    if button_rect3.collidepoint(mouse_pos):
        larger_add_button(add_button3.pos[0], add_button3.pos[1])
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect3 == add_button3.button_rect:
                with open(phys_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        tx.write("1")
                    else:
                        with open(phys_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data += 1
                                f.close()
                        with open(phys_stat_loc, "w") as file:
                            file.write(str(data))
    
    if button_rect4.collidepoint(mouse_pos):
        larger_add_button(add_button4.pos[0], add_button4.pos[1])
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect5 == add_button5.button_rect:
                with open(sd_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        tx.write("1")
                    else:
                        with open(sd_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data += 1
                                f.close()
                        with open(sd_stat_loc, "w") as file:
                            file.write(str(data))

    if button_rect5.collidepoint(mouse_pos):
        larger_add_button(add_button5.pos[0], add_button5.pos[1])
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect5 == add_button5.button_rect:
                with open(conf_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        tx.write("1")
                    else:
                        with open(conf_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data += 1
                                f.close()
                        with open(conf_stat_loc, "w") as file:
                            file.write(str(data))


def remove_button_click(button_rect1, button_rect2, button_rect3, button_rect4, button_rect5):
    mouse_pos = pygame.mouse.get_pos()
    if button_rect1.collidepoint(mouse_pos):
        larger_remove_button(remove_button1.pos[0] + 13, remove_button1.pos[1] + 10)
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect1 == remove_button1.button_rect:
                with open(int_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        pass
                    else:
                        with open(int_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data -= 1
                                f.close()
                        with open(int_stat_loc, "w") as file:
                            if data < 1:
                                pass
                            else:
                                file.write(str(data))

    if button_rect2.collidepoint(mouse_pos):
        larger_remove_button(remove_button2.pos[0] + 13, remove_button2.pos[1] + 10)
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect2 == remove_button2.button_rect:
                with open(wis_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        pass
                    else:
                        with open(wis_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data -= 1
                                f.close()
                        with open(wis_stat_loc, "w") as file:
                            if data < 1:
                                pass
                            else:
                                file.write(str(data))

    if button_rect3.collidepoint(mouse_pos):
        larger_remove_button(remove_button3.pos[0] + 13, remove_button3.pos[1] + 10)
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect3 == remove_button3.button_rect:
                with open(phys_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        pass
                    else:
                        with open(phys_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data -= 1
                                f.close()
                        with open(phys_stat_loc, "w") as file:
                            if data < 1:
                                pass
                            else:
                                file.write(str(data))
    
    if button_rect4.collidepoint(mouse_pos):
        larger_remove_button(remove_button4.pos[0] + 13, remove_button4.pos[1] + 10)
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect5 == remove_button5.button_rect:
                with open(sd_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        pass
                    else:
                        with open(sd_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data -= 1
                                f.close()
                        with open(sd_stat_loc, "w") as file:
                            if data < 1:
                                pass
                            else:
                                file.write(str(data))

    if button_rect5.collidepoint(mouse_pos):
        larger_remove_button(remove_button5.pos[0] + 13, remove_button5.pos[1] + 10)
        if pygame.mouse.get_pressed()[0]:
            time.sleep(0.3)
            if button_rect5 == remove_button5.button_rect:
                with open(conf_stat_loc, "r+") as tx:
                    if tx.read() == "":
                        pass
                    else:
                        with open(conf_stat_loc, "r") as f:
                            for line in f.readlines():
                                data = int(line.rstrip())
                                data -= 1
                                f.close()
                        with open(conf_stat_loc, "w") as file:
                            if data < 1:
                                pass
                            else:
                                file.write(str(data))

def draw_text():
    text_font = pygame.font.SysFont("BLOKLINKSANGULAR", 35)
    line_num = 0

    with open(os.path.join("Assets", "int_stat.txt"), "r") as f:
        int_text = text_font.render(f"Intelligence: {f.read().rstrip()}", 1, CYAN)

    with open(os.path.join("Assets", "wis_stat.txt"), "r") as f:
        wis_text = text_font.render(f"Wisdom: {f.read().rstrip()}", 1, CYAN)

    with open(os.path.join("Assets", "phys_stat.txt"), "r") as f:
        phys_text = text_font.render(f"Physique: {f.read().rstrip()}", 1, CYAN)

    with open(os.path.join("Assets", "sd_stat.txt"), "r") as f:
        sk_text = text_font.render(f"Self Discipline: {f.read().rstrip()}", 1, CYAN)

    with open(os.path.join("Assets", "conf_stat.txt"), "r") as f:
        conf_text = text_font.render(f"Confidence: {f.read().rstrip()}", 1, CYAN)
            
    WIN.blit(int_text, (add_button1.pos[0] + 30, add_button1.pos[1]))
    WIN.blit(wis_text, (add_button2.pos[0] + 30, add_button2.pos[1]))
    WIN.blit(phys_text, (add_button3.pos[0] + 30, add_button3.pos[1]))
    WIN.blit(sk_text, (add_button4.pos[0] + 30, add_button4.pos[1]))
    WIN.blit(conf_text, (add_button5.pos[0] + 30, add_button5.pos[1]))
            

def draw_window():
    WIN.blit(background, (0, 0))

    remove_button1.draw(LIGHT_BLUE, (remove_button1.pos[0] + 13, remove_button1.pos[1] + 10))
    remove_button2.draw(LIGHT_BLUE, (remove_button2.pos[0] + 13, remove_button2.pos[1] + 10))
    remove_button3.draw(LIGHT_BLUE, (remove_button3.pos[0] + 13, remove_button3.pos[1] + 10))
    remove_button4.draw(LIGHT_BLUE, (remove_button4.pos[0] + 13, remove_button4.pos[1] + 10))
    remove_button5.draw(LIGHT_BLUE, (remove_button5.pos[0] + 13, remove_button5.pos[1] + 10))

    add_button1.draw(LIGHT_BLUE, (add_button1.pos[0] + 13, add_button1.pos[1] + 10))
    add_button2.draw(LIGHT_BLUE, (add_button2.pos[0] + 13, add_button2.pos[1] + 10))
    add_button3.draw(LIGHT_BLUE, (add_button3.pos[0] + 13, add_button3.pos[1] + 10))
    add_button4.draw(LIGHT_BLUE, (add_button4.pos[0] + 13, add_button4.pos[1] + 10))
    add_button5.draw(LIGHT_BLUE, (add_button5.pos[0] + 13, add_button5.pos[1] + 10))

    remove_button_click(remove_button1.button_rect, remove_button2.button_rect, remove_button3.button_rect, remove_button4.button_rect, remove_button5.button_rect)

    add_button_click(add_button1.button_rect, add_button2.button_rect, add_button3.button_rect, add_button4.button_rect, add_button5.button_rect)
    
    draw_text()

    WIN.blit(human_body, (-110, 93))

    days_counter()

    pygame.display.update()


def main():
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
                pygame.quit()
                sys.exit()

        draw_window()

if __name__ == "__main__":
    main()
