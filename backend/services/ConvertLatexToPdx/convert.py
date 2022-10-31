# Store this code in 'app.py' file
import pathlib
import stat

from flask import Flask, request
import os, subprocess, platform

app = Flask(__name__)


@app.route('/convert', methods=['GET'])
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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
