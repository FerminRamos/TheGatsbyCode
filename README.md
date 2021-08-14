# "TheGatsbyCode" - Created by Fermin Ramos

### Inspiration Behind the Code + Project's Intentions

On November 2020, I heard a podcast episode called, "The Bible Code". It detailed the story of a 
reporter named Michael Drosnin and his quest to find hidden meanings within Hebrew Scripture. 
According to Drosnin, his work has lead to the prediction of some of the world's biggest historical 
events. The podcast mentions how Drosnin had discovered events such as the Gulf War, the Great 
Depression, and the 1969 moon landing! I was skeptical at first, so I decided to investigate his
findings on my own. I, however, was not the first to do so. In fact, a research team experimented
with Drosnin's methodology on other religious scriptures and found similar results! Thus, it was 
concluded that Drosnin's experiments did ***not*** prove the superiority of the Hebrew Scripture. 
(It should be noted that the researchers did not discredit nor disrespect the Hebrew 
Scripture, and instead aimed to limit some of Michael Drosnin's faulty spiritual claims)

For most people, this was a happy ending to the whole debate. However, the researcher's conclusions 
left the door wide open for me. I was curious to know the extent of Drosnin's experiments and 
decided to take matters into my own hands. I wanted to know if ordinary library books, such as The 
Great Gatsby, could create prophecies as well? I decided to find the answer to my question by loosely
following Michael Drosnin's methodology. 

Creating meaningful predictions off of a book like The Great Gatsby was never the intention behind 
this code, which is why I didn't try to replicate Michael Drosnin's "Bible Code" exactly. Instead, 
this project was aimed as a parody towards Drosnin's unfounded religious claims. By showing how 
ordinary books are capable of producing similar data to religious texts, we can safely assume 
that all of Drosnin's predictions are based on statistical chance, rather than on religion.


### Michael Drosnin's "The Bible Code" Methodology


### Fermin Ramos' "The Gatsby Code" Methodology


### Included Files + Usage
1. ***"Book.txt"*** - Temporary text file. Used to manipulate the original text. This is strictly used for testing purposes. Will not be included in the final product.
2. ***"The Great Gatsby Full Text.txt"*** - Is the original, full-text, book of The Great Gatsby. This book version has been edited slightly to eliminate all unnecessary words//phrases. For example, it has removed all Onomatopoeias from the text, as they would not appear in our dictionary. I also removed all Chapter titles, as I do not regard those as being part of the "text". 
3. ***"Book.py"*** - Is a separate python file used in conjunction with the main.py file. Book.py holds a single python function, whose whole purpose is to read the text and pull all the needed words into an array for later use. More details can be found in the Book.py file. 
4. ***"Dictionary.py"*** - Is a separate python file used in conjunction with the main.py file. Dictionary.py holds a single dictionary that spans to nearly 10,000 lines of code. This dictionary was acquired using google's 10,000 most used common words. The spacing of the dictionary may appear "jagged", but that is because all 10,000 lines of code were written using an automated python script. The file works and is perfectly readable. More details can be found in the Dictionary.py file. 
5. ***"google-10000-english-no-swears.txt"*** - Is an altered version of google's dictionary. It contains the 10,000 most common english words (excluding swear words). I used the 10,000 most common words instead of the first 10,000 words on an ordinary dictionary because common every-day terms would appear more frequently and thus be more useful. 
6. ***"google.py"*** - Is a separate python file used in conjunction with the main.py file. google.py holds a single python function, whose whole purpose is to read
the "google-10000-english-no-swears.txt" file and cross-referrence our words that we pulled from The Great Gatsby with those from google's dictionary. If a word matches in ***both*** instances, then we can safely use that word to create a prophecy. More details can be found in the google.py file. 
7. ***"main.py"*** - The main python file. Details on algorithms, how-to-use, and other mechanics can be found in the README.md file. 
