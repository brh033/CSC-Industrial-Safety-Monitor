# run constantly; no initial run
# 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# set colors
colors = ['#ee4d55', '#f36d54', '#fabd57', '#f6ee54', '#c7df7e', '#72c66e', '#4dab6d']

# values = [100, 80, 60, 40, 20, 0, -20, -40]
values = [210, 180, 150, 120, 90, 60, 30, 0]

x_axis_vals = [0, 0.44, 0.88, 1.32, 1.76, 2.2, 2.64]

# create the figure object
fig = plt.figure(figsize=(13,13))

ax = fig.add_subplot(projection='polar');

# create the curved bars
ax.bar(x=[0, 0.44, 0.88, 1.32, 1.76, 2.2, 2.64], 
       width=0.5, height=0.5, bottom=2,
       linewidth=3, edgecolor='white',
       color=colors, align='edge');
plt.annotate('DANGER', xy=(0.13,2.03), rotation=-76, color='white', fontweight='bold', fontsize=17);
plt.annotate('Unsustainable', xy=(0.62, 1.78), rotation=-51, color='white', fontweight='bold', fontsize=17);
plt.annotate('Maturing', xy=(1.17, 1.97), rotation=-32, color='white', fontweight='bold', fontsize=17);
plt.annotate('Developing', xy=(1.69, 2.2), color='white', fontweight='bold', fontsize=17);
plt.annotate('Foundational', xy=(2.18, 2.24), rotation=23, color='white', fontweight='bold', fontsize=17);
plt.annotate('Sustainable', xy=(2.59, 2.29), rotation=45, color='white', fontweight='bold', fontsize=17);
plt.annotate('Safe', xy=(2.96, 2.27), rotation=75, color='white', fontweight='bold', fontsize=17);

for loc, val in zip([0, 0.44, 0.88, 1.32, 1.76, 2.2, 2.64, 3.14], values):
    plt.annotate(val, xy=(loc, 2.5), ha='right' if val<=20 else 'left');

plt.annotate('50', xytext=(0,0), xy=(1.1, 2.0), 
            arrowprops=dict(arrowstyle='wedge, tail_width=0.6', color='black', shrinkA=0),
            bbox=dict(boxstyle='circle', facecolor='black', linewidth=2.0),
            fontsize=45, color='white', ha='center'
            );

plt.title('Geiger Counter', loc='center', pad=20, fontsize=35, fontweight='bold')
ax.set_axis_off()
plt.show()