import random

class Color:
    def __init__(self, light, dark, highlight=None, border=None):
        self.light = light
        self.dark = dark
        self.highlight = highlight or (255, 255, 0)  # Default: Yellow highlight
        self.border = border or (0, 0, 0)            # Default: Black border

    @staticmethod
    def classic():
        return Color(
            light=(240, 217, 181),   # Beige
            dark=(181, 136, 99),     # Brown
            highlight=(255, 255, 0),
            border=(0, 0, 0)
        )

    @staticmethod
    def neon():
        return Color(
            light=(0, 255, 200),     # Cyan
            dark=(50, 0, 100),       # Purple
            highlight=(255, 20, 147),# Pink
            border=(0, 255, 0)       # Green
        )

    @staticmethod
    def dark_mode():
        return Color(
            light=(60, 60, 60),      # Gray
            dark=(30, 30, 30),       # Darker Gray
            highlight=(255, 255, 255),
            border=(100, 100, 100)
        )

    @staticmethod
    def random_theme():
        def rand_color():
            return tuple(random.randint(0, 255) for _ in range(3))
        return Color(
            light=rand_color(),
            dark=rand_color(),
            highlight=rand_color(),
            border=rand_color()
        )
