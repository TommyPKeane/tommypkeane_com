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
   { "cssname": "/js/libs/highlight/styles/default.css", "mode": _base.MODE_ANY, },
   { "cssname": "/css/highlight.css",                    "mode": _base.MODE_ANY, },
   { "cssname": "/css/highlight-lite.css",               "mode": _base.MODE_LITE, },
   { "cssname": "/css/highlight-dark.css",               "mode": _base.MODE_DARK, },
   { "cssname": "/css/educational.css",                  "mode": _base.MODE_ANY, },
   { "cssname": "/css/educational-lite.css",             "mode": _base.MODE_LITE, },
   { "cssname": "/css/educational-dark.css",             "mode": _base.MODE_DARK, },
   { "cssname": "/css/educational-cpnk.css",             "mode": _base.MODE_CPNK, },
   { "cssname": "/css/educational-vapr.css",             "mode": _base.MODE_VAPR, },
];

educational_js_lst = [
   {"scriptname": "/js/libs/highlight/highlight.pack.js",},
   {"scriptname": "/js/libs/highlight-plugins/linenumbers/highlightjs-line-numbers.min.js",},
   {"scriptname": "/js/educational.js",},
];

educational_desc = (
   "An educational page by Tommy P. Keane for continuous-education and infotainment purposes."
);

site_author = "Tommy P. Keane";


@app_bp.route("/teaches", methods=["GET",],)
@app_bp.route("/articles", methods=["GET",],)
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
def educational(theme_class):
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
def edu_gtlt_ttt(theme_class):
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
def edu_py_functions(theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "python-functions.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed

@app_bp.route("/educational/python/classes", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "Educational - Python Classes",
   description= educational_desc,
   author= site_author,
)
def edu_py_classes(theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "python-classes.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed


@app_bp.route("/educational/d3.js/shapes", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "Educational - D3.js Basic Shapes",
   description= educational_desc,
   author= site_author,
)
def edu_d3js_shapes(theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "d3js-shapes.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed


@app_bp.route("/educational/linguistics/en-spelling", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "Educational - English - Spelling",
   description= educational_desc,
   author= site_author,
)
def edu_lang_en_spelling(theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "linguistics-en-spelling.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed


@app_bp.route("/educational/webdev/fail2ban", methods=["GET",],)
@http_request.html_response(
   css_lst= educational_css_lst,
   js_lst= educational_js_lst,
   title= "Educational - Web Development - fail2ban",
   description= educational_desc,
   author= site_author,
)
def edu_webdev_fail2ban(theme_class):
   """aksldjaskdj
   """

   yaml_content, template_file = http_request.parse_content_config(
      os.path.join(educational_src_dir, "webdev-fail2ban.yaml",)
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed
