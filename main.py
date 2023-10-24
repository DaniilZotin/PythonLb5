import re

def readFile(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            return text
    except Exception as e:
        return str(e)

def getFirstSentence(text):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    if sentences:
        firstSentence = sentences[0]
    else:
        firstSentence = None
    return firstSentence

def getAllWordsInFile(text):
    return re.findall(r'\w+', text)

def sortingWords(words):
    ukrainianWords = []
    englishWords = []
    for word in words:
        if any(char in word for char in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"):
            ukrainianWords.append(word)
    for word in words:
        if any(char in word for char in "abcdefghijklmnopqrstuvwxyz"):
            englishWords.append(word)


    sortedUkrainianWords = sorted(ukrainianWords, key=lambda word: word.lower())
    sortedEnglishWords = sorted(englishWords, key=lambda word: word.lower())

    return sortedUkrainianWords + sortedEnglishWords

if __name__ == "__main__":
    text = readFile("text.txt")

    if not text:
        print("Cannot read the file, it is empty, or another problem")
    else:
        print("First sentence: " + getFirstSentence(text))

        words = getAllWordsInFile(text)
        sortedResult = sortingWords(words)

        print("Sorted words: " + str(sortedResult))
        print("Quantity of words: " + str(len(words)))