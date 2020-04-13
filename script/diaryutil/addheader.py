from convenientpath import convenientpath
from pathlib import Path 
import mdutil 

def add_month_header(s):
    source = convenientpath.get_source() / s
    li = sorted(source.glob("*.md"))    
    for item in li:
        with item.open("r", encoding="utf-8") as f:
            newstr = mdutil.add_encoding_header (f.read())
        with item.open("w", encoding="utf-8") as f:
            f.write(newstr)

add_month_header("202004")