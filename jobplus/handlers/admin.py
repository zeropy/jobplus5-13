from flask import Blueprint
from flask import render_template, redirect, url_for
from jobplus.forms import Register

admin  = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def index():
    return 'admin index'

@admin.route('/register',methods=['GET','POST'])
def register():
    form = Register()
    if form.validate_on_submit():
        form.create_user()
        return redirect(url_for('front.index'))
    return render_template('register.html',form=form)
