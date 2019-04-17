import regex as re

def read_paper(paper):
    p = re.split("([.!?;]*[.!?;])", paper)
    ps = []
    for x in range(0, len(p)-1, 2):
        ps.append((p[x] + p[x+1]).strip())
    return ps

if __name__ == "__main__":
    print(read_paper("!Hello, there?! How's it going? I see you're typing now."))

