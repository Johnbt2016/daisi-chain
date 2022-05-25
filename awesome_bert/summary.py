def get_summary(context, query):
    with open("DAISI.md", "r") as f:
        text = f.read()
    
    return text