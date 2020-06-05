import os
import urllib.request
import random
import csv
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

ALLOWED_EXTENSIONS = set(["dcm", "png", "jpg"])


def openfile():
    f = open("pins.csv", 'r')
    pinread = []
    for k in csv.reader(f):
        pinread.append(k)
    f.close()
    return pinread


def writefile(txt):
    f = open("pins.csv", 'a', newline='')
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
        print("used pin")
        randomPin()


def folderIncrement():
    curr = ""
    for i in randomPin():
        curr += i
    UPLOAD_FOLDER = "uploads/" + curr
    os.mkdir(UPLOAD_FOLDER)
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    return curr


app = Flask(__name__)
app.secret_key = "secret key"


def allowed_file(filename):
    checkForExtension = "." in filename
    checkExtension = filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    return checkForExtension and checkExtension


@app.route("/")
def upload_form():
    return render_template("upload.html")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        pin = folderIncrement()
        writefile([pin])
        # check if the post request has the files part
        if "files[]" not in request.files:
            flash("No file part")
            return redirect(request.url)
        files = request.files.getlist("files[]")
        for i in range(len(files)):
            # if file and allowed_file(file.filename):
            filename = secure_filename(files[i].filename)
            files[i].save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            # if i == (len(files) - 1):
            #     S.run("Z:\Slicer 4.11.0-2020-03-24\Slicer.exe", shell=True)
        return render_template("upload3.html", pin=pin)


if __name__ == "__main__":
    app.run()
