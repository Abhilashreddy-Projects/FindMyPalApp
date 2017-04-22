"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, get, post
from datetime import datetime
from bottle import template


@route('/')
@route('/login')
@view('login')
def home():
    """Renders the home page."""
    return dict (
    )


@route('/register')
@view('Register')
def register():
    """ returns register page """
    return dict()