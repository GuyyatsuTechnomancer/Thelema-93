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
"""
  from PIL import Image

  def GetColor(IMAGE, ColorElement):

    def rgb2hex(r, g, b, switch):
      HexCode='#{:02x}{:02x}{:02x}'.format(r, g, b)
      if switch == 'BACKGROUND':
        return HexCode
      elif switch == 'TEXT':
        r, g, b = (256-r), (256-g), (256-b)
        return HexCode

    pixel=Image.open(IMAGE).resize((1, 1))# Pixel-ize and initialize 1-liner.

    if pixel.mode in ('RGBA', 'LA') or (pixel.mode == 'P' and 'transparency' in pixel.info):
      colors = list(pixel.convert('RGBA').getdata())

      for r, g, b, a in pixels: # just ignore the alpha channel
        return rgb2hex(r, g, b, ColorElement)
"""
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
  _html = []
  _hreflist=[]
  for card_type in Thoth.types:
    for card in Thoth.ATU:
      if tarot[card]['class']==card_type:
        _hreflist.append(f"      <li><a href={{{{ url_for('RenderCard', CARD='{card}') }}}}>{card}</a></li>\n")
    _html.append(f"<ul>\n  <li>{card_type}</li>\n  <li>\n    <ul>\n")
    for href in _hreflist: _html.append(href)
    _html.append("    </ul>\n  </li>\n</ul>\n\n")
    _hreflist.clear()
  for item in _html:
    ElementObject+=str(item)
  return ElementObject


def TextConverter(TextFile):
  HtmlString=''
  StringContainer=[]
  dStart='<p>'
  dEnd='</p>\n'
  with open(str(TextFile), 'r') as TextBlock:
    for line in TextBlock.readlines():
      LetterCount = 0
      FormattedLine = ''
      StringContainer.append(dStart)
      LetterList = [char for char in line]
      for letter in LetterList:
        FormattedLine+= letter
        LetterCount += 1
        if LetterCount == 94:
          FormattedLine+= '\n'
          LetterCount = 0
      FormattedLine+=dEnd
      StringContainer.append(FormattedLine)
  for StringElement in StringContainer:
    HtmlString+=StringElement
  return HtmlString