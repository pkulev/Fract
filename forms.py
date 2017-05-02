from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField
from wtforms.validators import DataRequired


class FractalArgumentsForm(FlaskForm):
    depth = IntegerField("depth")
    program = StringField("program")
    rule1 = StringField("rule 1")
    rule2 = StringField("rule 2")
    rule3 = StringField("rule 3")
    # TODO: add some else
    start_angle = FloatField("start angle")
    delta_angle = FloatField("delta angle")
    step = IntegerField("step")
