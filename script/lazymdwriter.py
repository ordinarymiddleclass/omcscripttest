UNORDERED = 0
ORDERED = 1
COMMENT = 2

def lazy_header (s, header_level = 2):
    '''
        Transform an arbitrary text to ATX-flavored heading.
    '''
    header_str = "#"*header_level
    if header_level < 1:
        raise ValueError("Invalid header level")
    elif header_level == 1:
        return "# " + s + " #\n"
    else:
        return "\n" + header_str + " " + s + " " \
            + header_str + "\n"

def lazy_ul (s):
    return "\n* " + s 

def lazy_ol(s, n):
    return "\n{}. {}\n\n    ".format(n, s)

def lazy_comment(s, n):
    return "\n[{}] {}\n\n".format(n, s)

class convenient_list():

    def __init__(self, title = ""):
        self.title = title
        self.content = []
        self.output = ""

    def add_ul(self, s):
        self.content.append((s, UNORDERED))

    def add_ol(self, s, n=1):
        self.content.append((s, ORDERED, n))

    def add_comment(self, s, n=1):
        self.content.append((s, COMMENT, n))
    
    def compile(self):
        self.output += lazy_header(self.title)
        for item in self.content:
            if item[1] == UNORDERED:
                self.output += lazy_ul(item[0])
            elif item[1] == ORDERED:
                self.output += lazy_ol(item[0], item[2])
            elif item[1] == COMMENT:
                self.output += lazy_comment(item[0], item[2])
        self.output += "\n"
        return self.output