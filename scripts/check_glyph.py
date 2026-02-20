import sys
from fontTools.ttLib import TTFont

glyph_code = sys.argv[1]
files = sys.argv[2:]

for f in files:
    font = TTFont(f)
    cmap = font['cmap'].getBestCmap()
    if int(glyph_code[2:], 16) in cmap:
        print(f"✅ Glyph {glyph_code} found in {f}")
    else:
        print(f"❌ Glyph {glyph_code} missing in {f}")
        sys.exit(1)
