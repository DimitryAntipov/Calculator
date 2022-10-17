from re import X
from tkinter import Y
import model_rational
import model_kompleks
import view

def button_click_rational():
    view.help_rational()
    value_a = view.get_value()
    value_action = view.get_action()
    value_b = view.get_value()
    model_rational.init(value_a, value_b, value_action)
    if value_action == "+":
        result = model_rational.sum_rational()
    elif value_action == "-":
        result = model_rational.sub_rational()
    elif value_action == "*":
        result = model_rational.mult_rational()
    elif value_action == "/":
        result = model_rational.div_rational()
    view.view_data(result)
    model_kompleks.wrire_resalt(value_a, value_b, value_action, result)


def button_click_kompleks():
    view.help_kompleks()
    value_a = view.get_value_komp()
    value_action = view.get_action()
    value_b = view.get_value_komp()
    model_kompleks.init(value_a, value_b, value_action)
    if value_action == "+":
        result = model_kompleks.sum_kpl()
    elif value_action == "-":
        result = model_kompleks.sub_kpl()
    elif value_action == "*":
        result = model_kompleks.mult_kpl()
    elif value_action == "/":
        result = model_kompleks.div_kpl()
    view.view_data(result)
    model_kompleks.wrire_resalt(complex(value_a[0],value_a[1]), complex(value_b[0],value_b[1]), value_action, result)