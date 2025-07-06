from color import Color

class Theme:
    def __init__(self, bg_theme, trace_theme, moves_theme):
        self.bg = bg_theme
        self.trace = trace_theme
        self.moves = moves_theme

# 🟫 Classic Theme Example
classic_theme = Theme(
    bg_theme=Color.classic(),
    trace_theme=Color((255, 255, 0), (200, 200, 0)),    # Yellow traces
    moves_theme=Color((0, 255, 0), (0, 200, 0))         # Green move indicators
)

# 🌈 Neon Theme Example
neon_theme = Theme(
    bg_theme=Color.neon(),
    trace_theme=Color((255, 105, 180), (255, 20, 147)), # Pink trace
    moves_theme=Color((0, 255, 255), (0, 200, 200))     # Aqua moves
)

# 🖤 Dark Mode Theme
dark_mode_theme = Theme(
    bg_theme=Color.dark_mode(),
    trace_theme=Color((150, 150, 150), (100, 100, 100)),
    moves_theme=Color((200, 100, 255), (150, 50, 200))
)

# 🎲 Random Theme Generator
def random_theme():
    return Theme(
        bg_theme=Color.random_theme(),
        trace_theme=Color.random_theme(),
        moves_theme=Color.random_theme()
    )
