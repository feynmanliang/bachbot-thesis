import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

from math import sqrt

matplotlib.use('pgf')
SPINE_COLOR = 'gray'
TEXT_WIDTH_IN = 6.20081968504

def latexify(fig_width=None, fig_height=None, columns=1, tick_labelsize=8):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = (3.39/6.9)*TEXT_WIDTH_IN if columns==1 else TEXT_WIDTH_IN # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    MAX_HEIGHT_INCHES = 8.0
    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large:" + str(fig_height) +
              "so will reduce to" + str(MAX_HEIGHT_INCHES) + "inches.")
        fig_height = MAX_HEIGHT_INCHES

    pgf_with_latex = {                      # setup matplotlib to use latex for output
        "pgf.texsystem": "xelatex",           # change this if using xetex or lautex
        "text.usetex": True,                # use LaTeX to write all text
        "font.family": "serif",
        "font.serif": [],                   # blank entries should cause plots to inherit fonts from the document
        "font.sans-serif": [],
        "font.monospace": [],
        "axes.labelsize": 10,               # LaTeX default is 10pt font.
        "font.size": 10,
        "legend.fontsize": 8,               # Make the legend/label fonts a little smaller
        "xtick.labelsize": tick_labelsize,
        "ytick.labelsize": tick_labelsize,
        'figure.figsize': [fig_width,fig_height],
        'text.latex.preamble': ['\usepackage{gensymb}'],
        "pgf.preamble": [
            r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts becasue your computer can handle it :)
            r"\usepackage[T1]{fontenc}",        # plots will be generated using this preamble
        ]
    }
    matplotlib.rcParams.update(pgf_with_latex)

def format_axes(ax):
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)

    return ax
