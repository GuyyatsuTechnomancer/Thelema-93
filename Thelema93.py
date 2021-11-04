#!/bin/python3
from flask import Flask, render_template, url_for, render_template_string, redirect, request 
from flask_navigation import Navigation
import sys
sys.path.append('./ThothFunctions')
from ThothClass import *
import json

Thelema93 = Flask(__name__, static_url_path='/static')
nav = Navigation(Thelema93)

nav.Bar('top', [
  nav.Item('Home Page', 'HomePage'),
  nav.Item('Card List', 'CardIndex'),
  nav.Item('Random Card', 'redirection') #removed the argument from here as it was causing the issues - replaced the Url item with redirection to send user to be redirected
])

@Thelema93.route('/')
@Thelema93.route('/THOTH')
def HomePage():
  return render_template(
    "HomePage.html",
    PageTitleitle="THOTH",
    description=str("Tarot Online; by Guyyatsu Hikikomori."),
    PageHeader="93/93; 93",
    PageContent=TextConverter('static/resources/articles/Thelema93-body')
  )

@Thelema93.route('/ATU')
def CardIndex():
  return render_template(
    "Index.html",
    PageTitle="The ATU",
    description=str('Index page of all the cards of the deck.'),
    PageHeader="The 78 Rays of the Sun",
    PageContent=render_template_string(BuildIndex())
  )

#random card nav.item takes you here in order for 'Thoth.RandomCard()' to be invoked and subsequently carry over its variable with the redirect function to 'RenderCard(card)' and pass the variable in as it's parameter and thus changing the name of the end point
@Thelema93.route('/ATU/redirect')
def redirection():
  CARD = Thoth.RandomCard()
  return redirect(url_for('RenderCard', card=CARD ))


@Thelema93.route('/ATU/<card>')
def RenderCard(card):
  #determines whether the user has been on this endpoint before so that when they refresh the page, they get redirected to 'redirection'
  with open('counter.json') as c:                                               
    counter = json.load(c)    
  if counter < 1:
    counter += 1
    with open('counter.json', 'w') as c:
      json.dump(counter, c)
      counter = 0
  if counter > 0:
    counter = 0
    with open('counter.json', 'w') as c:
      json.dump(counter, c)
    return redirect(url_for('redirection'))

  picture = str(DrawCard(card,data='picture'))
  essay = DrawCard(card,data='essay')
  return render_template(
    "Card.html",
    PageTitle=card,
    WorkingTitle=card,
    description="A card in the deck",
    ImagePath=url_for('static', filename='content/' + picture),
    CardEssay=TextConverter(str('static/content/' + essay))
  )

if __name__ == '__main__':
    Thelema93.run(host="localhost", port=8080, debug=True)