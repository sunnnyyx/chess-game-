import pygame
import os

from sound import Sound
from color import Color
from theme import Theme

class Config:

    def __init__(self):
        self.themes = []
        self._add_themes()
        self.idx = 0
        self.theme = self.themes[self.idx]
        self.font = pygame.font.SysFont('monospace', 18, bold=True)
        self.move_sound = Sound(os.path.join('logos-and-songs/sounds/move.wav'))
        self.capture_sound = Sound(os.path.join('logos-and-songs/sounds/capture.wav'))

    def change_theme(self):
        self.idx = (self.idx + 1) % len(self.themes)
        self.theme = self.themes[self.idx]

    def _add_themes(self):
        green = Theme(
            bg_theme=Color((234, 235, 200), (119, 154, 88)),
            trace_theme=Color((244, 247, 116), (172, 195, 51)),
            moves_theme=Color((200, 100, 100), (160, 80, 80))
        )

        brown = Theme(
            bg_theme=Color((235, 209, 166), (165, 117, 80)),
            trace_theme=Color((245, 234, 100), (209, 185, 59)),
            moves_theme=Color((180, 70, 70), (140, 50, 50))
        )

        blue = Theme(
            bg_theme=Color((229, 228, 200), (60, 95, 135)),
            trace_theme=Color((123, 187, 227), (43, 119, 191)),
            moves_theme=Color((160, 100, 200), (110, 50, 150))
        )

        gray = Theme(
            bg_theme=Color((120, 119, 118), (86, 85, 84)),
            trace_theme=Color((99, 126, 143), (82, 102, 128)),
            moves_theme=Color((220, 220, 220), (170, 170, 170))
        )

        self.themes = [green, brown, blue, gray]
