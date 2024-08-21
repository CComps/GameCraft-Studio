import pygame
from Render import Render
from Render.Grid import Grid  # Import the Grid class
from OpenGL.GL import *
from UI.ui_manager import UIManager  # Import the UIManager class


class Main:
    def __init__(self):
        self.Grid_Snapping = True
        self.selected_cells = []  # To keep track of the selected cells
        self.active_cell = None  # To keep track of the active cells

        pygame.init()
        self.screen = pygame.display.set_mode(
            (800, 600), pygame.OPENGL | pygame.DOUBLEBUF
        )
        pygame.display.set_caption("GameCraft Studio - Grid Selection Test")

        # Set up the viewport and projection
        glViewport(0, 0, 800, 600)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, 800, 600, 0, -1, 1)  # Orthographic projection (2D)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.render = Render(self.screen)
        self.grid = Grid(self.screen, grid_size=32)  # Initialize the Grid
        self.ui_manager = UIManager(self)  # Initialize the UIManager with reference to Main

        self.clock = pygame.time.Clock()
        self.running = True

    def get_mouse_pos(self, select=False, shift=False):
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if self.Grid_Snapping and select:
            if self.selected_cells != []:
                if not shift:
                    self.selected_cells = []
            x_mouse += -15
            y_mouse += -15
            mouse_pos = (x_mouse, y_mouse)
            snapped_pos = self.grid.snap_to_grid(mouse_pos)
            if shift:
                self.selected_cells.append(snapped_pos)
            self.active_cell = snapped_pos
            return [snapped_pos, self.active_cell]
        elif self.Grid_Snapping:
            x_mouse += -15
            y_mouse += -15
            mouse_pos = (x_mouse, y_mouse)
            snapped_pos = self.grid.snap_to_grid(mouse_pos)
            self.render.draw.draw_rect(
                (255, 0, 0), (snapped_pos[0], snapped_pos[1], 32, 32)
            )
        elif select:
            if self.selected_cells != []:
                if not shift:
                    self.selected_cells = []
            x_mouse += -15
            y_mouse += -15
            mouse_pos = (x_mouse, y_mouse)
            snapped_pos = self.grid.snap_to_grid(mouse_pos)
            if shift:
                self.selected_cells.append(snapped_pos)
            self.active_cell = snapped_pos
            return [snapped_pos, self.active_cell]
        else:
            mouse_pos = (x_mouse, y_mouse)
        return mouse_pos

    def handle_events(self):
        # Detect if Shift key is held
        shift_held = pygame.key.get_mods() & pygame.KMOD_LSHIFT

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_g:
                    self.Grid_Snapping = not self.Grid_Snapping

            # Handle mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    data_from_mouse = self.get_mouse_pos(select=True, shift=shift_held)
                    self.active_cell = data_from_mouse[1]
                    mouse_pos = data_from_mouse[0]

                elif event.button == 2:  # Middle Mouse click
                    pass

                elif event.button == 3:  # Right click
                    self.ui_manager.show_menu(pygame.mouse.get_pos())

            # Handle the UIManager events
            self.ui_manager.handle_event(event)

    def run(self):
        while self.running:
            self.handle_events()

            # Clear the screen with a background color
            glClearColor(0.1, 0.1, 0.1, 1)  # Dark grey background
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()

            # Render the grid
            self.grid.render()

            # Snap mouse position to grid and draw a red rectangle
            data_from_mouse = self.get_mouse_pos(select=False)
            mouse_pos = data_from_mouse[0]

            # Draw the selected cell in yellow
            if self.selected_cells:
                for self.selected_cell in self.selected_cells:
                    self.render.draw.draw_rect(
                        (255, 255, 0),  # Yellow color
                        (
                            self.selected_cell[0],
                            self.selected_cell[1],
                            self.grid.grid_size,
                            self.grid.grid_size,
                        ),
                        filled=False,
                        line_width=3,
                    )
            else:
                if self.active_cell is not None:
                    self.render.draw.draw_rect(
                        (255, 255, 0),  # Yellow color
                        (
                            self.active_cell[0],
                            self.active_cell[1],
                            self.grid.grid_size,
                            self.grid.grid_size,
                        ),
                        filled=False,
                        line_width=3,
                    )

            # Render the UI elements
            self.ui_manager.render()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        self.ui_manager.cleanup()  # Clean up Dear PyGui context


if __name__ == "__main__":
    main_program = Main()
    main_program.run()
