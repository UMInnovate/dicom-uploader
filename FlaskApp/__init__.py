import os
import random
import csv
import json
import time
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

# import sys
# print(sys.version)

ALLOWED_EXTENSIONS = set(["obj"])

# REMEMBER TO CHANGE THIS BACK TO "/var/www"!!!
rootfile = "/var/www"
pinfile = rootfile + "/storage/pins.csv"
# max file size is in MB
maxfilesize = 500


def openfile():
    f = open(pinfile, 'r')
    pinread = []
    for k in csv.reader(f):
        pinread.append(k)
    f.close()
    return pinread


def writefile(txt):
    f = open(pinfile, 'a')
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
        if len(openfile()) != 10**pinsize:
            print("used pin")
            return randomPin()
        else:
            # below MUST be replaced with an actual method for when all pins are used up
            print("all pins used, must delete something")
            exit(0)


def folderIncrement():
    curr = randomPin()
    # TEST COMMENT START
    UPLOAD_FOLDER = rootfile + "/storage/obj/" + curr
    os.mkdir(UPLOAD_FOLDER)
    # os.mkdir(rootfile + "/storage/obj/" + curr)
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


# for future functionality, replace "/" with "/{route_to_dicom}" below
@app.route("/")
def upload_form_dicom():
    return render_template("index.html", maxfilesize=maxfilesize)

# for future functionality, uncomment (and replace "/art_history" with "/{route_to_art_history}") below
# @app.route("/art_history")
# def upload_form_art_history():
#     return render_template("index_future.html")


# for future functionality, replace "/" with "/{route_to_dicom}" below
@app.route("/", methods=["GET", "POST"])
def upload_file_dicom():
    if request.method == "POST":
        # time.sleep(3)  # ONLY FOR TESTING!! PLEASE REMOVE ON DEPLOYMENT!!!
        # check if the post request has the files part
        print(request.content_length, maxfilesize)
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
        if goahead and request.content_length <= maxfilesize * (2**20):
            pin = folderIncrement()
            # TEST COMMENT START
            writefile([pin])
            for f in files:
                f.save(os.path.join(
                    app.config["UPLOAD_FOLDER"], filename))
            # TEST COMMENT END
        else:
            return render_template("failure.html", maxfilesize=maxfilesize)
        # if i == (len(files) - 1):
        #     S.run("Z:\Slicer 4.11.0-2020-03-24\Slicer.exe", shell=True)
        return render_template("success.html", pin=pin)


# for future functionality, uncomment (and replace "/art_history" with "/{route_to_art_history}") below
# @app.route("/art_history", methods=["GET", "POST"])
# def upload_file_art_history():
#     if request.method == "POST":
#         # time.sleep(3)  # ONLY FOR TESTING!! PLEASE REMOVE ON DEPLOYMENT!!!
#         pin = folderIncrement()
#         # TEST COMMENT START
#         writefile([pin])
#         data = dict({"pin": pin, "models": []})
#         # check if the post request has the files part
#         quantity = int(request.form["quantity"])
#         for i in range(quantity):
#             modeldata = dict()
#             curr = str(i)
#             if "files" + curr + "[]" not in request.files:
#                 flash("No file part")
#                 return redirect(request.url)
#             files = request.files.getlist("files" + curr + "[]")
#             cap = request.form.get("caption" + curr)
#             if cap is not None:
#                 modeldata.update({"caption": cap, "files": []})
#             for i in range(len(files)):
#                 #     # if file and allowed_file(file.filename):
#                 filename = secure_filename(files[i].filename)
#                 files[i].save(os.path.join(
#                     app.config["UPLOAD_FOLDER"], filename))
#                 modeldata["files"].append(filename)
#             data["models"].append(modeldata)
#             # if i == (len(files) - 1):
#             #     S.run("Z:\Slicer 4.11.0-2020-03-24\Slicer.exe", shell=True)
#         with open(os.path.join(app.config["UPLOAD_FOLDER"], pin + ".json"), "w") as jsonfile:
#             json.dump(data, jsonfile, indent=2)
#         # TEST COMMENT END
#         return render_template("success.html", pin=pin)
