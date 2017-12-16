import glob

def clean_word(w):
    '''
    input: "word" from a text with puncutation, etc
    output: "clean" word in lowercase and without punctuation
    '''
    all_letters=""
    for l in w:
        if l.isalpha() or l == "'":
            l = l.lower()
            all_letters += l
    return all_letters

def find_pos(list, reverse, s):
    if (not reverse):
        for i in range(len(list)):
            if s in list[i]:
                return i
    elif (reverse):
        for i in range(len(list)):
            if s in list[len(list)-1-i]:
                return len(list)-1-i

def clean_data(data):
    #positions to cut out all the gutenberg fine text
    try:
        beginning_cut_pos = find_pos(data, False, "PROJECT GUTENBERG EBOOK")
        end_cut_pos = find_pos(data, True, "PROJECT GUTENBERG EBOOK")
        
        data = data[beginning_cut_pos+1: end_cut_pos]
    except:
        print("Bypassing cutting of gutenberg fine text")
    
    for item in data:
        item = item.lower()
        if (item == ''):
            data.remove(item)
    
    #if - -> replace with space
    #make all data lowercase
    #
    return data

def iindex():
    #list of all .txt files within the folder
    file_list = glob.glob("*.txt")
    
    iindex_dict = {}
    
    for filename in file_list:
        if filename == "book_iindex_data.txt":
            print("Not processing book_iindex_data")
        else:
            print("Processing " + filename + "...")
            f = open(filename)
            data = []
            for line in f:
                line = line.rstrip("\n\r")
                data.append(line)
            f.close()
            
            #INVERTED INDEX
            data = clean_data(data)
            for item in data:
                for word in item.split(" "):
                    word = clean_word(word)
                    #Add word to dictionary; key = word, value = list of books
                    iindex_dict.setdefault(word, [])
                    iindex_dict[word].append(filename)
            
            print("Completed " + filename + ".")
    
    #write dictionary data out to file
    o = open("book_iindex_data.txt", "a+")
    o.write( str(iindex_dict) )
    o.close()
    
    print("Word iindex data compilation complete")
    
iindex()