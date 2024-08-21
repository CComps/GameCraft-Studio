import sys
import numpy as np
import logging
import dearpygui.dearpygui as dpg

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 10
selected_square = None
show_viewport = True

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

def render_grid(drawlist, vertices, edges):
    square_size = WINDOW_WIDTH / GRID_SIZE
    for edge in edges:
        dpg.draw_line(p1=(edge[0], edge[1]), p2=(edge[2], edge[3]), color=(0, 0, 0, 255), thickness=1.0, parent=drawlist)

    for i in range(GRID_SIZE - 1):
        for j in range(GRID_SIZE - 1):
            top_left = vertices[i * GRID_SIZE + j]
            dpg.draw_quad(
                p1=(top_left[0], top_left[1]),
                p2=(top_left[0] + square_size, top_left[1]),
                p3=(top_left[0] + square_size, top_left[1] + square_size),
                p4=(top_left[0], top_left[1] + square_size),
                color=(200, 200, 200, 255),
                fill=(200, 200, 200, 255),
                parent=drawlist
            )

def setup_ui():
    logging.debug("Setting up the UI.")
    dpg.create_context()
    dpg.create_viewport(title="2D Grid Engine", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

    vertices, edges = generate_grid(GRID_SIZE)

    with dpg.window(label="Main Window", width=WINDOW_WIDTH, height=WINDOW_HEIGHT):
        with dpg.drawlist(width=WINDOW_WIDTH, height=WINDOW_HEIGHT) as drawlist:
            render_grid(drawlist, vertices, edges)
            dpg.set_item_user_data(drawlist, edges)

    dpg.setup_dearpygui()
    dpg.show_viewport()

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()

def toggle_viewport(sender, app_data):
    global show_viewport
    show_viewport = not show_viewport
    logging.info("Toggling viewport. Now it is %s.", "visible" if show_viewport else "hidden")

if __name__ == "__main__":
    logging.info("Starting the 2D Grid Engine.")

    # Setup UI
    setup_ui()
    logging.info("2D Grid Engine is running.")
