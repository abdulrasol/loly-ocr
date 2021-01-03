from flask import Flask, redirect, request, render_template
from flask_session import Session
from tempfile import mkdtemp
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
    if msg == None:
        msg = False
    return render_template('home.html', action='/editing', langs = helpers.langs, msg=msg)

# Editing Def
@app.route('/editing', methods=["GET", "POST"])
def editing(msg = None):
    if request.method == 'POST':
        
        if request.form.get('lang') == None:
            return home('Selcet language!')
        
        if not(request.files['camera']):
            file = request.files['file']
        else:
            file = request.files['camera']
            
        
        get = helpers.ocr(file, language=request.form.get('lang'))
        if get['CODE'] == 0:
            return render_template('editing.html', action='/download', text = get['MSG'])
        else:
            return home(get['MSG'])
    return home('Selcet file first!')

# downloading file after editing
@app.route('/downloading')
def downloading():
    pass