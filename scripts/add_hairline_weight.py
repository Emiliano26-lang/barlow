# scripts/add_hairline_weight.py
from fontTools.ttLib import TTFont
import sys

def add_hairline(input_font, output_font):
    font = TTFont(input_font)
    # TODO: implement weight adjustment logic
    font.save(output_font)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: add_hairline_weight.py input.ttf output.ttf")
        sys.exit(1)
    add_hairline(sys.argv[1], sys.argv[2])
