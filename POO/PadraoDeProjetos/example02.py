from abc import ABC, abstractclassmethod

class PngInterface(ABC):
    @abstractclassmethod
    def draw(self):
        raise NotImplementedError


class PngImage(PngInterface):
    def __init__(self, png_path):
        self.png_path = png_path
        self.format = "raster"

    def draw(self):
        return print(f"Drawing PNG {self.png_path} with {self.format}")

class SvgAdapter(PngInterface):
    def __init__(self, svg):
        self.svg_image = svg

    def draw(self):
        return self.svg.get_image()

class SvgImage:
    def __init__(self, svg_path):
        self.svg_path = svg_path
        self.format = "vector"

    def get_image(self):
        return print(f"Drawing SVG {self.svg_path} with {self.format}")

SvgAdapter(SvgImage("arquivo.txt")).draw()
PngImage("arquivo.png").draw()