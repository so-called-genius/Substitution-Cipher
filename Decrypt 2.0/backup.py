import pprint

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mykey=[]

def main():
    englishdic = open("English word.txt", 'r')
    patternaggregationfordic = {}
    for line in englishdic:
        line = line.strip()
        words = line.split()
        for word in words:
            t=True
            for l in word:
                if ord(l) < 65 or ord(l) > 90:
                    t = False
            if not t:
                continue
            p = getpattern(word)
            if p not in patternaggregationfordic:
                patternaggregationfordic[p] = []
            patternaggregationfordic[p].append(word)

    blankmapping = {}
    wordic = []
    for i in range(26):
        blankmapping[chr(i + 65)] = {}
    print(blankmapping)
    filename = input("Enter name of input file: ")
    inputFile = open(filename, "r")
    for line in inputFile:
        line = line.strip()
        words = line.split()
        for word in words:
            word = word.upper()
            t = True
            for l in word:
                if ord(l) < 65 or ord(l) > 90:
                    t = False
            if getpattern(word) not in patternaggregationfordic:
                t = False
            if not t:
                continue
            if word not in wordic:
                wordic.append(word)
    for word in wordic:
        for l in range(len(word)):
            tem = []
            for p in patternaggregationfordic[getpattern(word)]:
                if p[l] not in tem:
                    tem.append(p[l])
            for m in tem:
                if m not in blankmapping[word[l]]:
                    blankmapping[word[l]][m] = 1
                else:
                    blankmapping[word[l]][m] += 1

    for l in blankmapping:
        t = ''
        temp = 0
        for le in blankmapping[l]:
            if blankmapping[l][le] > temp:
                temp = blankmapping[l][le]
                t = le
        blankmapping[l] = t
    pprint.pprint(blankmapping)
    letternotfound=[]
    for l in LETTERS:
        indicate=False
        for le in blankmapping:
            if blankmapping[le]==l:
                mykey.append(le)
                indicate=True
                break
        if not indicate:
            mykey.append('0')
            letternotfound.append(l)
    for k in range(len(mykey)):
        if mykey[k]=='0':
            mykey[k]=letternotfound[0]
            letternotfound.pop(0)
    key=''.join(mykey)
    print(LETTERS,key)



def getpattern(word):
    pattern = []
    passed = {}
    index = 0
    for l in word:
        if l not in passed:
            passed[l] = str(index)
            index = index + 1
        pattern.append(passed[l])
    return "".join(pattern)


if __name__ == '__main__':
    main()
