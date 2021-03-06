#!/bin/python3
from flask import Flask, render_template, url_for, render_template_string
from flask_navigation import Navigation
import sys
sys.path.append('./ThothFunctions')
from ThothClass import *

Thelema93 = Flask(__name__, static_url_path='/static')
nav = Navigation(Thelema93)

nav.Bar('top', [
  nav.Item('Home Page', 'HomePage'),
  nav.Item('Card List', 'CardIndex'),
  nav.Item('Random Card', 'DrawRandomCard')
])

@Thelema93.route('/')
@Thelema93.route('/TheBookOfThoth')
@Thelema93.route('/Tarot')
@Thelema93.route('/Thoth-Tarot')
def HomePage():
  """ The initial entrypoint to the whole deck;
  with a bit of exposition by Aleister Crowley himself."""
  return render_template(
    "HomePage.html",
    PageTitleitle="THOTH",
    description=str("Tarot Online; by Guyyatsu Hikikomori."),
    PageHeader="93/93; 93",
    PageContent=TextConverter('static/resources/articles/Thelema93-body')
  )

@Thelema93.route('/ATU')
@Thelema93.route('/KEYS')
def CardIndex():
  """ """
  return render_template(
    "Index.html",
    PageTitle="The ATU",
    description=str('Index page of all the cards of the deck.'),
    PageHeader="The 78 Rays of the Sun",
    PageContent=render_template_string(BuildIndex())
  )

@Thelema93.route('/ATU/<CARD>')
@Thelema93.route('/KEYS/<CARD>')
def RenderCard(CARD):
  return render_template(
    "Card.html",
    PageTitle=CARD,
    WorkingTitle=CARD,
    description="A card in the deck",
    ImagePath=url_for('static', filename='content/' + str(DrawCard(card=CARD,data='picture'))),
    CardEssay=TextConverter(str('static/content/' + DrawCard(card=CARD,data='essay')))
  )

@Thelema93.route('/DRAW')
@Thelema93.route('/DrawRandom')
@Thelema93.route('/RandomCard')
@Thelema93.route('/RANDOM')
@Thelema93.route('/random')
def DrawRandomCard():
  CARD=str(Thoth.RandomCard())# Here's the fucker!
  return render_template(
    "Card.html",
    PageTitle=CARD,
    WorkingTitle=CARD,
    description="A card in the deck",
    ImagePath=url_for('static', filename='content/' + str(DrawCard(card=CARD,data='picture'))),
    CardEssay=TextConverter(str('static/content/' + DrawCard(card=CARD,data='essay')))
  )


if __name__ == "__main__":
  Thelema93.run(host='0.0.0.0')