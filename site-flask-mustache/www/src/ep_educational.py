import copy;
import os;

import flask;

from . import (
   _base,
   _util,
   http_request,
);


app_bp = flask.Blueprint("educational", __name__);

educational_src_dir = "./src/templates/educational/";

educational_css_lst = [
   {"cssname": "/js/highlight/styles/default.css",},
   {"cssname": "/css/educational.css",},
   {"cssname": "/css/educational-light.css",},
   {"cssname": "/css/educational-dark.css",},
];

educational_js_lst = [
   {"scriptname": "/js/highlight/highlight.pack.js",},
   {"scriptname": "/js/educational.js",},
];

educational_desc = (
   "An educational page by Tommy P. Keane for continuous-education and infotainment purposes."
);

site_author = "Tommy P. Keane";


@app_bp.route("/educational", methods=["GET",],)
@app_bp.route("/educational.html", methods=["GET",],)
@app_bp.route("/educational.htm", methods=["GET",],)
@app_bp.route("/educational/python", methods=["GET",],)
@app_bp.route("/educational/d3js", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "Educational Pages (www.tommypkeane.com)",
   description= "Educational pages by Tommy P. Keane, for continuous-education and infotainment purposes.",
   author= site_author,
)
def educational(body_theme_class):
   """Provide the Settings (Customisation) Page.
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "educational.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed


@app_bp.route("/gtlt/ttt", methods=["GET",],)
@app_bp.route("/educational/ttt", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "gtlt - Tommy Teaches Tommy",
   description= "Tommy Teaches Tommy documents from the collection of Greater Trees Lesser Turtles publications by Tommy P. Keane",
   author= site_author,
)
def edu_gtlt_ttt(body_theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "gtlt-ttt.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed


@app_bp.route("/educational/python/functions", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "Educational - Python Functions",
   description= educational_desc,
   author= site_author,
)
def edu_py_functions(body_theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "python-functions.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed
