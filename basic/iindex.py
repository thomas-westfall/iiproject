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

def query(iindex, word):
    for key, value in iindex.items():
        if key == word:
            return value
    return ""

def queryand(iindex, word, wordb):
    ans = []
    
    if query(iindex, word) != "" and query(iindex, wordb) != "":
        wordone = iindex[word]
        wordtwo = iindex[wordb]

        for x in wordone:
            if x in wordtwo:
                ans.append(x)
        return ans
        
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
    return ans


#def queryor(iindex, word, wordb):
    
sample_index = build_inverted_index('sample-texts.csv',0,1)
texas_index = build_inverted_index('offenders-clean.csv',0,8)
#print (sample_index)

#print queryand(texas_index, 'God', 'sorry')
print query(sample_index, 'do')
print queryand(sample_index, 'do', 'us')
print querynot(sample_index, 'do')
#print buildvalues(sample_index)
