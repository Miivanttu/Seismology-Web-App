import random
from flask import Blueprint, render_template
from bokeh.embed import components
from bokeh.plotting import figure
import numpy as np

graph = Blueprint('graph', __name__)

@graph.route('/graph')
def drawGraph():
    # Generate synthetic data
    x = np.linspace(0, 10, 50)  # Independent variable
    y = 2.5 * x + np.random.normal(0, 3, size=50)  # Dependent variable with noise

    # Fit a linear regression model
    m, b = np.polyfit(x, y, 1)  # Slope (m) and intercept (b)
    y_pred = m * x + b  # Predicted y values based on the regression line

    # Create a Bokeh figure
    plot = figure(title="Regression Analysis", x_axis_label="Taandatud kaugus, m/√kg", y_axis_label="Võnkekiirus, mm/s")
    plot.scatter(x, y, size=10, color="blue", alpha=0.7, legend_label="Data Points")
    plot.line(x, y_pred, color="red", line_width=2, legend_label=f"Regression Line: y = {m:.2f}x + {b:.2f}")

    plot.legend.location = "top_left"

    # Generate script and div for embedding
    script, div = components(plot)
    return render_template("graph.html", script=script, div=div)
