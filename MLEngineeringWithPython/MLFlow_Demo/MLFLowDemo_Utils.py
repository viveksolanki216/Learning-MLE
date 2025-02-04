import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
cm = plt.cm.RdBu

# It lists and defines all utilities for the MLFlow Demo
# Function to plot decision boundry, restricted to 2-d plots ie 2 features
def plot_decision_boundry(model,X):
    x1, x2 = np.meshgrid(np.arange(X[:,0].min() -.5, X[:,0].max() +.5 , 0.05),
                         np.arange(X[:,1].min() -.5, X[:,1].max() +.5,  0.05))
    y_plot_pred_probs = model.predict_proba(np.c_[x1.ravel(), x2.ravel()])[:,1]

    plt.contourf(x1,
                 x2,
                 y_plot_pred_probs.reshape(x1.shape), cmap=cm, alpha=.7)
    plt.xlabel('feature 1')
    plt.ylabel('feature 2')
