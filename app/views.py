from app import app, db
from flask import render_template, request, redirect, url_for, flash, jsonify, json
from flask_login import login_user, logout_user, current_user, login_required
from forms import mk_profile
from models import UserProfile
from random import randint

import time
import os

# ----------------------------------

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/profile/', methods=['GET', 'POST'])
def make_profiles():
    form = mk_profile()
    file_folder = app.config['UPLOAD_FOLDER']
    if request.method == 'POST':
        
        # collection of data from the form
        Firstname = form.Firstname.data
        Lastname = form.Lastname.data
        Age = form.Age.data
        Bio = form.Bio.data
        Gender = request.form['Gender']

        # Genertating a unquie user id
        userid = str(randint(100000, 999999))

        # creating a username. NOTE did not know if I should allow the user 
        # to create one for themselves or not, so I'm choosing to generate one
        # dynamically.
        username = Firstname + str(randint(10, 999))

        # collecting the date of the submition of the profile
        date = timeinfo()

        # collecting the imAge and renaming 
        file = request.files['Image']
        file.filename = username
        file.save(os.path.join(file_folder, file.filename))

        # save data to database
        user = UserProfile(Firstname, Lastname, userid, Age, Bio, Gender, username, date)
        db.session.add(user)
        db.session.commit()

        flash('Profile Successfully Created')
        return redirect(url_for('home'))
    return render_template('mk_profile.html', form=form)

@app.route('/profiles/', methods=['GET', 'POST'])
def list_profiles():
    user_profiles = UserProfile.query.all()
    if request.method == 'POST':
        data = []
        for x in user_profiles:
            lst ={
            'username': x.username,
            'userid': x.userid
            }
            data.append(lst)
        return json.dumps(data)

    return render_template('lst_profiles.html', user_profiles = user_profiles)

@app.route('/profile/<userid>', methods=['GET', 'POST'])
def view_profiles(userid):
    get_profile = UserProfile.query.filter_by(userid=userid).first()
    if request.method == 'POST':
        data = {
        'userid': get_profile.userid,
        'username': get_profile.username,
        'image': get_profile.username,
        'gender': get_profile.gender,
        'age': get_profile.age,
        'date': get_profile.date
        }
        return jsonify(data)

    return render_template('vw_profiles.html', get_profile = get_profile)

# ----------------------------------

def timeinfo():
    now = time.strftime('%c')

    month = str(now[4:8])
    date = str(now[8:10])
    year = str(now[-4:])

    date_format = date + " " + month + " " + year

    return date_format

# ----------------------------------

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered pAge for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-Age=0'
    return response


@app.errorhandler(404)
def pAge_not_found(error):
    """Custom 404 pAge."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")