while True:
    text = str(input("Enter text: ")).split(' ')
    words = []
    agains = False
    for i in text:
        for z in words:
            if i == z:
                agains = True

        if agains == True:
            agains = False
            continue
        words.append(i)
        agains = False
        
    words.sort()
    print(words)

    word_let  = "".join(words)

    for char in set(word_let):
        count = word_let.count(char)
        print('{} = {}'.format(char, count),end=';  ')
    print()
