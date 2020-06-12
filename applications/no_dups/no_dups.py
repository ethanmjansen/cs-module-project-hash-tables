def no_dups(s):
    # Your code here
    cache = {}
    text = ""
    words = s.split()

    for word in words:
        word = word.lower()
        if word in cache:
            cache[word] += 1
        else:
            cache[word] = 1

    for i in list(cache):
        text += i + " "

    return text.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))