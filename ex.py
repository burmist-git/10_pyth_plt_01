#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Fri Dec  4 13:54:00 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.

'''

import numpy as np
import math
import matplotlib.pyplot as plt

def printinfo(func):
    def wrapper():
        print("")
        print("Simple reminder-training example. Function name : {} --> ".format(func.__name__))
        func()
    return wrapper

@printinfo
def plot_errorbar():
    fig = plt.figure()
    x = np.arange(10)
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 10)
    
    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
    
    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
    
    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                 label='uplims=True, lolims=True')
    
    upperlimits = [True, False] * 5
    lowerlimits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
                 label='subsets of uplims and lolims')
    
    plt.legend(loc='lower right')    
    
    plt.show()

@printinfo
def plot_scatter():
    
    np.random.seed(19680801)
    x = np.random.random(100)*5
    y = np.random.random(100)*5

    fig = plt.figure(num=None, figsize=None, dpi=None, facecolor=None,
                     edgecolor=None, frameon=True, clear=False)
    ax = fig.add_axes([0.1, 0.1, 0.85, 0.85])
    
    plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None,
                vmin=None, vmax=None, alpha=None, linewidths=None,
                edgecolors=None, plotnonfinite=False, data=None)

    plt.title('The title')
    plt.xlim(-0.5, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.xlabel('The x lable')
    plt.ylabel('The y lable')
    plt.show()
    
def main():
    plot_errorbar()
    plot_scatter()
    
if __name__ == "__main__":
    main()
