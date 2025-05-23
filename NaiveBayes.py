import English

""" Naive Bayes """

def cleanupText(text):
    # Go through all text and eliminate things like punctuation? 
    for letter in text:
        if letter == ".":
            letter = ""

def processText(textname):
    # DBC principles
    txt = str(textname)
    with open(txt, "r", encoding="utf-8") as f:
        txt = f.read()

    # Join all text into a single string to get bigrams
    fullText = "".join(txt)

    # Clean up text as you go
    fullText = cleanupText( fullText )

    return fullText

processedText = processText("EmailDataset.txt")

# Notes:
