import ast
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

nonfiction = ['actor', 'actors', 'actress', 'actresses', 'comedy', 'comedian', 'comedians', 'punk rock', 'punk rocker', 'rap', 'rapper', 'hip-hop', 'hip hop', 'film director', 'cinema director', 'movie director', 'motion picture director', 'africa', 'african', 'asia', 'asian', 'canada', 'canadian', 'france', 'french', 'europe', 'european', 'germany', 'german', 'greece', 'greek', 'ireland', 'irish', 'celtic', 'italy', 'italian', 'rome', 'roman', 'russia', 'russian', 'spain', 'spanish', 'portugal', 'portuguese', 'latin america', 'latin american', 'mexico', 'mexican', 'south america', 'south american', 'middle east', 'middle eastern', 'egypt', 'egyptian', 'iran', 'iranian', 'iraq', 'iraqi', 'israel', 'israeli', 'palestine', 'palestinian', 'syria', 'syrian', 'turkey', 'ottoman', 'afghan war', 'iraq war', 'civil war', 'american revolution', 'american revolution war', 'air force', 'army', 'marine', 'marines', 'navy', 'cold war', 'vietnam war', 'world war 1', 'world war I', 'WW1', 'world war 2', 'world war II', 'WW2', 'united kingdom prime minister', 'UK prime minister', 'U.K. prime minister', 'british prime minister', 'great britain prime minister', 'united states president', 'US president', 'U.S. president', 'american president', 'buddhist', 'buddhism', 'atholic', 'catholicism', 'christian', 'christianity', 'hindu', 'hinduism', 'islam', 'islamic', 'islamist', 'judaism', 'baseball', 'basketball', 'box', 'boxing', 'football', 'american football', 'golf', 'hockey', 'motor sport', 'f1', 'formula 1', 'formula one', 'nascar', 'grand prix', 'rugby', 'soccer', 'classic composer', 'classic music', 'classical composer', 'classical music', 'country music', 'country band', 'country artist', 'folk music', 'folk singer', 'folk artist', 'folk band', 'jazz band', 'jazz artist', 'jazz music', 'pop music', 'pop artist', 'pop band', 'pop singer', 'r&b', 'r & b', 'rhythm & blues', 'rock & roll', 'rock music', 'rock band', 'rock genre', 'dancer', 'dancing', 'ballet', 'choreography', 'choreographer', 'holocaust', 'american civil war', 'american revolution war', 'british', 'scotland', 'scottish', 'north ireland', 'wales', 'welsh', 'united kingdom', 'united states', 'US president', 'U.S. president', 'america president', 'british royalty', 'british monarchy', 'british king', 'british queen', 'british prince', 'british princess', 'british duchess', 'england royalty', 'england monarchy', 'england king', 'england queen', 'england prince', 'england princess', 'england duchess', 'english royalty', 'english monarchy', 'english king', 'english queen', 'english prince', 'english princess', 'english', 'duchess', 'astronaut', 'apollo', 'nasa', 'british', 'scotland', 'scottish', 'north ireland', 'wales', 'welsh', 'united states football', 'america football', 'american football', 'soccer', 'football', 'motor sport', 'motor sports', 'f1', 'formula one', 'formula 1', 'nascar', 'grand prix']

fantasyscience = ['angels', 'demons', 'dragons', 'elf', 'fae', 'fairies', 'ghost', 'spirit', 'deities', 'god', 'pantheon', 'psychic', 'telepathic', 'vampire', 'shapeshifter', 'witch', 'wizard', 'warlock', 'druid', 'shaman', 'artificial intelligence', 'aliens', 'clones', 'corporations', 'mutants', 'pirates', 'privateer', 'corsair', 'psychics', 'robots', 'androids', 'superhero', 'invasion', 'colonization', 'cyberpunk', 'contact', 'empire', 'republic', 'genes', 'metaphysical', 'visionary', 'theology', 'spiritual', 'fleet', 'starship', 'troop', 'armor', 'marine', 'soldier', 'exploration']

