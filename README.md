**Created by Team L-T-E: Leo Au-Yeung and Thomas Westfall** <br /><br />
**Project Description:** <br />
LTE: Library Testing Environment is a project that imitates searching a library catalog<br />

**Running the project:**


**Project creation flow:**<br />
Downloaded top 100 books from Project Gutenberg (https://www.gutenberg.org/)<br />
Created a frequency table and inverted index of English books for categorization (ended up using only frequency) <br />
Created a python backend which takes a query of pre-set book genres and returns a list of top (10) books from our database<br />
Created a flask frontend which has two pages: homepage to input a query and result page listing book results<br /><br />

**Main Goals:** <br />
What a user will be able to do: <br />
Look up one or more genres of books to find books in our “database” (database will just contain Project Gutenberg books in English) matching the genre(s) <br />
Program will return most relevant results (say top 5-10?) books of those genres. This will be done by: <br />
Return all books containing the major keywords of each genre (iindex part) along with making sure the words actually appear a good number of times (frequency part); keywords will be found with NYPL/Amazon API (can't seem to find a good list with a Google search of "book genre keywords"<br />
Checking the frequencies of the keywords of each book, and returning the books with the most frequent occurrences of keywords <br /> <br />

**Side/Future Goals:** <br />
“Create” a book out of the data using n-grams as well; machine-learning esque project
