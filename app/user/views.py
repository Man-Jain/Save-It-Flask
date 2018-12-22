from flask import abort, render_template, flash, redirect, url_for

from .. import db
from ..models import Notes
from .forms import *
from . import user

@user.route('/')
@user.route('/index')
def index():
	notes = Notes.query.all()
	return render_template('/user/index.html', notes = notes)

@user.route('/forms', methods = ['GET', 'POST'])
def forms():
	form = NotesForm()
	if form.validate_on_submit():
		note = Notes(title=form.title.data,
					 description=form.description.data)
		note.save()
		flash('Note Saved')
		return redirect(url_for('user.forms'))

	return(render_template('/user/forms.html', form=form, title='Add Note'))

@user.route('/edit/<note_id>', methods = ['GET', 'POST'])
def edit_note(note_id):
	edited_note = Notes.query.get(mongo_id=note_id)

	form = EditNotesForm()
	if form.validate_on_submit():
		edited_note.description = form.description.data
		edited_note.save()
		flash('Note Edited')
		return redirect(url_for('user.forms'))

	return(render_template('/user/edit-forms.html', form=form, title='Edit Note', note=edited_note))

@user.route('/delete/<note_id>', methods = ['GET', 'POST'])
def delete_note(note_id):
	deleted_note = Notes.query.get(mongo_id=note_id)
	deleted_note.remove()

	return(redirect(url_for('user.index')))