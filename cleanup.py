#!/usr/bin/fontforge
import os
import xml.etree.ElementTree as ET
ET.register_namespace('', 'http://www.w3.org/2000/svg')

attributes_to_remove = ['class', 'id', 'data-name']

def find_svg_files(directory):
	svg_files = []
	for root, dirs, files in os.walk(directory):
		for file in files:
			if file.endswith('.svg'):
				svg_files.append(os.path.join(root, file))
	return svg_files

def remove_unnecessary_elements(svg_file):
	tree = ET.parse(svg_file)
	root = tree.getroot()

	for defs in root.findall('.//{http://www.w3.org/2000/svg}defs'):
		root.remove(defs)

	for defs in root.findall('.//{http://www.w3.org/2000/svg}title'):
		root.remove(defs)

	for elem in root.iter():
		for attr in attributes_to_remove:
			if attr in elem.attrib:
				del elem.attrib[attr]

	tree.write(svg_file)

def main(directory):
	for type in ("regular", "bold"):
		svg_files = find_svg_files(directory + "-" + type)
		for svg_file in svg_files:
			remove_unnecessary_elements(svg_file)

if __name__ == "__main__":
	main("svg")
