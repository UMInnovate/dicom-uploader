# How to set up

## Getting all dependencies

If you use `conda`,

1. cd into this directory.
1. run `conda create --prefix ./env --file requirements.txt` and complete the associated prompts to install most dependencies
1. run `conda activate ./env` to activate the environment.
1. Once environment is active, run `pip install flask-wtf wtforms` to install the right versions of the form-making library.

If you use pip,

1. run `pip3 install -r requirements2.txt`

## To run the app locally

### Windows

I'm still working on moving the web form to a server that it can live on, but for development purposes, you can use `flask run` to set up a local instance at [`https:\\localhost:5000`](https:\localhost:5000).

# Starting Web Form locally on Windows

1. Install python (check: type "python" in terminal)
2. Install Flask (type "pip install flask" in terminal)
3. Navigate to directory with flask app
4. Set flask app script (type "set FLASK_APP=main.py" in terminal)
5. Run flask app locally (type: "flask run" in terminal)
6. Navigate to "http://localhost:5000" in browser address bar

# Starting GitAutoPush

1. Move the bash to a directory outside of git repo
2. Run gitautopush
