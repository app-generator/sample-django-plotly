from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from plotly.offline import plot
import plotly.graph_objects as go


# Create your views here.

# Injects data processed by Plotly
@login_required
def index(request):
    """
    View demonstrating how to display a graph object
    on a web page with Plotly. 
    """

    # Generating some data for plots.
    x = [i for i in range(-10, 11)]
    y1 = [3 * i for i in x]
    y2 = [i ** 2 for i in x]
    y3 = [10 * abs(i) for i in x]

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []

    # Adding linear plot of y1 vs. x.
    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

    # Adding scatter plot of y2 vs. x. 
    # Size of markers defined by y2 value.
    graphs.append(
        go.Scatter(x=x, y=y2, mode='markers', opacity=0.8,
                   marker_size=y2, name='Scatter y2')
    )

    # Adding bar plot of y3 vs x.
    graphs.append(
        go.Bar(x=x, y=y3, name='Bar y3')
    )

    # Setting layout of the figure.
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout},
                    output_type='div')

    return render(request, 'charts/dashboard.html',
                  context={'plot_div': plot_div, 'segment': 'plotly',
                           'prof': request.user})

