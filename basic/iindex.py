import csv

def build_inverted_index(filename,keyindex,textindex):
    csv_reader =csv.reader(open(filename))
    d={}
    for line in csv_reader:
        document = line[keyindex]
        textstring = line[textindex]
        # cleantext = "".join([x if x.isalpha() else ' ' for x in s ])
        cleantext = ""
        for letter in textstring:
            if letter.isalpha():
                cleantext = cleantext + letter
            else:
                cleantext = cleantext + " "
        wordlist = cleantext.split()
        for word in wordlist:
            d.setdefault(word,[])
            d[word].append(document)
    return d



def buildvalues(iindex):
    ans = []
    for key, value in iindex.items():
        for x in value:
            if not x in ans:
                ans.append(x)
    return ans

def removedupes(l):
    ans = []
    for x in l:
        if x not in ans:
            ans.append(x)
    return ans

def query(iindex, word):
    for key, value in iindex.items():
        if key == word:
            freq = len(value)
            return removedupes(value)
    return ""

def queryand(iindex, word, wordb):
    ans = []
    
    if query(iindex, word) != "" and query(iindex, wordb) != "":
        wordone = iindex[word]
        wordtwo = iindex[wordb]

        for x in wordone:
            if x in wordtwo:
                ans.append(x)
        freq = len(ans)
        return removedupes(ans)
        
    return "One/both word(s) not found"

def querynot(iindex, word):
    val = buildvalues(iindex)
    
    if query(iindex, word) == "":
        return val
    
    ans = []
    avoid = iindex[word]
    for x in val:
        if not x in avoid:
            ans.append(x)
    freq = len(ans)
    return removedupes(ans)


def queryor(iindex, word, wordb):
    if query(iindex, word) == "" and query(iindex, wordb) == "":
        return "Neither word found"
    ans = []
    for x in iindex[word]:
        ans.append(x)
    for y in iindex[wordb]:
        if not y in ans:
            ans.append(y)
    freq = len(ans)
    return removedupes(ans)
        
sample_index = build_inverted_index('sample-texts.csv',0,1)
texas_index = build_inverted_index('offenders-clean.csv',0,8)
#print (sample_index)

#print query(sample_index, 'do')
#print query(sample_index, 'us')
#print queryand(sample_index, 'do', 'us')
#print querynot(sample_index, 'do')
#print queryor(sample_index, 'do', 'us')
#print buildvalues(sample_index)

print query(texas_index, 'Joanna')
print queryand(texas_index, 'God', 'sorry')
