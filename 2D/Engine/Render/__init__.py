from .Draw import Draw

#############################
# from .Shaders import Shaders
# from .Sprite import Sprite
# from .Camera import Camera
# from .Texture import Texture
# from .Rendering_Pipeline import RenderingPipeline
#############################


class Render:
    def __init__(self, screen):
        self.draw = Draw(screen)
        #############################
        # self.shaders = Shaders()
        # self.sprite = Sprite()
        # self.camera = Camera()
        # self.texture = Texture()
        # self.pipeline = RenderingPipeline()
        #############################

    def update(self):
        """This could be used to update the rendering pipeline or other tasks."""
        pass
