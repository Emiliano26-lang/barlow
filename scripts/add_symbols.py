from fontTools.ttLib import TTFont
import sys

def add_symbols(font_path):
    font = TTFont(font_path)
    cmap = font["cmap"].tables[0].cmap
    cmap[0x2105] = "uni2105"
    cmap[0x2100] = "uni2100"
    font.save(font_path)
    print("Symbols added successfully.")

if __name__ == "__main__":
    add_symbols(sys.argv[1])
