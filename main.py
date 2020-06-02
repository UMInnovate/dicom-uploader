import os
import urllib.request
from app import app
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
        flash("File(s) successfully uploaded! Please reload page to reupload~")

        return redirect("/")


if __name__ == "__main__":
    app.run()

# TODO compress main and app into one file.
# TODO redo README documentation
