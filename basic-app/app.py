from shiny import render, ui
from shiny.express import *

ui.panel_title("Progress-kitty!")


with ui.layout_columns(col_widths= [3,3,3,3]):
    with ui.card():
        "task 1"
        ui.input_slider("n1", "N", 0, 100, 0)
        @render.text
        def txt1():
            return f"this task is about {input.n1()}% done"
    with ui.card():
        "card 2"
        ui.input_slider("n2", "N", 0, 100, 0)
        @render.text
        def txt2():
            return f"this task is about {input.n2()}% done"
    with ui.card():
        "card 3"
        ui.input_slider("n3", "N", 0, 100, 0)
        @render.text
        def txt3():
            return f"this task is about {input.n3()}% done"
    with ui.card():
        "card 4"
        ui.input_slider("n4", "N", 0, 100, 0)
        @render.text
        def txt4():
            return f"this task is about {input.n4()}% done"
