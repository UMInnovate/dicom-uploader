import os
import random
import csv
import json
import time
import subprocess
from flask import (
    Flask,
    flash,
    request,
    redirect,
    render_template,
    jsonify,
    make_response,
)
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(["dcm", "stl", "jpg"])

# the only paths you should need to change below are "rootfile", "extensionpath", and "slicerPath"
rootfile = "C:/UM_Innovate"
inputfile = rootfile + "/storage/dicom/"
outputfile = rootfile + "/storage/obj/"
pinfile = rootfile + "/storage/pins.csv"
extensionpath = "C:/UM_Innovate/dicom-visualizer-slicer/DICOM2OBJ/DICOM2OBJ.py"
slicerPath = r"C:\Users\mgarg\AppData\Local\NA-MIC\Slicer 4.11.0-2020-07-14"
# max file size is in MB
maxfilesize = 500

env = os.environ
newpath = {"PATH": slicerPath}
env.update(newpath)


def openfile():
    f = open(pinfile, "r")
    pinread = []
    for k in csv.reader(f):
        pinread.append(k)
    f.close()
    return pinread


def writefile(txt):
    f = open(pinfile, "a", newline="")
    pinwrite = csv.writer(f)
    pinwrite.writerow(txt)
    f.close


def randomPin():
    pinsize = 6
    pinarr = ""
    for i in range(pinsize):
        pinarr += str(random.randint(0, 9))
    if [pinarr] not in openfile():
        return pinarr
    else:
        if len(openfile()) != 10 ** pinsize:
            print("used pin")
            return randomPin()
        else:
            # below MUST be replaced with an actual method for when all pins are used up
            print("all pins used, must delete something")
            exit(0)


def folderIncrement():
    curr = randomPin()
    # TEST COMMENT START
    UPLOAD_FOLDER = inputfile + curr
    os.mkdir(UPLOAD_FOLDER)
    os.mkdir(outputfile + curr)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    # TEST COMMENT END
    return curr


app = Flask(__name__)
app.secret_key = "secret key"


def allowed_file(filename):
    checkForExtension = "." in filename
    checkExtension = False
    if checkForExtension:
        checkExtension = filename.rsplit(
            ".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return checkForExtension and checkExtension


@app.route("/index.html")
@app.route("/")
def upload_form_dicom():
    return render_template("index.html", maxfilesize=maxfilesize)


@app.route("/", methods=["GET", "POST"])
def upload_file_dicom():
    if request.method == "POST":
        if "files[]" not in request.files:
            flash("No file part")
            return redirect(request.url)
        files = request.files.getlist("files[]")
        goahead = True
        pin = ""
        for f in files:
            filename = secure_filename(f.filename)
            if not allowed_file(filename):
                goahead = False
        if goahead and request.content_length <= maxfilesize * (2 ** 20):
            pin = folderIncrement()
            # TEST COMMENT START
            writefile([pin])
            for f in files:
                f.save(os.path.join(app.config["UPLOAD_FOLDER"], f.filename))
            cmd = [
                "Slicer",
                "--no-main-window",
                "--no-splash",
                "--python-script",
                extensionpath,
                "-i",
                inputfile + pin + "/",
                "-o",
                outputfile + pin + "/",
                "-n",
                request.form.get("min_thresh"),
                "-x",
                request.form.get("max_thresh")
            ]
            subprocess.run(cmd, shell=True, env=env)
            # TEST COMMENT END
            return render_template("success.html", pin=pin)
        else:
            return render_template("failure.html", maxfilesize=maxfilesize)
