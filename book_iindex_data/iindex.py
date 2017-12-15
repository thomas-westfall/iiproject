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
    beginning_cut_pos = find_pos(data, False, "*** START OF THIS PROJECT GUTENBERG EBOOK")
    end_cut_pos = find_pos(data, True, "*** END OF THIS PROJECT GUTENBERG EBOOK")
    
    data = data[beginning_cut_pos+1: end_cut_pos]
    
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
    
    for filename in file_list:
        f = open(filename)
        data = []
        
        for line in f:
            line = line.rstrip("\n\r")
            data.append(line)
        f.close()
        
        freq_dict = {}
        
        #FREQUENCY
        data = clean_data(data)
        for item in data:
            for word in item.split(" "):
                word = clean_word(word)
                freq_dict.setdefault(word, 0)
                freq_dict[word] += 1
        
        #creating a master dict with key being filename
        book_dict = {}
        book_dict.setdefault(filename, freq_dict)
        
        #write out to data file
        o = open("book_iindex_data.txt", "a+")
        print("Writing data for: " + filename)
        o.write( str(book_dict) + "\n")
        o.close()
    
    print("Word frequency data compilation complete")
    
iindex()