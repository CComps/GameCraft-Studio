import pygame
from OpenGL.GL import *
import math


class Draw:
    def __init__(self, screen):
        self.screen = screen
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def draw_rect(self, color, rect):
        """Draw a rectangle using OpenGL."""
        glColor4f(color[0] / 255, color[1] / 255, color[2] / 255, 1)
        glBegin(GL_QUADS)
        glVertex2f(rect[0], rect[1])
        glVertex2f(rect[0] + rect[2], rect[1])
        glVertex2f(rect[0] + rect[2], rect[1] + rect[3])
        glVertex2f(rect[0], rect[1] + rect[3])
        glEnd()

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
