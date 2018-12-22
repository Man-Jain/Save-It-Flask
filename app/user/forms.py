from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

class NotesForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Create Note')

class EditNotesForm(FlaskForm):
	description = StringField('Description', validators=[DataRequired()])
	submit = SubmitField('Edit Note')