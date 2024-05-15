import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw a Perfect Rectangle")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

font = pygame.font.SysFont(None, 48)
score_font = pygame.font.SysFont(None, 72)
fineprint_font = pygame.font.SysFont(None, 24)

# Function to calculate the score based on rectangle properties
def calculate_score(rect):
    x, y, w, h = rect
    if w <= 0 or h <= 0:
        return 0
    aspect_ratio = max(w, h) / min(w, h)
    perfect_ratio = 1.0
    score = max(0, 100 - abs(perfect_ratio - aspect_ratio) * 100)
    return score

def draw_gradient_line(screen, start_pos, end_pos, color1, color2):
    x1, y1 = start_pos
    x2, y2 = end_pos
    for i in range(100):
        x = x1 + (x2 - x1) * i / 100
        y = y1 + (y2 - y1) * i / 100
        r = color1[0] + (color2[0] - color1[0]) * i / 100
        g = color1[1] + (color2[1] - color1[1]) * i / 100
        b = color1[2] + (color2[2] - color1[2]) * i / 100
        pygame.draw.line(screen, (int(r), int(g), int(b)), (x, y), (x + 1, y + 1), 1)

# Main loop
running = True
drawing = False
rect_start = (0, 0)
rect_end = (0, 0)
center_point = (WIDTH // 2, HEIGHT // 2)
current_rect = None
current_score = None

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            rect_start = event.pos
            current_rect = None  # Reset current rectangle
            current_score = None  # Reset current score
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            rect_end = event.pos
            current_rect = pygame.Rect(min(rect_start[0], rect_end[0]), min(rect_start[1], rect_end[1]), abs(rect_end[0] - rect_start[0]), abs(rect_end[1] - rect_start[1]))
            current_score = calculate_score((0, 0, current_rect.width, current_rect.height))

    if current_rect:
        draw_gradient_line(screen, current_rect.topleft, current_rect.topright, RED, YELLOW)
        draw_gradient_line(screen, current_rect.topright, current_rect.bottomright, YELLOW, GREEN)
        draw_gradient_line(screen, current_rect.bottomright, current_rect.bottomleft, GREEN, YELLOW)
        draw_gradient_line(screen, current_rect.bottomleft, current_rect.topleft, YELLOW, RED)
        if current_score is not None:
            score_text = score_font.render(f"{current_score:.1f}%", True, ORANGE)
            screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - score_text.get_height() // 2))
            new_best_text = font.render("New best score", True, WHITE)
            screen.blit(new_best_text, (WIDTH // 2 - new_best_text.get_width() // 2, HEIGHT // 2 + score_text.get_height() // 2))

    pygame.draw.circle(screen, WHITE, center_point, 5)

    if drawing:
        rect_end = pygame.mouse.get_pos()
        temp_rect = pygame.Rect(min(rect_start[0], rect_end[0]), min(rect_start[1], rect_end[1]), abs(rect_end[0] - rect_start[0]), abs(rect_end[1] - rect_start[1]))
        pygame.draw.rect(screen, WHITE, temp_rect, 1)
        draw_gradient_line(screen, temp_rect.topleft, temp_rect.topright, RED, YELLOW)
        draw_gradient_line(screen, temp_rect.topright, temp_rect.bottomright, YELLOW, GREEN)
        draw_gradient_line(screen, temp_rect.bottomright, temp_rect.bottomleft, GREEN, YELLOW)
        draw_gradient_line(screen, temp_rect.bottomleft, temp_rect.topleft, YELLOW, RED)

    # Fine print
    fineprint_text = fineprint_font.render("created by Isaac Tomeho, inspired by Neal.fun", True, WHITE)
    screen.blit(fineprint_text, (WIDTH - fineprint_text.get_width() - 10, HEIGHT - fineprint_text.get_height() - 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
