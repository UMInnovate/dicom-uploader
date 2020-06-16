# Flask Uploader Form

**This is a test**

## Setting up the environment

### The short way

Using `conda` you can run the following command:

```bash
conda create --prefix ./env --file package-list.txt
```

After you follow the prompts, you can activate your environment using the following command:

```bash
conda activate ./env/
```

And you can deactivate your environment using:

```bash
conda deactivate
```

### The slightly longer way

If you want to install things yourself using conda you can start with a fresh environment:

```bash
conda create --prefix ./env python=3.7
```

This script will create an environment on your local machine inside the current folder. To activate the environment you can run this command: `conda activate ./env/`.

(Once you're done working on stuff in this repo, I recommend deactivating the environment using: `conda deactivate`.)

As of right now the most important package we're using is `flask`. To install flask on the environment you can run the following code once your environment is active:

```
conda install flask
```

### Other ways

If you use pip, you can check the `requirements.txt` file for what to install.

If you use another virtual environment management tool, one of these two files (package-list.txt or requirements.txt) should help you on your way.

If you don't use a virtual environment, today's a good day to start. It makes keeping versions of code consistent across machines and time.

## To run the app locally

With your environment active, run the following in your terminal:

```bash
export set FLASK_APP=main.py
```

This points the logic of the flask app to run from `main.py` instead of the default `app.py`. By including both export and set, you get around the UNIX/Windows differences (one of my future TODOs is to get rid of this extra step).

To run the app locally in a dev environment all you need to do now is type this command:

```bash
flask run
```

And go to the following URL in a browser: [`http://localhost:5000`](http://localhost:5000).
