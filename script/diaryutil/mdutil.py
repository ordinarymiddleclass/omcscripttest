GPHEADER =[ '[_metadata_:encoding]: - "utf-8"',
        '[_metadata_:fileformat]: - "markdown"',
        '[_metadata_:MIME_type]: - "text/plain"',
        '[_metadata_:markdown_version]: - "commonmark version 0.29"',
        '[_metadata_:markdown_spec]: - "https://spec.commonmark.org/0.29/"']

from convenientpath import convenientpath
from pathlib import Path 
from runpandoc import pandoc_html
from runpandoc import pandoc_txt
from runpandoc import pandoc_tex
from runpandoc import pandoc_tei
from runpandoc import pandoc_docbook

def add_encoding_header(s):
    return "\n".join(GPHEADER) + "\n\n" + s 

def _remove_encoding_header(li):
    while "metadata" in li[0]:
        li.pop(0)
    if li[0] == "\n":
        li.pop(0)

def _normalize_text_inner(li):
    _remove_encoding_header(li)
    if "===" in li[1]:
        li.pop(1)
    if "###### tags" in li[-1]:
        li.pop()
    title = li[0].split("_")
    newtitle_raw = title[2].strip("\n").strip(" #") 
    newtitle_list = [newtitle_raw[:4], newtitle_raw[4:6], newtitle_raw[6:]]
    newtitle = "/".join(newtitle_list)
    adjusted_title = "# " + title[0].strip("# ") + " " + newtitle + " #\n"
    li[0] = adjusted_title
    return "".join(li)

def normalize_text(fp):
    """
        只能使用在照規定寫完的蒼白球日誌
    """
    li = fp.readlines()
    return _normalize_text_inner(li)

def concatmd (li):
    """
        take a list of path of files, and concatenate them 
    """
    destlist = []
    for item in li:
        with item.open("r", encoding="utf-8") as f:
            destlist.append(normalize_text(f))
    return "\n\n".join(destlist)

def convertmonth(s):
    """
        Get a string like "201912" and convert the items in that month into unified md, html, txt and tex files 
    """
    dest = convenientpath.get_dest("md")
    dest_html = convenientpath.get_dest("html")
    dest_txt = convenientpath.get_dest("txt")
    dest_tex = convenientpath.get_dest("tex")
    dest_tei = convenientpath.get_dest("xml_tei")
    dest_docbook = convenientpath.get_dest("xml_docbook")
    destfile = dest / "gpdiary{}.md".format(s)
    destfile_html = dest_html / "gpdiary{}.html".format(s)
    destfile_txt = dest_txt / "gpdiary{}.txt".format(s)
    destfile_tex = dest_tex / "gpdiary{}.tex".format(s)
    destfile_tei = dest_tei / "gpdiary{}.xml".format(s)
    destfile_docbook = dest_docbook / "gpdiary{}.xml".format(s)
    source = convenientpath.get_source() / s
    li = []
    li += sorted(source.glob("*.md"))    
    newmd = add_encoding_header(concatmd(li))
    newmd.replace("---", "")
    with destfile.open("w", encoding="utf-8") as f:
        f.write(newmd)
    with destfile_html.open("w", encoding="utf-8") as f:
        f.write(pandoc_html(str(destfile)))
    with destfile_txt.open("w", encoding="utf-8") as f:
        f.write(pandoc_txt(str(destfile)))
    with destfile_tex.open("w", encoding="utf-8") as f:
        f.write(pandoc_tex(str(destfile)))
    with destfile_tei.open("w", encoding="utf-8") as f:
        f.write(pandoc_tei(str(destfile)))
    with destfile_docbook.open("w", encoding="utf-8") as f:
        f.write(pandoc_docbook(str(destfile)))


for item in ["201909", "201910", "201911", "201912", "202001", "202002", "202003"]:
    convertmonth(item)

"""
dest = convenientpath.get_dest("md")
dest_html = convenientpath.get_dest("html")
dest_txt = convenientpath.get_dest("txt")
dest_tex = convenientpath.get_dest("tex")
destfile = dest / "gpdiary2019autumn.md"
destfile_html = dest_html / "gpdiary2019autumn.html"
destfile_txt = dest_txt / "gpdiary2019autumn.txt"
destfile_tex = dest_tex / "gpdiary2019autumn.tex"

testlist = []
for item in ["201909", "201910", "201911"]:
    source = convenientpath.get_source() / item 
    testlist += sorted(source.glob("*.md"))
newmd = concatmd(testlist)
newmd.replace("---", "")
with destfile.open("w", encoding="utf-8") as f:
    f.write(newmd)
with destfile_html.open("w", encoding="utf-8") as f:
    f.write(pandoc_html(str(destfile)))
with destfile_txt.open("w", encoding="utf-8") as f:
    f.write(pandoc_txt(str(destfile)))
with destfile_tex.open("w", encoding="utf-8") as f:
    f.write(pandoc_tex(str(destfile)))

destfile = dest / "gpdiary2019winter.md"
destfile_html = dest_html / "gpdiary2019winter.html"
destfile_txt = dest_txt / "gpdiary2019winter.txt"
destfile_tex = dest_tex / "gpdiary2019winter.tex"

testlist = []
for item in ["201912", "202001", "202002"]:
    source = convenientpath.get_source() / item 
    testlist += sorted(source.glob("*.md"))
newmd = concatmd(testlist)
newmd.replace("---", "")
with destfile.open("w", encoding="utf-8") as f:
    f.write(newmd)
with destfile_html.open("w", encoding="utf-8") as f:
    f.write(pandoc_html(str(destfile)))
with destfile_txt.open("w", encoding="utf-8") as f:
    f.write(pandoc_txt(str(destfile)))
with destfile_tex.open("w", encoding="utf-8") as f:
    f.write(pandoc_tex(str(destfile)))

"""