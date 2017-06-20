#!/usr/bin/env python

import argparse

from flask import Flask, redirect, render_template, url_for

import pilfract
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
    path = "static/output.png"
    form = FractalArgumentsForm()
    if form.validate_on_submit():
        args = argparse.Namespace(
            depth=form.depth.data,
            program=form.program.data,
            rules=form.rules.data,
            start_angle=form.start_angle.data,
            delta_angle=form.delta_angle.data,
            step=form.step.data,
            view=False, output=path)

        pilfract.main(args)
        return render_template("fractal.html", path=path)
    return render_template("index.html", form=form)


app.run("0.0.0.0", 8080)
