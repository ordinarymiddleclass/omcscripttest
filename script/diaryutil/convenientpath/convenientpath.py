from pathlib import Path 

def get_source():
    parent = Path(__file__).parent.parent.parent.parent 
    return parent / "source"

def get_dest(dest_name):
    parent = Path(__file__).parent.parent.parent.parent  
    dest = parent / "export" / dest_name
    if not dest.is_dir():
        dest.mkdir()
    else:
        return dest

if __name__ == "__main__":
    print(Path.cwd())
    
    dest = get_dest("html")
    source = get_source()

    for item in source.glob("*.md"):
        newname = item.name.split(".")[0] + ".html"
        newfile = dest / newname
