#!/usr/bin/env python

from flask import Flask, redirect, render_template, url_for

from forms import FractalArgumentsForm


app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.secret_key = app.config["WTF_CSRF_SECRET_KEY"]


@app.route("/")
@app.route("/index")
def index():
    return redirect(url_for("submit"))


@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = FractalArgumentsForm()
    if form.validate_on_submit():
        import main, sys
        sys.argv = [
            "-d", form.depth.data,
            "-p", form.program.data,
            "-r", form.rule1.data,  # TODO FIXME: oh my
            "-sa", form.start_angle.data,
            "-da", form.delta_angle.data,
            "-s", form.step.data,
        ]

        main.main()
        
        return redirect("/success")
    return render_template("index.html", form=form)


@app.route("/success")
def success():
    return "<img src='templates/output.png'>Fooraqtal</img>"


app.run("0.0.0.0", 8080)
