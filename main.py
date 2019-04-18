import regex as re


def record_sentence(sentence, papers_read):
    if sentence in papers_read.keys():
        papers_read[sentence] = papers_read[sentence]+1
    else:
        papers_read[sentence] = 1

def read_paper(paper, papers_read):
    p = re.split("([.!?;]*[.!?;])", paper)
    for x in range(0, len(p)-1, 2):
        record_sentence((p[x] + p[x+1]).strip(), papers_read)

if __name__ == "__main__":
    papers_read = dict()
    paper0 = "!Hello, there?! How's it going? I see you're typing now."
    paper1 = ("In order to foster a convivial atmosphere, no computer work"
              "is allowed in the cafe.")
    paper2 = "I see you're typing now. I type, too."
    read_paper(paper0, papers_read)
    read_paper(paper1, papers_read)
    read_paper(paper2, papers_read)
    print(papers_read)


