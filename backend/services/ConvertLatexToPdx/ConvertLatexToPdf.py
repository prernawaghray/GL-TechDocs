# Store this code in 'app.py' file
import pathlib
import stat
import warnings

from flask import Flask, request, Blueprint
import os, subprocess, platform
import sys

# Suppress warnings
warnings.filterwarnings("ignore")

sys.path.append('../')

convertLatexToPdfBlueprint = Blueprint('convertLatexToPdfBlueprint', __name__)


@convertLatexToPdfBlueprint.route('/api/convertLatexToPdf', methods=['GET'])
def convertToPdf():
    # TeX source filename
    tex_filename = request.args.get('filepath')
    filename, ext = os.path.splitext(tex_filename)
    # the corresponding PDF filename
    pdf_filename = filename + '.pdf'
    log_filename = filename + '.log'
    aux_filename = filename + '.aux'
    path = pathlib.Path(tex_filename).parent
    os.chmod(path, stat.S_IRWXO)
    print(pdf_filename)

    # compile TeX file
    subprocess.run('pdflatex -interaction=nonstopmode -no-shell-escape ' + tex_filename, shell=True, check=True)

    # check if PDF is successfully generated
    if not os.path.exists(pdf_filename):
        raise RuntimeError('PDF output not found')
    if os.path.exists(log_filename):
        os.remove(log_filename)
    if os.path.exists(aux_filename):
        os.remove(aux_filename)

    # open PDF with platform-specific command
    if platform.system().lower() == 'darwin':
        subprocess.run(['open', pdf_filename])
    elif platform.system().lower() == 'windows':
        os.startfile(pdf_filename)
    elif platform.system().lower() == 'linux':
        subprocess.run(['xdg-open', pdf_filename])
    else:
        raise RuntimeError('Unknown operating system "{}"'.format(platform.system()))

    return pdf_filename
