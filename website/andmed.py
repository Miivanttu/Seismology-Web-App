from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField, DateTimeField
from wtforms.validators import DataRequired
from .models import Data
from . import db
from datetime import datetime

# Define the form class
class DataForm(FlaskForm):
    kuupaev = DateTimeField('Kuupäev', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
    vertikaalne = FloatField('Vertikaalne', validators=[DataRequired()])
    horisontaalne = FloatField('Horisontaalne', validators=[DataRequired()])
    piki = FloatField('Piki', validators=[DataRequired()])
    risti = FloatField('Risti', validators=[DataRequired()])
    vektor_summa = FloatField('Vektor-summa', validators=[DataRequired()])
    submit = SubmitField('Add Data')

# Blueprint for the "Andmed" page
andmed = Blueprint('andmed', __name__)

@andmed.route('/andmed', methods=['GET', 'POST'])
def andmed_home():
    form = DataForm()

    if form.validate_on_submit():
        try:
            # Extract data from the form
            kuupaev = form.kuupaev.data
            vertikaalne = form.vertikaalne.data
            horisontaalne = form.horisontaalne.data
            piki = form.piki.data
            risti = form.risti.data
            vektor_summa = form.vektor_summa.data

            # Insert data into the database
            data = Data(
                kuupaev=kuupaev,
                vertikaalne=vertikaalne,
                horisontaalne=horisontaalne,
                piki=piki,
                risti=risti,
                vektor_summa=vektor_summa
            )
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('andmed.andmed_home'))
        except Exception as e:
            print(f"Error: {e}")
            form.kuupaev.errors.append('Invalid date format.')

    # Query all data entries to display in the table
    data_entries = Data.query.all()
    return render_template('andmed.html', form=form, data_entries=data_entries)