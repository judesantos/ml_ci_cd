"""
This module contains the main routes for the Flask app.

Implements the home route for the application.
Initializes the main blueprint for the application.
"""

from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    return render_template(
        'dashboard.html',
        message="Welcome to the secure Flask app!"
    )
