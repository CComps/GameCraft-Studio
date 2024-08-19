# UI/ui_manager.py
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

    def render(self):
        """Render the Dear PyGui UI."""
        dpg.render_dearpygui_frame()

    def cleanup(self):
        """Clean up the Dear PyGui context."""
        dpg.destroy_context()
