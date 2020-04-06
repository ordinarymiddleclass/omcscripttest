import markdown 
from lxml import etree
from pathlib import Path
import os 

current_path = Path(os.path.realpath(__file__))
root = current_path.parent.parent
newfilepath = root / "source"/ "gpdiary0006_20191004.md"


with open (newfilepath, "r", encoding ="utf-8") as fp:
    content = markdown.markdown(fp.read(), output_format = "xhtml")

parser = etree.HTMLParser(encoding="utf-8")

with open("test.html", "w", encoding ="utf-8") as fp:
    fp.write(content)

with open("test.html", "r", encoding ="utf-8") as fp:
    tree = etree.parse(fp, parser)

print (tree.child())