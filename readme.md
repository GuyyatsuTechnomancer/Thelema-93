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

## The Breakdown

It currently consists of two files, ThothDatabase and ThothClass. 

### ThothDatabase
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


### ThothClass
ThothClass defines an object class named Thoth, which owns .DrawRandomCard() and .ReturnCardData(). 

Thoth.DrawRandomCard does exactly what it says on the tin;
it draws a random card by calling random.choice(list(ThothDatabase.tarot.keys())) and returning the results.

Thoth.ReturnCardData(cardd, dFormat) will return either a given cards picture or it's essay, depending whether or not you set
the dFormat argument to 'picture' or 'essay' respectively.
