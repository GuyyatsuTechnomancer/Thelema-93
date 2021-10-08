#!/bin/python3
from flask import Flask, render_template
from flask_navigation import Navigation
import sys
sys.path.append('./ThothFunctions')
from ThothClass import *

Thelema93 = Flask(__name__)
nav = Navigation(Thelema93)

nav.Bar('top', [
  nav.Item('Home Page', 'HomePage'),
  nav.Item('Card List', 'CardIndex'),
  nav.Item('Random Card', 'RenderCard', {'CARD': str(Thoth.RandomCard())})
])

@Thelema93.route('/')
@Thelema93.route('/THOTH')
def HomePage():
  return render_template(
    "HomeLayout.html",
    PageTitleitle="THOTH",
    WorkingTitle="93/93; 93",
    description=str("Tarot Online; The Works of Aleister Crowley,"
      " presented by the student Guyyatsu Hikikomori.")
  )


@Thelema93.route('/ATU')
def CardIndex():
  return render_template(
    "IndexLayout.html",
    PageTitle="The ATU",
    WorkingTitle="The 78 Rays of the Sun",
    description=str('Index page of all the cards of the deck.'),
    PageBlock="{% block IndexPage %}",
    content=BuildIndex()
  )

@Thelema93.route('/ATU/<string:CARD>')
def RenderCard(CARD):
  return render_template(
    "CardLayout.html",
    PageTitle=CARD,
    WorkingTitle=CARD,
    description="A card in the deck",
    PageBlock="{% block CardPage %}",
    ImagePath=DrawCard(card=CARD,data='picture'),
    CardEssay=DrawCard(card=CARD,data='essay')
  )