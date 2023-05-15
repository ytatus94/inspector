import plotly.express as px
import plotly.graph_objects as go


def plot_timeseries(df, x, y, title):
    figure = px.line(
        df,
        x=x,
        y=y,
        title=title,
    )
    figure.update_layout(hovermode='x unified')
    # print('figure should be ready')

    return figure


def plot_bar_chart(df, x, y, title):
    figure = px.bar(
        df,
        x=x,
        y=y,
        title=title,
    )
    figure.update_layout(hovermode='x unified')
    # print('figure should be ready')

    return figure


