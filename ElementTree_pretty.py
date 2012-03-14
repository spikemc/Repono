"""
From Doug Hellmann's PyMOTW tutorials:
http://www.doughellmann.com/PyMOTW/xml/etree/ElementTree/create.html
"""

from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
	"""Returns a pretty print XML string for the Element."""
	rough_string = ElementTree.tostring(elem, 'utf-8')
	reparsed = minidom.parseString(rough_string)
	return reparsed.toprettyxml(indent="  ")

	
