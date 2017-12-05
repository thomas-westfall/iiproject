from bs4 import BeautifulSoup
import requests,re

def download_top_100():
    '''This script will download Top 100 books of last 30 days from Project 
    Gutenberg and saves them with appropriate file name'''
    
    #Getting response from Project gutenberg's top list webpage
    base_url = 'http://www.gutenberg.org/files'
    r = requests.get('http://www.gutenberg.org/browse/scores/top')
    soup = BeautifulSoup(r.text, "html.parser")
    
    #Retrieving urls for list of top books in last30 days category
    h_tag = soup.find(id='books-last30')
    ol_tag = h_tag.next_sibling.next_sibling
    
    #Accessing and iterating through each book's data
    for a_tag in ol_tag.find_all('a'):
        #Finding main url of book
        m = re.match(r'(.*)(\(\d+\))', a_tag.text)
        book_name = m.group(1).strip()
        m = re.match(r'/ebooks/(\d+)', a_tag.get('href'))
        book_id = m.group(1)
        book_main_url = base_url + '/' + book_id
        
        #Accessing and retrieving data from book's url
        r2 = requests.get(book_main_url)
        soup2 = BeautifulSoup(r2.text, "html.parser")
        
        #Retrieving urls used to download book's txt files
        inner_a_tag = soup2.find_all('a')
        
        #==========RETRIEVING BOOK'S TXT URL==========
        txt_urls_list = []
        for item in inner_a_tag:
            href_content = item.get('href')
            if ".txt" in href_content:
                flag = True
                temp_url= item.get('href')
                txt_urls_list.append( str(temp_url) )
        
        try:
            #If multiple txt files, use first one
            #This also acts as a flag to check a txt file exists
            book_txt_filename = txt_urls_list[0]
            #Retrieving book data
            book_url = base_url + '/' + book_id + '/' + book_txt_filename
            book = requests.get(book_url)
            
            #Generating book's .txt file with its book name and retrieved data
            filename = book_name + ".txt"
            print ('Downloaded... ', filename)
            with open(filename, 'w') as f:
                #book.text IS THE DATA (book in text form)
                f.write(book.text.encode('UTF-8'))
        except:
            #If txt version does not exist, print this
            print ('Unable to retrieve .txt file for... ', book_name)
        
download_top_100()