import pygame
import time

pygame.init()

# Display settings
window_size = (400, 200)
display = pygame.display.set_mode(window_size)
pygame.display.set_caption("Digital Clock")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Global color variable for the segments
SEGMENT_COLOR = (0, 255, 0)  # A bright green color for the LCD segments

# Global variable for segment positions (relative)
# --0--
# 1   2
# --3--
# 4   5
# --6--
SEGMENT_POSITIONS = {
    0: [(5, 2), (7, 0), (33, 0), (35, 2), (33, 4), (7, 4)],
    1: [(2, 5), (4, 7), (4, 33), (2, 35), (0, 33), (0, 7)],
    2: [(38, 5), (36, 7), (36, 33), (38, 35), (40, 33), (40, 7)],
    3: [(5, 38), (7, 36), (33, 36), (35, 38), (33, 40), (7, 40)],
    4: [(2, 41), (4, 43), (4, 69), (2, 71), (0, 69), (0, 43)],
    5: [(38, 41), (36, 43), (36, 69), (38, 71), (40, 69), (40, 43)],
    6: [(5, 74), (7, 72), (33, 72), (35, 74), (33, 76), (7, 76)]
}

SEGMENT_BOOLS = {
    0: [True, True, True, False, True, True, True],
    1: [False, False, True, False, False, True, False],
    2: [True, False, True, True, True, False, True],
    3: [True, False, True, True, False, True, True],
    4: [False, True, True, True, False, True, False],
    5: [True, True, False, True, False, True, True],
    6: [True, True, False, True, True, True, True],
    7: [True, False, True, False, False, True, False],
    8: [True, True, True, True, True, True, True],
    9: [True, True, True, True, False, True, True]
}

clock = pygame.time.Clock()

def draw_digit(position, segments_bool):
    x_offset, y_offset = position
    # Iterate over each segment's boolean state and draw if True
    for i, segment_is_on in enumerate(segments_bool):
        if segment_is_on:
            # Adjust each segment position by the digit's top-left corner position
            adjusted_segment_positions = [(x + x_offset, y + y_offset)
                                          for x, y in SEGMENT_POSITIONS[i]]
            pygame.draw.polygon(display, SEGMENT_COLOR, adjusted_segment_positions)

def draw_colon(position, color):
    x_offset, y_offset = position
    # Top dot
    pygame.draw.circle(display, color, (x_offset, y_offset + 25), 3)
    # Bottom dot
    pygame.draw.circle(display, color, (x_offset, y_offset + 50), 3)

def draw_time():
    x_offset, y_offset = (30, 60)
    # Get current time
    current_time_str = time.strftime("%H:%M:%S", time.localtime())

    # Calculate the spacing between the digits and the size of each digit
    digit_spacing = 10  # Space between digits
    digit_width = 42 + digit_spacing  # Each digit is about 42 pixels wide

    # Iterate through each character in the time string
    for i, char in enumerate(current_time_str):
        if char == ':':  # Positions where colons should be drawn
            x_offset += digit_spacing / 2
            colon_position = (x_offset, y_offset)
            draw_colon(colon_position, SEGMENT_COLOR)
            x_offset += digit_spacing * 1.5
            continue
        
        # Convert the character to an integer to access SEGMENT_BOOLS
        digit = int(char)
        
        # Draw the digit using the draw_digit method
        draw_digit((x_offset, y_offset), SEGMENT_BOOLS[digit])
        x_offset += digit_width

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the background
    display.fill(black)

    # Render the time
    draw_time()
    
    # Update the display
    pygame.display.update()
    
    # Cap the frame rate to 1 FPS to update the clock every second
    clock.tick(1)

pygame.quit()
