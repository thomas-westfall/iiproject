
Project: LTE - Library Testing Environment
==============================================================

**Created by Team L-T-E -- Leo Au-Yeung and Thomas Westfall** <br /><br />

Project submitted on December 19, 2017<br /><br />

==============================================================

**Project Description:** <br />
LTE: Library Testing Environment is a project that imitates searching a library catalog<br />
A user will choose a book genre that they wish to search up,<br />
and the program returns the top 10 books corresponding to that genre from our database<br /><br />

==============================================================

**Running the project:**<br />
Make sure you have python installed on your system<br />
	- python app.py
Open up a browser and go to localhost:8000<br /><br />

==============================================================

**Project flow**<br />
The user will open up the homepage and select a genre from the preset list<br />
The python backend then takes the genre selection and calls up the genre's keywords<br />
The genre's keywords are then used to coordinate with the frequency data of books in the database<br />
The books with the most frequent number of keywords that match those of the genre are chosen (10 books)<br />
The books' titles are then returned to the user in the result page listed in a table from 1 to 10<br /><br />

==============================================================

**Project creation flow:**<br />
First started off with the basics folder: Created and, or, and not queries with an inverted index<br />
Extensions of project:<br />
(More raw detail can be found in to-do.txt)<br />
Downloaded top 100 books from Project Gutenberg (https://www.gutenberg.org/)<br />
Created a frequency table and inverted index of English books for categorization (ended up using only frequency) <br />
Created a python backend which takes a query of pre-set book genres and returns a list of top (10) books from our database<br />
Created a flask frontend which has two pages: homepage to input a query and result page listing book results<br /><br />