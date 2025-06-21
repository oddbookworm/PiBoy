from src.item_parser import parse_items

parse_items()

from lxml import etree

xmlschema_doc = etree.parse("configs/Items.xsd")
xmlschema = etree.XMLSchema(xmlschema_doc)
doc = etree.parse("configs/Items.xml")
if not xmlschema.validate(doc):
    print(xmlschema.error_log)
