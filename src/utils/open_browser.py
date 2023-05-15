import os
import webbrowser


def open_browser():
    port = 8050
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new("http://localhost:{}".format(port))


