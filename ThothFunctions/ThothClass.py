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
  types=['TRUMPS', 'COURTS', 'MINORS']
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
  """ Constructs a unique html element for ease of routing views."""
  ElementObject=""
  _html = ['<ul>']
  _hreflist=[]
  for card_type in Thoth.types:
    for card in Thoth.ATU:
      if tarot[card]['class']==card_type:
        _hreflist.append(f"<li><a href='{{{{ url_for('ATU/{card}') }}}}'>{card}</a></li>")
    _html.append(f"<li>{card_type}</li><li><ul>")
    for href in _hreflist: _html.append(href)
    _html.append("</li></ul>")
    _hreflist.clear()
  _html.append('</ul>')
  for item in _html:
    ElementObject+=str(item)
  return ElementObject