thriller= ['amateur', 'british detective', 'fbi', 'female police', 'private investigator', 'heist', 'robbery', 'thief', 'theft', 'murder', 'noir', 'mob', 'mafia', 'organized crime', 'yakuza', 'serial killer', 'vigilante justice', 'dark', 'disturbing', 'scary', 'vengeful', 'small town', 'island', 'beach', 'space', 'mountain', 'suburban', 'urban', 'paranormal', 'psychic', 'telepath', 'vampire', 'werewolf', 'shapeshifter', 'assassin', 'hitman', 'conspiracy', 'financial', 'pulp', 'terrorism']

literaturefiction = ['ancient', 'medieval', 'renaissance', '16th century', '17th century', '18th century', '19th century', '20th century', '21st century', 'aging', 'aged', 'childhood', 'youth', 'coming of age', 'death', 'loss', 'grief', 'depression', 'mental illness', 'alcohol abuse', 'drug abuse', 'family life', 'friendship', 'immigration', 'immigrant', 'love', 'marriage', 'politics', 'politician', 'religion', 'religious', 'spiritual', 'travel', 'voyage', 'military', 'war', 'school', 'college', 'university', 'career', 'workplace', 'working', 'office', 'divorce', 'marriage', 'parenting', 'parent and children', 'dating', 'relationship', 'singlehood', 'single women', 'sister', 'wedding']
['angels', 'demons', 'dragons', 'elf', 'fae', 'fairies', 'ghost', 'spirit', 'deities', 'god', 'pantheon', 'psychic', 'telepathic', 'vampire', 'shapeshifter', 'witch', 'wizard', 'warlock', 'druid', 'shaman', 'artificial intelligence', 'aliens', 'clones', 'corporations', 'mutants', 'pirates', 'privateer', 'corsair', 'psychics', 'robots', 'androids', 'superhero', 'invasion', 'colonization', 'cyberpunk', 'contact', 'empire', 'republic', 'genes', 'metaphysical', 'visionary', 'theology', 'spiritual', 'fleet', 'starship', 'troop', 'armor', 'marine', 'soldier', 'exploration']


f = open("_data/book_freq_data.txt")
for line in f:
    
    #THERE IS ONLY ONE LINE IN THE DATA!!
    #YOU CAN'T DO str(f) b/c thats still the iowrapper bs
    
    #1. Change data into string:
    s=str(line)
    
    #2. Change string into dict (since it's already in dict format):
    dict = ast.literal_eval(s)
    
    #3. Parsing through the data:
    #for key in dict --> key = book name, dict[key] = corresponding data; imbedded dictionary

    main = {}

    for bookname, freqs in dict.items():
        templist = []
        nonfictiontemp = 0
        fantasysciencetemp = 0
        thrillertemp = 0
        literaturefictiontemp = 0
        
        for word, freq in freqs.items():
            if word in nonfiction:
                nonfictiontemp = nonfictiontemp + freq
            if word in fantasyscience:
                fantasysciencetemp = fantasysciencetemp + freq
            if word in thriller:
                thrillertemp = thrillertemp + freq
            if word in literaturefiction:
                literaturefictiontemp = literaturefictiontemp + freq

        templist.append(nonfictiontemp)
        templist.append(fantasysciencetemp)
        templist.append(thrillertemp)
        templist.append(literaturefictiontemp)

        main[bookname] = templist #list order: nonfic,fantasysci,thrill,lit

    nonfictionsorted = sorted(main.items(),key=lambda x: x[1][0])
    fantasysciencesorted = sorted(main.items(),key=lambda x: x[1][1])
    thrillersorted = sorted(main.items(),key=lambda x: x[1][2])
    literaturefictionsorted = sorted(main.items(),key=lambda x: x[1][3])

    nonfictionsorted.reverse()
    fantasysciencesorted.reverse()
    thrillersorted.reverse()
    literaturefictionsorted.reverse()
    
    topnonfiction = []
    topfantasyscience = []
    topthriller = []
    topliteraturefiction = []

    numbooks = 10 #number of books shown on results page
    
    for x in range(0, numbooks):
        topnonfiction.append(nonfictionsorted[x][0])
        topfantasyscience.append(fantasysciencesorted[x][0])
        topthriller.append(thrillersorted[x][0])
        topliteraturefiction.append(literaturefictionsorted[x][0])

def gettop(genre):
    if genre == "nonfiction":
        return topnonfiction
    if genre == "fantasyscifi":
        return topfantasyscience
    if genre == "thriller":
        return topthriller
    if genre == "fiction":
        return topliteraturefiction

f.close()
