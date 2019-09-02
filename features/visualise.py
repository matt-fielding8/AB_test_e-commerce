'''Module for visualisation features'''

import matplotlib.pyplot as plt
import seaborn as sb


def createPlot(title="", figsize=[14.7,8.27], xlabel="", ylabel="",
                axis_font=14, title_font=16, tick_font=14, fontweight='bold'):
    '''Sets up plot axis according to params'''
    _, ax = plt.subplots(figsize=figsize);
    ax.set_title(label=title, fontsize=title_font, fontweight=fontweight);
    ax.set_xlabel(xlabel, fontsize=axis_font);
    ax.set_ylabel(ylabel, fontsize=axis_font);
    plt.xticks(fontsize=tick_font);
    plt.yticks(fontsize=tick_font);
