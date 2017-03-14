from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, RadioField, FileField
from flask_wtf.file import FileRequired
from wtforms.validators import InputRequired

class mk_profile(FlaskForm):
	"""docstring for mk_profile"""
	Firstname = StringField('Firstname', validators=[InputRequired()]) # Example of adding a placeholder using flask form... will not apply to this file because another method is impliemented in mk_profile.html
	Lastname = StringField('Lastname', validators=[InputRequired()]) # Firstname = StringField('Firstname', validators=[InputRequired()], render_kw={"placeholder": "First Name"})
	Age = IntegerField('age')
	Bio = TextAreaField('biography')
	Image = FileField(validators=[FileRequired])
	Gender = RadioField('Gender', choices = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')])


