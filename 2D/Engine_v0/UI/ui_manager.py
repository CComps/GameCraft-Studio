import pygame
import dearpygui.dearpygui as dpg


class UIManager:
    def __init__(self, main_program):
        """
        Initializes the UI Manager.

        Parameters:
        - main_program: A reference to the Main class of the game engine.
        """
        self.main_program = main_program

        # Create the Dear PyGui context
        dpg.create_context()

        # Create the UI layout
        self.create_ui()

        # Set up and show the Dear PyGui viewport
        dpg.create_viewport(title="GameCraft Studio - UI", width=300, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()

        # Initialize Pygame UI elements
        self.font = pygame.font.SysFont(None, 24)
        self.menu_items = ["Thing 1", "Thing 2", "Thing 3", "Thing 4"]
        self.menu_visible = False
        self.menu_rects = []
        self.menu_position = (0, 0)

    def create_ui(self):
        """Creates the UI layout."""
        with dpg.window(label="Controls", width=300, height=600):
            dpg.add_text("Tool Options")
            dpg.add_button(
                label="Toggle Grid Snapping", callback=self.toggle_grid_snapping
            )
            dpg.add_button(label="Quit", callback=self.quit)

    def toggle_grid_snapping(self):
        """Toggle the grid snapping feature in the game engine."""
        self.main_program.Grid_Snapping = not self.main_program.Grid_Snapping

    def quit(self):
        """Stop the main program's run loop."""
        self.main_program.running = False

    def show_menu(self, position):
        """Show a right-click context menu at the given position."""
        self.menu_visible = True
        self.menu_position = position
        self.menu_rects = []
        for index, item in enumerate(self.menu_items):
            item_rect = pygame.Rect(position[0], position[1] + index * 30, 100, 25)
            self.menu_rects.append(item_rect)

    def hide_menu(self):
        """Hide the right-click context menu."""
        self.menu_visible = False

    def draw_menu(self, screen):
        """Draw the right-click context menu."""
        if not self.menu_visible:
            return
        
        for index, item in enumerate(self.menu_items):
            item_rect = self.menu_rects[index]
            pygame.draw.rect(screen, (50, 50, 50), item_rect)
            pygame.draw.rect(screen, (255, 255, 255), item_rect, 2)
            text_surface = self.font.render(item, True, (255, 255, 255))
            screen.blit(text_surface, (item_rect.x + 5, item_rect.y + 5))

    def handle_event(self, event):
        """Handle Pygame events for the context menu."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.menu_visible:  # Left click
                for rect in self.menu_rects:
                    if rect.collidepoint(event.pos):
                        print(f"{self.menu_items[self.menu_rects.index(rect)]} selected")
                        self.hide_menu()

            elif event.button == 3:  # Right click
                self.hide_menu()

    def render(self):
        """Render the Dear PyGui UI and the Pygame context menu."""
        dpg.render_dearpygui_frame()

    def cleanup(self):
        """Clean up the Dear PyGui context."""
        dpg.destroy_context()
