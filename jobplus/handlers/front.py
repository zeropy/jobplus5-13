from flask import Blueprint
from flask import render_template, url_for

front = Blueprint('front', __name__)

@front.route('/')
def index():
    return 'sdf'
