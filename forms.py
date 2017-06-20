from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField
from wtforms.validators import DataRequired


class FractalArgumentsForm(FlaskForm):
    depth = IntegerField("depth")
    program = StringField("program")
    rules = StringField("rules")
    start_angle = FloatField("start angle")
    delta_angle = FloatField("delta angle")
    step = IntegerField("step")
