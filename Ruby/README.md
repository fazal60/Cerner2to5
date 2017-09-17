# Cerner2^5

## The script
* This repo contains a ruby script named *Cerner2to5.rb*
* This script uses Goodreads API to get information about authors and books.
* The information is returned in XML format.
* Nokogiri gem has been utilized to parse XML data.

## Installation and Usage
* [API Documentation](https://www.goodreads.com/api/documentation)
* I have hardcoded my own API_Key for the purpose of this demo.
* You need to pass in an authorname to fetch booklist for that author.
* If you pass a random string, the API logic tries to find the authorname closely matching the string you entered. On failing to find one, it flashes and Invalid author name message.


```
git clone https://github.com/sheikhms60/Cerner2to5.git
cd Cerner2to5
cd Ruby
ruby Cerner2to5 Rowling
```
### Expected result
```
Author name closest to the one you passed in is 'J.K. Rowling'
------Books by this author are as follows------
Harry Potter and the Sorcerer's Stone (Harry Potter, #1)
Harry Potter and the Prisoner of Azkaban (Harry Potter, #3)
Harry Potter and the Deathly Hallows (Harry Potter, #7)
Harry Potter and the Goblet of Fire (Harry Potter, #4)
Harry Potter and the Chamber of Secrets (Harry Potter, #2)
Harry Potter and the Order of the Phoenix (Harry Potter, #5)
Harry Potter and the Half-Blood Prince (Harry Potter, #6)
The Tales of Beedle the Bard
Harry Potter Boxset (Harry Potter, #1-7)
The Casual Vacancy
```

### Edge cases
* Special characters passed in for authorname will raise an exception which is handled.
* No argument passed in will flash a message.




