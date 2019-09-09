'''Module for visualisation features'''

import matplotlib.pyplot as plt
import seaborn as sb
import typing
import model as mod

from typing import List


def createPlot(r: int=1, c: int=1, title: List=[""],
                figsize: List=[14.7,8.27], xlabel: str="", ylabel: str="",
                axis_font: int=14, title_font: int=16, tick_font: int=14,
                fontweight: str='bold', sharex: bool=False,
                sharey: bool=False) -> List:
    '''
    Sets up plot axis according to params.
    Precondition: len(title) == r*c
    '''
    _, axs = plt.subplots(r, c, figsize=figsize, sharex=sharex, sharey=sharey);

    if r == 1 and c == 1:
        axs = [axs]
    else:
        axs = axs.flatten()

    for i, ax in enumerate(axs):
        ax.set_title(label=title[i], fontsize=title_font, fontweight=fontweight);
        ax.set_xlabel(xlabel, fontsize=axis_font);
        ax.set_ylabel(ylabel, fontsize=axis_font);
        plt.xticks(fontsize=tick_font);
        plt.yticks(fontsize=tick_font);

    return axs

def plotROC(X, y, theta, thresholds, **kwargs):
    '''Plots the ROC (Received Operator Characterstic) curve'''
    tpr, fpr = [], []
    for t in thresholds:
        predictions = mod.predict(X, theta, threshold=t)
        cnf = mod.confMatrix(predictions, y)

        tpr.append(cnf[1][1]/(cnf[1][1]+cnf[1][0]))
        fpr.append(cnf[0][1]/(cnf[0][1]+cnf[0][0]))

    createPlot(title=["Receiving Operator Characterstic Curve"],
                xlabel='False Positive Rate',
                ylabel='True Positive Rate', **kwargs);

    sb.regplot(x=fpr, y=tpr, scatter_kws={'alpha':0.5});
    plt.xlim(0,1);
    plt.ylim(0,1);
