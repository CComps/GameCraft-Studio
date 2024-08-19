import pygame
from OpenGL.GL import *


class Grid:
    def __init__(self, screen, grid_size=32, color=(200, 200, 200)):
        """
        Initialize the grid.

        Parameters:
        - screen: The pygame screen surface.
        - grid_size: Size of the grid squares.
        - color: Color of the grid lines.
        """
        self.screen = screen
        self.grid_size = grid_size
        self.color = color

    def render(self):
        """Render the grid on the screen."""
        glColor4f(self.color[0] / 255, self.color[1] / 255, self.color[2] / 255, 1)
        glBegin(GL_LINES)
        for x in range(0, self.screen.get_width(), self.grid_size):
            glVertex2f(x, 0)
            glVertex2f(x, self.screen.get_height())
        for y in range(0, self.screen.get_height(), self.grid_size):
            glVertex2f(0, y)
            glVertex2f(self.screen.get_width(), y)
        glEnd()

    def snap_to_grid(self, pos):
        """
        Snap the given position to the nearest grid point.

        Parameters:
        - pos: A tuple (x, y) representing the position to snap.

        Returns:
        - A tuple (snapped_x, snapped_y) representing the snapped position.
        """
        x = round(pos[0] / self.grid_size) * self.grid_size
        y = round(pos[1] / self.grid_size) * self.grid_size
        return (x, y)
