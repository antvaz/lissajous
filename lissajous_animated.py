from numpy import sin,pi,linspace
from pylab import plot,show,subplot
import matplotlib as mpl
import matplotlib.pyplot as plt
from ipywidgets import interact,interactive,fixed,interact_manual
import ipywidgets as widgets

t = linspace(-4*pi,4*pi,300);

fig, axs = plt.subplots(2, 2,figsize=(10,10))
def lissajous(A,B,wa,wb,delta):
    x=A*sin(wa* t + delta)
    y=B*sin(wb * t)
    plt.plot(x,y)
  

interact(lissajous,A=1,B=1,wa=widgets.IntSlider(min=1, max=4, step=1),wb=widgets.IntSlider(min=1, max=4, step=1),
         delta=widgets.IntSlider(min=-6, max=6, step=1))
