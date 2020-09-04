import copy;
import pathlib;

import flask;

from . import (
   _base,
   _util,
   http_request,
);


app_bp = flask.Blueprint("main", __name__);

main_src_pth = pathlib.Path("./src/templates/");

main_css_lst = [
   # { "cssname": "/js/libs/highlight/styles/default.css", "mode": _base.MODE_ANY, },
];

main_js_lst = [
   # {"scriptname": "/js/libs/highlight/highlight.pack.js",},
];

main_desc = (
   "Landing Page for www.tommypkeane.com, website of Tommy P. Keane, Data-Scientist and Software-Engineer."
);

site_author = "Tommy P. Keane";


@app_bp.route("/", methods=["GET",],)
@app_bp.route("/index", methods=["GET",],)
@app_bp.route("/index.html", methods=["GET",],)
@app_bp.route("/index.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= main_css_lst,
   js_lst= main_js_lst,
   title= "Tommy P. Keane - Professional Website",
   description= main_desc,
   author= site_author,
)
def ep_intro(theme_class,):
   """Provide the Main Landing Page Response
   """
   content_dct = dict();
   template_file = (main_src_pth / "index.mustache");

   return (content_dct, template_file,);
# fed
