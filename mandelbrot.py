# inspired by the mandelbrot set we made in CS161 at PCC with Nick Insalata.

import pygame, sys

pygame.init()

# Resolution of the pygame window, not picture quality.
RESOLUTION = 700

# 200 seems good when zooming. 1000 is good when not zooming. Higher = better resolution, lower = much faster draws
# Defines the max number of times we iterate for a given number
MAX_ITERATIONS = 200

# set up the window
DISPLAY_SURFACE = pygame.display.set_mode((RESOLUTION, RESOLUTION))
pygame.display.set_caption('Mandelbrot Set')


def is_bounded(Cr, Ci):
    # M0 = 0
    Mr = 0.0
    Mi = 0.0
    
    for i in range(0, MAX_ITERATIONS):
        # Mn = Mn-1 * Mn-1 + C
        temp = Mr
        Mr = Mr**2 - Mi**2 + Cr
        Mi = 2*temp*Mi + Ci
        
        # pathagorean theorem. Calculating if distance from origin is greater than 2.
        if Mr**2 + Mi**2 > 4:
            return i
    return i


def draw(zoom, x0, y0, pixel_array):
    # generate GUI coords
    for r in range(0, RESOLUTION):
        for c in range(0, RESOLUTION):
            # convert from GUI coords to complex coords
            Cr = x0 - zoom/2 + zoom*c/RESOLUTION
            Ci = y0 + zoom/2 - zoom*r/RESOLUTION
            
            # test the point and return the number of iterations
            n = is_bounded(Cr, Ci)

            # The RGB values of each coordinate are a function of the number of iterations
            #pixel_array[c][r] = ((10*n)%255, (10*n)%255, (10*n)%255) 
            #pixel_array[c][r] = ((2*n)%255, (4*n)%255, (6*n)%255)
            #pixel_array[c][r] = ((2*n)%255, (1*n)%255, (3*n)%255)
            #pixel_array[c][r] = ((50*n)%255, (2*n)%255, (16*n)%255)
            pixel_array[c][r] = ((4*n)%255, (3*n)%255, (8*n)%255)


def zoom_in(position): 
    global zoom, x0, y0

    # resize and recenter on the click coords
    x0 = x0 - zoom/2 + zoom * position[0] / RESOLUTION
    y0 = y0 + zoom/2 - zoom * position[1] / RESOLUTION
    zoom /= 10


# create pixel array
pixel_array = pygame.PixelArray(DISPLAY_SURFACE)

zoom = 4.0 # 4.0 seems best, but this can be anything
x0 = 0.0
y0 = 0.0


draw(zoom, x0, y0, pixel_array)

# run the 'game' loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            del pixel_array
            pygame.quit()
            sys.exit()

        # handle MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            zoom_in(position)
            draw(zoom, x0, y0, pixel_array)

    pygame.display.update()

