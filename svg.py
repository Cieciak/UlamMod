
class SVG_Element:

    def __init__(self, *, depth: int = 0, **_) -> None: self.depth = depth

class SVG_Circle(SVG_Element):

    ARGS = ['cx', 'cy', 'r', 'fill']
    PATTERN = r'<circle cx="_cx_" cy="_cy_" r="_r_" fill="_fill_"/>'

    def __init__(self, cx: float, cy: float, r: float, *, fill: str = 'black', depth: float = 0) -> None:
        args = locals()
        args.pop('self')
        super().__init__(depth=depth)
        self.passed = locals()

    def __str__(self) -> str:
        output = self.PATTERN
        for key in self.ARGS:
            output = output.replace(f'_{key}_', f'{self.passed[key]}')
        return output

class SVG_Rect(SVG_Element):

    ARGS = ['x', 'y', 'width', 'height', 'fill']
    PATTERN = r'<rect x="_x_" y="_y_" width="_width_" height="_height_" fill="_fill_"/>'

    def __init__(self, x: float, y: float, width: float, height: float, *, fill: str = 'black', depth: float = 0) -> None:
        super().__init__(depth=depth)
        self.passed = locals()

    def __str__(self) -> str:
        output = self.PATTERN
        for key in self.ARGS:
            output = output.replace(f'_{key}_', f'{self.passed[key]}')
        return output

class SVG:

    def __init__(self, width: int = 500, heigth: int = 500, *, offset: tuple[float, float] = (0,0)) -> None:
        self.width = width
        self.heigth = heigth

        self.canvas: list[SVG_Element] = []

    def append(self, obj: SVG_Element): self.canvas.append(obj)

    def save(self, path):
        text = r'<svg xmlns="http://www.w3.org/2000/svg" width="_width_" height="_heigth_">_object_</svg>'
        text = text.replace('_width_', f'{self.width}').replace('_heigth_', f'{self.heigth}')
        
        content = ''.join([str(obj) for obj in self.canvas])

        text = text.replace('_object_', content)

        with open(path, 'w') as file:
            file.write(text)
