import bokeh
from bokeh.models import ColumnDataSource
from bokeh.io import curdoc
from bokeh.plotting import figure

from datetime import datetime
import requests
import time

data_source = ColumnDataSource(data = {"close": [], "DateTime": []})

# create the line chart
fig = figure(x_axis_type="datetime",
             plot_width=900, plot_height=450,
             title=" __ (every 10 seconds)")

fig.line(x="DateTime", y="cpm", line_color="tomato",
         line_width=3.0, source=data_source)

fig.xaxis.axis_label = "Date Time"
fig.yaxis.axis_label = "cpm"

# define callbacks
def update_chart():
    global data_source
    resp = requests.get()
    hist_data = resp.json()
    new_row = {" ": [hist_data["cpm"],], "DateTime": [datetime.now(),]}
    data_source.stream(new_row)

# # update the stream data
# from bokeh.io import push_notebook
# while True:
#     resp = requests.get(url)
#     hist_data = resp.json()
#     new_row = {"Radioactivity": [hist_data["cpm"],], "DateTime": [datetime.now(),]}
#     data_source.stream(new_row)
#     push_notebook(handle=handle_line_chart)
#     time.sleep(10)

curdoc().add_periodic_callback(update_chart, 10000)
curdoc().add_root(fig)