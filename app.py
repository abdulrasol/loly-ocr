from flask import Flask, redirect, render_template
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.utils import secure_filename
import helpers



app = Flask(__name__)


# App Configs
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["DEBUG"] = True
app.config['UPLOAD_FOLDER'] = helpers.UPLOAD_FOLDER
app.config['FILES_DIR'] = helpers.FILES_DIR
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# utitize
app.secret_key = 'super secret key'

# Home def
@app.route('/')
def home(msg = None):
    return render_template('home.html')

# Editing Def
@app.route('/editing')
def editing(msg = None):
    return render_template('editing.html')

# downloading file after editing
@app.route('/downloading')
def downloading():
    pass