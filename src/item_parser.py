import xml.etree.ElementTree as ET
from .items.guns import SmallGun

def parse_items():
    tree = ET.parse('configs/Items.xml')
    root = tree.getroot()
    weapons = root.find('weapons')
    small_guns = weapons.find('small-guns')
    forty_four = small_guns.find('gun')

    gun = SmallGun(forty_four)
