import pygame
import math
import time

pygame.init()

# Display settings
clock_size = 400
display = pygame.display.set_mode((clock_size, clock_size))
pygame.display.set_caption("Clock with PyGame")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Clock settings
center = (clock_size // 2, clock_size // 2)
clock_radius = clock_size // 2 - 5

# Choose a font and size
font_size = 24
clock_font = pygame.font.SysFont('Georgia', font_size)

def draw_mark(angle, length, color, width=1, mark_length=10):
    start_x = center[0] + (length - mark_length) * math.cos(math.radians(angle))
    start_y = center[1] - (length - mark_length) * math.sin(math.radians(angle))
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(display, color, (start_x, start_y), (end_x, end_y), width)

def draw_hand(angle, length, color, width=1, offset=10):
    # Offset from the center where the hand is 'pinned'
    start_x = center[0] - offset * math.cos(math.radians(angle))
    start_y = center[1] + offset * math.sin(math.radians(angle))

    # The end point remains the same, calculated from the full length
    end_x = center[0] + (length - offset) * math.cos(math.radians(angle))
    end_y = center[1] - (length - offset) * math.sin(math.radians(angle))

    pygame.draw.line(display, color, (start_x, start_y), (end_x, end_y), width)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill background
    display.fill(white)

    # Draw clock border
    pygame.draw.circle(display, black, center, clock_radius, 4)

    # Draw hour and minute marks
    for i in range(60):
        angle = 90 - (i * 360 / 60)
        if i % 5 == 0:  # Hour marks (every 5 minutes)
            draw_mark(angle, clock_radius - 2, black, width=4, mark_length=15)
        else:  # Minute marks
            draw_mark(angle, clock_radius - 2, black, width=1, mark_length=10)

    for num in range(1, 13):
        angle = math.radians(90 - (num * 360 / 12))  # Calculate angle for each number
        text = clock_font.render(str(num), True, black)  # Render the number text
        text_rect = text.get_rect(center=(center[0] + math.cos(angle) * (clock_radius - 40),
                                        center[1] - math.sin(angle) * (clock_radius - 40)))
        display.blit(text, text_rect)  # Draw the text on the screen

    # Get current time
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate angles for each hand
    hour_angle = 90 - (360 * (hours + minutes / 60) / 12)
    minute_angle = 90 - (360 * minutes / 60)
    second_angle = 90 - (360 * seconds / 60)

    # Draw clock hands
    draw_hand(hour_angle, clock_radius * 0.5, black, 6)  # Hour hand
    draw_hand(minute_angle, clock_radius * 0.8, black, 4, 20)  # Minute hand
    draw_hand(second_angle, clock_radius * 0.9, red, 2, 40)  # Second hand

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(15)


pygame.quit()
