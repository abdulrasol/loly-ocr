from flask import Flask, redirect, request, render_template, send_file, send_from_directory
from flask_session import Session
from tempfile import mkdtemp
import helpers, time, os



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
    return render_template('home.html', action='/editing', langs=helpers.langs, msg=msg, title='Loly | Upload file to extract text')

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
            return render_template('editing.html', action='/downloading', text = get['MSG'], title='Loly | editing extracted text')
        else:
            print(get)
            return home(get['MSG'])
    return home('Selcet file first!')

# downloading file after editing
@app.route('/downloading', methods=["GET", "POST"])
def downloading():
    if request.method == 'POST':
        # save file as user request
        filename = time.strftime(f"%y%m%d%H%M%S.{request.form.get('get')}")
        with open(os.path.join(helpers.FILES_DIR,filename),'a') as file:
            file.write(request.form.get('text'))
            for file in os.listdir(helpers.FILES_DIR):
                file = os.path.join(helpers.FILES_DIR, file)
                if os.stat(file).st_mtime < time.time() - 900:
                    os.remove(file)
        url = f'{request.url_root}{helpers.FILES_DIR}/{filename}'
        return render_template('downloading.html', url=url, title=f"Loly | download extracted text as{request.form.get('get')}")
    return home('Start by uploading file first!')

# setup PWA app
@app.route('/service-worker.js')
def sw():
    return app.send_static_file('js/service-worker.js'), 200, {'Content-Type': 'text/javascript'}