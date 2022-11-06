# Store this code in 'app.py' file
import os
import pathlib
import stat
import subprocess
import sys
import warnings
from os.path import exists

from flask import request, Blueprint, make_response, jsonify, current_app

# Suppress warnings
warnings.filterwarnings("ignore")

sys.path.append('../')

convertLatexToPdfBlueprint = Blueprint('convertLatexToPdfBlueprint', __name__)


@convertLatexToPdfBlueprint.route('/api/convertLatexToPdf', methods=['GET'])
def convertToPdf():
    # TeX source filename
    tex_filename = request.args.get('filepath')
    file_exists = exists(tex_filename)
    if file_exists:
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

        if os.path.exists(log_filename):
            os.remove(log_filename)
        if os.path.exists(aux_filename):
            os.remove(aux_filename)

        # check if PDF is successfully generated
        if not os.path.exists(pdf_filename):
            current_app.logger.info('Converted PDF file could not be found. Latex to PDF conversion failed for the '
                                    'file: ' + tex_filename)
            return make_response(jsonify('Latex to PDF conversion failed for the file: ' + tex_filename), 500)
        current_app.logger.info('Latex to PDF conversion successful for the file: ' + tex_filename)
        return make_response(jsonify(pdf_filename), 202)
    else:
        current_app.logger.info('Provided Latex filepath ' + tex_filename + ' not found.')
        return make_response(jsonify(tex_filename), 404)
