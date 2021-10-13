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
  nav.Item('Random Card', 'RenderCard', {'CARD': Thoth.RandomCard()})
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

@Thelema93.route('/ATU/<string:CARD>')
def RenderCard(CARD):
  return render_template(
    "Card.html",
    PageTitle=CARD,
    WorkingTitle=CARD,
    description="A card in the deck",
    ImagePath=url_for('static', filename='content/' + str(DrawCard(card=CARD,data='picture'))),
    CardEssay=TextConverter(str('static/content/' + DrawCard(card=CARD,data='essay')))
  )