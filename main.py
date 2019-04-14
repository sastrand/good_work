import regex as re

def read_paper(paper):
    p = re.split("[.!?;]+", paper)
    return p

if __name__ == "__main__":
    print(read_paper("Hello, there! How's it going? I see you're typing now."))

