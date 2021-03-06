# https://en.wikipedia.org/wiki/ANSI_escape_code
class ColorMeta(type):
    def __new__(mcls, name, bases, attrs):
        newattrs = {}
        for name, value in attrs.items():
            newattrs[name] = f'\033[{value}m'
        return super().__new__(mcls, name, bases, newattrs)


class Color(metaclass=ColorMeta):
    RESET = 0


class ForegroundColor(Color):
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    LIGHT_GRAY = 37
    GRAY = 90
    LIGHT_RED = 91
    LIGHT_GREEN = 92
    LIGHT_YELLOW = 93
    LIGHT_BLUE = 94
    LIGHT_MAGENTA = 95
    LIGHT_CYAN = 96
    WHITE = 97


class BackgroundColor(Color):
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    LIGHT_GRAY = 47
    GRAY = 100
    LIGHT_RED = 101
    LIGHT_GREEN = 102
    LIGHT_YELLOW = 103
    LIGHT_BLUE = 104
    LIGHT_MAGENTA = 105
    LIGHT_CYAN = 106
    WHITE = 107


class StyleColor(Color):
    BOLD = 1
    DIM = 2
    ITALIC = 3
    UNDERLINE = 4


Fore = ForegroundColor()
Back = BackgroundColor()
Style = StyleColor()
