from werkzeug.utils import secure_filename
import ocrspace, os
from docx import Document

UPLOAD_FOLDER = 'static/uploads'
FILES_DIR = 'static/texts'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
langs = [
    'Arabic',
    'Bulgarian',
    'Chinese_Simplified',
    'Chinese_Traditional',
    'Croatian',
    'Danish',
    'Dutch',
    'English',
    'Finnish',
    'French',
    'German',
    'Greek',
    'Hungarian',
    'Italian',
    'Japanese',
    'Korean',
    'Norwegian',
    'Polish',
    'Portuguese',
    'Russian',
    'Slovenian',
    'Spanish',
    'Swedish',
    'Turkish'
]

# get Text from file input(file)=>output(str'text')
def ocr(file, language = 'English'):

    if not file:
        return {
            'CODE': 1,
            'MSG': 'File not attached!'
        }

    if not(allowed_file(file.filename)):
        return {
            'CODE': 2,
            'MSG': 'PDF, PNG, JPG and JPEG files are allowed only!'
        }
    
    file = save_file(file)

    try:
        api = eval(f"ocrspace.API('e36c320cbb88957', ocrspace.Language.{language})")
        text = api.ocr_file(file)
    except Exception as e:
        return {
            'CODE': 3,
            'MSG': e
        }
    finally:
        os.remove(file)
    
    return {
            'CODE': 0,
            'MSG': text
        }

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    filename = secure_filename(file.filename)
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    return os.path.join(UPLOAD_FOLDER, filename)

