
def cleanword(word):
    word_clean = ''
    for i in word:
        if i > 'A' and i < 'z':
            word_clean = word_clean + i
    return word_clean


def has_dashdash(text):
    if text.count('--') > 0:
        return True
    return False

def extract_words(text):
    while has_dashdash(text):
        index = text.index('--')
        if index < len(text)-2:
            text = text[0:index] + ' ' + text[index+2:]
    words = text.split()
    for i in range(0, len(words)):
        words[i] = cleanword(words[i].lower())
    return words 

def wordcount(word, words):
    cont = 0
    for i in words:
        if i == word:
            cont = cont + 1
    return cont

def wordset(words):
    unique_words = []
    for word in words:
        if unique_words.count(word) == 0:
            unique_words.append(word)
    return sorted(unique_words)          

def longestword(words):
    biggest = 0
    for word in words:
        if len(word) > biggest:
            biggest = len(word)
    return biggest

def test(expression):
    print(expression)


test(cleanword("what?") == "what")
test(cleanword("'now!'") == "now")
test(cleanword("?+='w-o-r-d!,@$()'") == "word")

test(has_dashdash("distance--but"))
test(not has_dashdash("several"))
test(has_dashdash("spoke--"))
test(has_dashdash("distance--but"))
test(not has_dashdash("-yo-yo-"))

test(extract_words("Now is the time! 'Now', is the time? Yes, now.") == ['now','is','the','time','now','is','the','time','yes','now'])
test(extract_words("she tried to curtsey as she spoke--fancy") ==['she','tried','to','curtsey','as','she','spoke','fancy'])

test(wordcount("now",  ["now","is","time","is","now","is","is"]) == 2)
test(wordcount("is", ["now","is","time","is","now","the","is"]) == 3)
test(wordcount("time", ["now","is","time","is","now","is","is"]) == 1)
test(wordcount("frog", ["now","is","time","is","now","is","is"]) == 0)

test(wordset(["now", "is", "time", "is", "now", "is", "is"]) ==  ["is", "now", "time"])
test(wordset(["I", "a", "a", "is", "a", "is", "I", "am"]) == ["I", "a", "am", "is"])
test(wordset(["or", "a", "am", "is", "are", "be", "but", "am"]) ==  ["a", "am", "are", "be", "but", "is", "or"])

test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)