#!/bin/python3
from flask import Flask, render_template, url_for, render_template_string
from flask_navigation import Navigation
import sys
sys.path.append('./ThothFunctions')
from ThothClass import *

Thelema93 = Flask(__name__)
nav = Navigation(Thelema93)

RandomCard=(str(Thoth.RandomCard()))

nav.Bar('top', [
  nav.Item('Home Page', 'HomePage'),
  nav.Item('Card List', 'CardIndex'),
  nav.Item('Random Card', 'RenderCard', {'CARD': RandomCard})
])

@Thelema93.route('/')
@Thelema93.route('/THOTH')
def HomePage():
  return render_template(
    "HomeLayout.html",
    PageTitleitle="THOTH",
    WorkingTitle="93/93; 93",
    description=str("Tarot Online; by Guyyatsu Hikikomori.")
  )


@Thelema93.route('/ATU')
def CardIndex():
  return render_template(
    "IndexLayout.html",
    PageTitle="The ATU",
    WorkingTitle="The 78 Rays of the Sun",
    description=str('Index page of all the cards of the deck.'),
    content=render_template_string(BuildIndex())
  )

@Thelema93.route('/ATU/<string:CARD>')
def RenderCard(CARD):
  return render_template(
    "CardLayout.html",
    PageTitle=CARD,
    WorkingTitle=CARD,
    description="A card in the deck",
    ImagePath=DrawCard(card=CARD,data='picture'),
    CardEssay=DrawCard(card=CARD,data='essay')
  )