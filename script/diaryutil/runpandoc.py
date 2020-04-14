import subprocess 

def pandoc_html(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "html", "-M", "title=gpdiary", filename], encoding="utf-8")

def pandoc_txt(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "plain", filename], encoding="utf-8")

def pandoc_tex(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "latex", filename], encoding="utf-8")

def pandoc_tei(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "tei", filename], encoding="utf-8")
def pandoc_docbook(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "docbook", filename], encoding="utf-8")
