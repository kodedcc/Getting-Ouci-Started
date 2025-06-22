
# safe_ouci_pixel_engine.py

# This simulates decision-making over a 10x10 grid, changing pixel color based on input data

import random

WIDTH = 10
HEIGHT = 10

def simulate_pixel_grid(time_of_day, temperature):
    grid = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            # Simulate logic: warm = red, cool = blue, neutral = green
            if temperature > 30:
                color = (255, random.randint(0, 100), 0)  # red-ish
            elif temperature < 15:
                color = (0, 100, 255)  # blue-ish
            else:
                color = (0, 255, 100)  # green-ish
            row.append(color)
        grid.append(row)
    return grid

if __name__ == "__main__":
    frame = simulate_pixel_grid(time_of_day="afternoon", temperature=25)
    for row in frame:
        print(row)
