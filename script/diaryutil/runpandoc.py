import subprocess 

def pandoc_html(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "html", filename], encoding="utf-8")

def pandoc_txt(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "plain", filename], encoding="utf-8")

def pandoc_tex(filename):
    return subprocess.check_output(["pandoc", "-s", "-t", "latex", filename], encoding="utf-8")
