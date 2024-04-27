

def replace_chars(str):
    unsupchar = ["*", '"', "/", "\\", "<", ">", ":", "|", "?","\t",'..']
    for char in unsupchar:
        str = str.replace(char, " ")
    str = str.replace("  ", " ")
    if str[-1] == ".":
        str = str.replace('.','')
    return str.strip()