**This folder contains python scripts to generate data utilized in the project** <br/><br/>

download_top_100.py -- Downloads the top 100 books from the last 30 days from Project Gutenberg <br/>
main url utilized: http://www.gutenberg.org/browse/scores/top#books-last30 <br/><br/>

frequency.py -- Goes through the downloaded books (stored in book_database) and generates a frequency <br/>
database in the form of a dictionary named book_freq_data.txt <br/><br/>

iindex.py -- Goes through the downloaded books (stored in book_database) and generates an inverted index <br/>
database in the form of a dictionary named book_iindex_data.txt (ended up not using this in the end, but still useful)<br/><br/>