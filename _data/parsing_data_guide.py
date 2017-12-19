import ast

f = open("book_freq_data.txt")
for line in f:
    
    #THERE IS ONLY ONE LINE IN THE DATA!!
    #YOU CAN'T DO str(f) b/c thats still the iowrapper bs
    
    #1. Change data into string:
    s=str(line)
    
    #2. Change string into dict (since it's already in dict format):
    dict = ast.literal_eval(s)
    
    #3. Parsing through the data:
    #for key in dict --> key = book name, dict[key] = corresponding data; imbedded dictionary
    for key in dict:
        dict2 = dict[key]
        if (".txt" in key):
            print(key)
        #for word in dict2 --> word = word, dict2[word] = frequency of word
        for word in dict2:
            frequency = dict2[word]
            #print(word, frequency)
f.close()