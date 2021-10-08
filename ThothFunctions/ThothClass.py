#!/bin/python3
""" Functional back end for the flask instance.

The Thoth class contains a couple preleminary variables common to all functionality;
    A list of all the cards in the deck taken from the dictionary,
    The ability to randomly pull a card from that list.

DrawCard takes a card and gives back either it's text or it's image as a file path.

BuildIndex generates a useable html pattern with proper headings and classification of it's members.

    It achieves this by first accepting one of three classes: 'TRUMPS', 'COURTS', or 'MINORS', then comparing
members of the ATU list against values within same-named sub-dictionaries that match the given class.

    The resulting list is iterated over to be wrapped within an html string after first printing the structural
html headings."""
from ThothDatabase import tarot


class Thoth:
  ATU=list(tarot.keys())
  def RandomCard():
    from random import choice
    return choice(Thoth.ATU)


def DrawCard(card, data):
  """ Returns the url path for a given card's picture or text.
  Accepts a card title, and either 'essay' or 'jpg'."""
  if data=='picture': ext='jpg'
  elif data=='essay': ext=str(data)
  else: ext='jpg'

  CardObject=tarot[card]; cTitle=CardObject['title']; cClass=CardObject['class']

  if cClass=='TRUMPS': return str(f"{cClass}/{cTitle}/{cTitle}.{ext}") 
  else:
    cOrder=CardObject['order']
    cSuit=CardObject['suit']
    return str(f"{cClass}/{cOrder}/{cSuit}/{cTitle}.{ext}")


def BuildIndex():
  """ Creates an unordered list of linked line items
  referencing a specific cards route in the flask app.
  
  The idea here is to render an html block containing all the
  cards organized under their class as an unordered list whose
  members are references to api routing calls."""
  _cardlist = []

  def ClassifyCard(hierarchy):
    """ Generates a list of cards based on type; i.e, 'TRUMPS', 'COURTS', or 'MINORS',
    and then saves it to RAM for the next function to pick up."""
    _cardlist.clear()
    for card in Thoth.ATU:
      if tarot[card]['class']==str(hierarchy):
        _cardlist.append(card)

  def CardLinker(CardClass):
    """ Calls ClassifyType and formulates an html string for the given card."""
    ClassifyCard(CardClass)
    for card in _cardlist:
      return str("<li><a href='{{ url_for('ATU/" + str(card) + "') }}'>" + str(card) + "</a></li>")
""" Here's where the bug's at. Need to figure a way to return CardLinker three times
  as a sub-line of an unordered list. Like so:

<ul>
  <li>TRUMPS</li>
  <li>
    <ul>
      <li>Card 1</li>
      <li>Card 2</li>
    </ul>
  </li>

  <li>COURTS</li>
  <li>
    <ul>
      <li>Card 3</li>
      <li>Card 4</li>
    </ul>
  </li>

  <li>MINORS</li>
  <li>
    <ul>
      <li>Card 5</li>
      <li>Card 6</li>
    </ul>
  </li>
</ul>
"""