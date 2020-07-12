import copy;

import flask;

from . import (
   _base,
   _util,
   http_request,
);


app_bp = flask.Blueprint("static_files", __name__);


@app_bp.route("/img/<path:path>", methods=["GET",])
def get_static_img(path):
   """Provide the static image files when requested.
   """
   response_obj = flask.send_from_directory("img", path);
   return (response_obj);
# fed


@app_bp.route("/js/<path:path>", methods=["GET",])
def get_static_js(path):
   """Provide the static JavaScript files when requested.
   """
   response_obj = flask.send_from_directory("js", path);
   return (response_obj);
# fed


@app_bp.route("/css/<path:path>", methods=["GET",])
def get_static_css(path):
   """Provide the static CSS files when requested.
   """
   response_obj = flask.send_from_directory("css", path);
   return (response_obj);
# fed


@app_bp.route("/fonts/<path:path>", methods=["GET",])
def get_static_font(path):
   """Provide the static Font (Typeface) files when requested.
   """
   response_obj = flask.send_from_directory("fonts", path);
   return (response_obj);
# fed


@app_bp.route("/photos/<path:path>", methods=["GET",])
def get_static_photo(path):
   """Provide the static Photography images when requested.
   """
   response_obj = flask.send_from_directory("photos", path);
   return (response_obj);
# fed
