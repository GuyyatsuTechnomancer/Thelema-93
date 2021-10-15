# PythonTarot


## The Story

This is the project that inspired me to learn programming in the first place. 

It started off as an attempt at disseminating the tarot as codified 
by Aleister Crowley, just static html pages hand-typed with copy-pasted 
data from poorly formatted public domain resources.

It was a glorified index page, at best. Absolutely no 'smart' design whatsoever.

Then I wanted the ability to pull a random card like a real deck but also automagically 
have the long-form text data associated with it; it went through a couple iterations and 
took a little more familiarity with python before getting here but it's here, and I'm proud of it.

# Thelema93
-----------
The wsgi entry point. Initializes the the entire thing; from setting us up with a preferred port-ip address to defining the url routes and building the pages from template.

We got three routes; the home page, the index page, and the random page.



# Templates
-----------
Templates are the building blocks of Flask, they allow for programming and modularity in
your structure.  layout.html is common to all pages; it puts the ML in HTML, while the routs defined in Thelema93 refer to the blocks being applied to the template.


# ThothFunctions
----------------

## ThothDatabase
ThothDatabase contains a nested dictionary, ThothDatabase.tarot, that has a 1:1 mapping 
of the card titles as the names of sub-dictionaries.  These sub-dicts also contain the card title, 
as well as it's class (TRUMPS, COURTS, MINORS.)  For COURTS and MINORS their order and suit are also 
defined.

The values defined within the sub-dicts correlate with directories within found within the greater 
TAROT sub-module; for example we have:

> TarotDatabase.tarot['TwoOfSwords']: 
>> 'title': 'TwoOfSwords', 
>> 'class': 'MINORS', 
>> 'order': 'TWOS', 
>> 'suit': 'SWORDS' 

The Thoth.ReturnCardData function plugs these values into fstrings to return a 
relative filepath on the fly. 


## ThothClass
ThothClass defines an object class named Thoth, which defines a few variables and 
functions used by the mainline functions.

ATU is a list of all the cards, types includes a handy reference to important points in the ThothDatabase, RandomCard does exactly what it says on the tin;
it draws a random card by calling random.choice(Thoth.ATU) and returning the results.

DrawCard(card, data) will return either a given cards picture or it's essay, depending whether or not you set the data argument to 'picture' or 'essay' respectively.

BuildIndex iterates over the list of cards and uses the types list to compare each card
to the ThothDatabase and check if the values contains the relevant type string.  If it does,
it wraps the cards title with html formatting and appends it to the _hreflist.  Once the
list has been exhausted the _hreflist is iterated over to be concatenated into a singular
string that is then returned.

TextConverter does something similar, only it takes a text file and iterates over the lines of text and wraps them in <p> tags while keeping track of how many letters are being passed and applying plaintext page breaks every 94 characters for ease of rendered source code viewing.