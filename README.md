**Written by Leo Au-Yeung and Thomas Westfall** <br /><br />
**Project Description:** <br />
Create a library catalog-esque project. Project will utilize iindex algorithms, books (English) from Project Gutenberg, NYPL API. Possibly utilize n-grams if we have time <br />

Using books from Project Gutenberg (https://www.gutenberg.org/) : <br />
Create an inverted index (iindex) of English books for categorization: <br />
Each book would have its own index of words (after ridding major “stop words”/common words) and their frequencies <br />
The “indexes” would be the books themselves (so we’ll have a whole catalog of English books) <br /><br />

**Main Goals:** <br />
What a user will be able to do: <br />
Look up one or more genres of books to find books in our “database” (database will just contain Project Gutenberg books in English) matching the genre(s) <br />
Program will return most relevant results (say top 5-10?) books of those genres. This will be done by: <br />
Return all books containing the major keywords of each genre (iindex part) along with making sure the words actually appear a good number of times (frequency part); keywords will be found with NYPL/Amazon API (can't seem to find a good list with a Google search of "book genre keywords"<br />
Checking the frequencies of the keywords of each book, and returning the books with the most frequent occurrences of keywords <br /> <br />

**Side/Future Goals:** <br />
“Create” a book out of the data using n-grams as well; machine-learning esque project
