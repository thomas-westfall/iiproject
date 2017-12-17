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
            freq = len(value)
            x = 0
            tempfreq = 0
            ans = {}
            #ans['total'] = freq;

            for i in range(0, freq - 1):
                if value[i] not in ans:
                    tempfreq = 0
                    k = i
                    while True:
                        if value[i] == value[k]:
                            tempfreq = tempfreq + 1
                            k = k + 1
                        else:
                            break
                    ans[value[i]] = tempfreq
 
            return ans

def queryand(iindex, word, wordb):
    ans = {}
    temp = []
    
    if query(iindex, word) != {} and query(iindex, wordb) != {}:

        dicta = query(iindex, word)
        dictb = query(iindex, wordb)

        for key, value in dicta.items():
            temp = []
            if key in dictb:
                temp.append(value)
                temp.append(dictb[key])
                ans[key] = temp
        return ans
       
    return "One/both word(s) not found"

def querynot(iindex, word):
    val = buildvalues(iindex)
    
    if query(iindex, word) == {}:
        return val
    
    ans = []
    avoid = iindex[word]
    for x in val:
        if not x in avoid:
            ans.append(x)
    freq = len(ans)
    return removedupes(ans)


def queryor(iindex, word, wordb):
    if query(iindex, word) == {} and query(iindex, wordb) == {}:
        return "Neither word found"
    ans = {}
    dicta = query(iindex, word)
    dictb = query(iindex, wordb)

    for key, value in dicta.items():
        temp = []
        if not key in dictb:
            temp.append(value)
            temp.append(0)
            ans[key] = temp
        else:
            temp.append(value)
            temp.append(dictb[key])
            ans[key] = temp
    for key, value in dictb.items():
        temp = []
        if not key in dicta:
            temp.append(0)
            temp.append(value)
            ans[key] = temp
            
    return ans

sample_index = build_inverted_index('sample-texts.csv',0,1)
texas_index = build_inverted_index('offenders-clean.csv',0,8)
spam_index = build_inverted_index('spam.csv',0,1)
#print (texas_index)

print query(sample_index, 'do')
print query(sample_index, 'us')
#print queryand(sample_index, 'do', 'us')
#print querynot(sample_index, 'do')
print queryor(sample_index, 'do', 'us')
#print buildvalues(sample_index)

#print query(texas_index, 'sorry')
#print queryand(texas_index, 'God', 'sorry')
#print queryand(spam_index, 'Hello','hello')
#print query(spam_index, "Hello")
