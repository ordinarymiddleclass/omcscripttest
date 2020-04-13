from convenientpath import convenientpath
from pathlib import Path 
import mdutil

def create_test_files():
    source = convenientpath.get_source() / "202003"
    dest = convenientpath.get_dest("test")
    li = source.glob("*.md")
    for item in li:
        newname = "test" + str(item).split("\\")[-1]
        with open(item, "r", encoding="utf-8") as f:
            s = mdutil.add_encoding_header(f.read())
        with open (str(dest/newname), "w", encoding = "utf-8") as f:
            f.write(s)

def test_normalize_text():
    create_test_files()
    testdir = convenientpath.get_dest("test")
    testfiles = testdir.glob("*.md")
    for item in testfiles:
        with open(item, "r", encoding="utf-8") as f:
            print(mdutil.normalize_text(f))

mdutil.convertmonth("test")