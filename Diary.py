while True:
    text=str(input("Enter text: ")).split()
    words = []
    agains = False
    TPS={}
    for i in text:
        for z in words:
            if i == z:
                agains = True
        if agains == True:
            agains == False
            continue
        words.append(i)
        agains = False
    words.sort()
    print(words)

    text  = "".join(words)

    for char in set(text):
        count = text.count(char)
        print('{}-{}'.format(char, count))
