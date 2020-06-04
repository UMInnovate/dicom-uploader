import os
import urllib.request
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


def folderIncrement():
    curr = 0
    folders = os.walk("uploads/")
    for i, j, k in folders:
        if len(j) > 0:
            curr = int(max(j)) + 1
    UPLOAD_FOLDER = "uploads/" + str(curr)
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
        # flash("File(s) successfully uploaded! Please enter " +
        #       str(pin) + " on your Magic Leap headset.")

        return render_template("upload3.html", pin=pin)


if __name__ == "__main__":
    app.run()
