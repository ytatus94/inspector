import dash
import os
import shutil
from dash import Dash, html, dcc
# from dash_extensions.enrich import DashProxy, MultiplexerTransform
from src.utils.open_browser import open_browser
from threading import Timer


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(
    __name__,
    external_stylesheets=external_stylesheets,
    use_pages=True,
    suppress_callback_exceptions=True,
)

# app = DashProxy(
#     __name__,
#     external_stylesheets=external_stylesheets,
#     use_pages=True,
#     suppress_callback_exceptions=True,
#     prevent_initial_callbacks=True,
#     transforms=[MultiplexerTransform()]
# )

app.layout = html.Div(children=[
    dcc.Store(id='store-cloud-setting', storage_type='session'),
    # dcc.Store(id='metadata-model-layer-dataframe', storage_type='session'),
    # dcc.Store(id='df-apni-results-ai', storage_type='session'),
    # dcc.Store(id='df-apni-results-tr', storage_type='session'),
    dash.page_container
])

if __name__ == '__main__':
    # If the temp directory exists, then delete it.
    if os.path.exists('temp/'):
#        shutil.rmtree('temp/')
        print('temp/ directory exists')

    Timer(1, open_browser).start()
    app.run_server(debug=True, port=8050)


