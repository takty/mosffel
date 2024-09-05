#!/usr/bin/fontforge
import fontforge
import os

fn = "Mosffel"

def make_font(type):
	font = fontforge.font()

	if type == "regular":
		font.fontname     = fn + "-Regular"
		font.fullname     = fn + " Regular"
		font.weight       = "Regular"
		font.os2_stylemap = 0x0040
		font.os2_panose   = (2, 0, 5, 9, 0, 0, 0, 0, 0, 0)
	elif type == "bold":
		font.fontname     = fn + "-Bold"
		font.fullname     = fn + " Bold"
		font.weight       = "Bold"
		font.os2_stylemap = 0x0020
		font.os2_panose   = (2, 0, 8, 9, 0, 0, 0, 0, 0, 0)

	font.familyname = fn
	font.version    = "001.000"
	font.copyright  = "Copyright (c) 2024, Takuto Yanagida"
	font.encoding   = "ISO8859-1"
	font.ascent     = 800
	font.descent    = 200
	font.upos       = -100
	font.uwidth     = 50

	font.hhea_ascent      = 800
	font.hhea_ascent_add  = 0
	font.hhea_descent     = -200
	font.hhea_descent_add = 0
	font.hhea_linegap     = 350
	font.vhea_linegap     = 0

	font.os2_vendor          = ""
	font.os2_capheight       = 790
	font.os2_typoascent      = 800
	font.os2_typoascent_add  = 0
	font.os2_typodescent     = -200
	font.os2_typodescent_add = 0
	font.os2_typolinegap     = 350
	font.os2_winascent       = 1000
	font.os2_winascent_add   = 0
	font.os2_windescent      = 250
	font.os2_windescent_add  = 0
	font.os2_xheight         = 580
	font.os2_codepages       = (1, 0)
	font.os2_unicoderanges   = (3, 0, 0, 0)

	return font

def find_svg_files(directory):
	svg_files = []
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.svg'):
				svg_files.append(os.path.join(root, file))
	return svg_files

def make_glyph(font, svg_file):
	num = os.path.basename(svg_file).split(' ', 1)[0]
	code = int(num) + 31

	glyph = font.createChar(code)
	glyph.importOutlines(svg_file)

	glyph.width = 620

	glyph.correctDirection()
	glyph.simplify()
	glyph.round()
	glyph.autoHint()

def main(directory, output_file):
	fn = os.path.splitext(output_file)[0]
	ext = os.path.splitext(output_file)[1]

	for type in ("regular", "bold"):
		font = make_font(type)

		svg_files = find_svg_files(directory + "-" + type)
		for svg_file in svg_files:
			make_glyph(font, svg_file)

		font.generate(fn + "-" + type + ext, flags=("opentype"))

if __name__ == "__main__":
	main("svg", "mosffel.otf")
