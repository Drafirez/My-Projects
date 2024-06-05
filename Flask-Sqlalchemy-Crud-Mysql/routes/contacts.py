from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return render_template('index.html')

@contacts.route('/new')
def add_contacts():
    return 'Saving a contact'

@contacts.route('/update')
def update():
    return 'Update a contact'

@contacts.route('/delete')
def delete():
    return 'Delete a contact'