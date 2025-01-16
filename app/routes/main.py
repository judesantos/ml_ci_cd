"""
This module contains the main routes for the Flask app.

Implements the home route for the application.
Initializes the main blueprint for the application.
"""

from flask import Blueprint, render_template, url_for
from flask import redirect, flash
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from UI.survey_form import SurveyForm
from extensions import limiter

bp = Blueprint('main', __name__)


@bp.route('/')
@limiter.limit("5 per minute")
def home():
    return render_template(
        'index.html',
    )


@bp.route('/dashboard', methods=['GET', 'POST'])
@limiter.limit("100 per minute")
@jwt_required()
def dashboard():

    form = SurveyForm()
    if form.validate_on_submit():
        # Run inference on the survey data here.

        flash('Survey submitted successfully', 'success')
        return redirect(url_for('main.dashboard'))

    user = get_jwt_identity()
    form = SurveyForm()

    return render_template('dashboard.html', user=user, form=form)
