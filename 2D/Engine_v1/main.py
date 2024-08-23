import glfw
import numpy as np
import logging
from OpenGL.GL import *

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 10
selected_square = None
aspect_ratio = WINDOW_WIDTH / WINDOW_HEIGHT

def generate_grid(grid_size):
    logging.debug("Generating grid vertices and edges.")
    vertices = []
    edges = []
    square_size = WINDOW_WIDTH / grid_size
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * square_size
            y = j * square_size
            vertices.append([x, y])
            if i < grid_size - 1:
                edges.append([x, y, x + square_size, y])
            if j < grid_size - 1:
                edges.append([x, y, x, y + square_size])

    logging.debug("Generated %d vertices and %d edges.", len(vertices), len(edges))
    return vertices, edges

def render_grid(vertices, edges):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Render edges
    glColor3f(0.0, 0.0, 0.0)
    glBegin(GL_LINES)
    for edge in edges:
        glVertex2f(edge[0], edge[1])
        glVertex2f(edge[2], edge[3])
    glEnd()

    # Render squares
    square_size = WINDOW_WIDTH / GRID_SIZE
    for i in range(GRID_SIZE - 1):
        for j in range(GRID_SIZE - 1):
            top_left = vertices[i * GRID_SIZE + j]
            if selected_square == (i, j):
                glColor3f(1.0, 1.0, 1.0)  # Highlight selected square in white
            else:
                glColor3f(0.1, 0.1, 0.1)  # almost black
            glBegin(GL_QUADS)
            glVertex2f(top_left[0], top_left[1])
            glVertex2f(top_left[0] + square_size, top_left[1])
            glVertex2f(top_left[0] + square_size, top_left[1] + square_size)
            glVertex2f(top_left[0], top_left[1] + square_size)
            glEnd()

def select_square(window, x, y):
    """Select a square based on the mouse click coordinates."""
    global selected_square
    square_width = WINDOW_WIDTH / GRID_SIZE
    square_height = WINDOW_HEIGHT / GRID_SIZE

    grid_x = int(x // square_width)
    grid_y = int(y // square_height)

    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        selected_square = (grid_x, grid_y)
        logging.debug("Selected square: %s", selected_square)


def on_mouse_click(window, button, action, mods):
    if action == glfw.PRESS:
        x, y = glfw.get_cursor_pos(window)
        print(f"Mouse clicked at ({x}, {y})")
        select_square(window, x, y)

def on_window_resize(window, width, height):
    global aspect_ratio
    if height == 0:
        height = 1

    new_aspect_ratio = width / height

    if new_aspect_ratio > aspect_ratio:
        # Window is wider than the aspect ratio
        new_width = height * aspect_ratio
        new_height = height
    else:
        # Window is taller than the aspect ratio
        new_width = width
        new_height = width / aspect_ratio

    glViewport(int((width - new_width) / 2), int((height - new_height) / 2), int(new_width), int(new_height))

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -1, 1)  # Setup orthographic projection
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    # Initialize the library
    if not glfw.init():
        return

    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, "2D Grid Engine", None, None)
    if not window:
        glfw.terminate()
        return

    # Make the window's context current
    glfw.make_context_current(window)

    # Set the initial viewport and projection
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WINDOW_WIDTH, WINDOW_HEIGHT, 0, -1, 1)  # Setup orthographic projection
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Set up mouse button callback
    glfw.set_mouse_button_callback(window, on_mouse_click)

    # Set up window resize callback
    glfw.set_window_size_callback(window, on_window_resize)

    # Generate grid vertices and edges
    vertices, edges = generate_grid(GRID_SIZE)

    # Loop until the user closes the window
    while not glfw.window_should_close(window):
        # Render the grid
        render_grid(vertices, edges)

        # Swap front and back buffers
        glfw.swap_buffers(window)

        # Poll for and process events
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    logging.info("Starting the 2D Grid Engine.")
    main()
