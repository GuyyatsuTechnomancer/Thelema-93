#!/bin/python3
from ThothDatabase import tarot

class Thoth:
  ATU=list(tarot.keys())
  def RandomCard(): from random import choice; return choice(Thoth.ATU)


def DrawCard(card, data):
  """ Returns the url path for a given card's picture or text.
  If no specification is made towards either, the picture is rteturned."""
  def ShowEssay(route):
    with open(route, 'r') as essay:
      return str(essay.read())

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
  """ Creates an unordered list """
  _cardlist = []
  def ClassifyType(hierarchy):
    _cardlist.clear()
    for card in Thoth.ATU:
      if tarot[card]['class']==str(hierarchy):
        _cardlist.append(card)

  def CardHREF(CardClass):
    ClassifyType(CardClass)
    for card in _cardlist:
      return str("<li><a href='{{ url_for('ATU/" + str(card) + "') }}'>" + str(card) + "</a></li>")
  
  CardIndex = str(
    "<ul><li>Trumps<li><li><ul>"
    + CardHREF("TRUMPS")
    + "</ul></li></ul><br>"
    + "<ul><li>Courts<li><li><ul>"
    + CardHREF('COURTS')
    + "</ul></li></ul><br>"
    + "<ul><li>Minors<li><li><ul>"
    + CardHREF('MINORS')
    + "</ul></li></ul><br>"
  )

  return CardIndex