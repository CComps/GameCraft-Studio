import pygame
from OpenGL.GL import *
import math


class Draw:
    def __init__(self, screen):
        self.screen = screen
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def draw_rect(self, color, rect, filled=True, line_width=1):
        """Draw a rectangle using OpenGL. If 'filled' is False, only the outline is drawn with specified line width."""
        glColor4f(color[0] / 255, color[1] / 255, color[2] / 255, 1)

        if filled:
            glBegin(GL_QUADS)  # Draw filled rectangle
        else:
            current_line_width = glGetFloatv(
                GL_LINE_WIDTH
            )  # Save the current line width
            glLineWidth(line_width)  # Set the line width for the outline
            glBegin(GL_LINE_LOOP)  # Draw only the outline

        glVertex2f(rect[0], rect[1])
        glVertex2f(rect[0] + rect[2], rect[1])
        glVertex2f(rect[0] + rect[2], rect[1] + rect[3])
        glVertex2f(rect[0], rect[1] + rect[3])
        glEnd()

        if not filled:
            glLineWidth(
                current_line_width
            )  # Reset the line width to its previous value

    def draw_circle(self, color, center, radius):
        """Draw a circle using OpenGL."""
        glColor4f(color[0] / 255, color[1] / 255, color[2] / 255, 1)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(center[0], center[1])
        for angle in range(0, 361, 10):
            x = center[0] + radius * math.cos(angle * math.pi / 180)
            y = center[1] + radius * math.sin(angle * math.pi / 180)
            glVertex2f(x, y)
        glEnd()

    def draw_line(self, color, start_pos, end_pos, width=1):
        """Draw a line using OpenGL."""
        glColor4f(color[0] / 255, color[1] / 255, color[2] / 255, 1)
        glLineWidth(width)
        glBegin(GL_LINES)
        glVertex2f(start_pos[0], start_pos[1])
        glVertex2f(end_pos[0], end_pos[1])
        glEnd()
