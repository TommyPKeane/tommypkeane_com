import copy;
import os;
import pathlib;

import flask;

from . import (
   _base,
   _util,
   http_request,
);


app_bp = flask.Blueprint("projects", __name__);

projects_src_dir = pathlib.Path("./src/templates/projects/");

projects_css_lst = [
   {"cssname": "/js/libs/highlight/styles/default.css",},
   {"cssname": "/css/highlight.css",},
   {"cssname": "/css/projects.css",},
   # {"cssname": "/css/projects-light.css",},
   # {"cssname": "/css/projects-dark.css",},
];

projects_js_lst = [
   {"scriptname": "/js/libs/highlight/highlight.pack.js",},
   {"scriptname": "/js/libs/highlight-plugins/linenumbers/highlightjs-line-numbers.min.js",},
   {"scriptname": "/js/projects.js",},
];

projects_desc = (
   "An projects page by Tommy P. Keane for continuous-education and infotainment purposes."
);

site_author = "Tommy P. Keane";

keys_svg = _util.get_file_contents_str("./img/tommylogos/music-piano-octave.svg");
knob_svg = _util.get_file_contents_str("./img/tommytofu/knob.svg");


@app_bp.route("/projects", methods=["GET",],)
@app_bp.route("/projects.html", methods=["GET",],)
@app_bp.route("/projects.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= projects_css_lst,
   js_lst= projects_js_lst,
   title= "Projects (www.tommypkeane.com)",
   description= "Overview of personal projects undertaken by Tommy P. Keane.",
   author= site_author,
)
def page_projects(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   return (None);
# fed


synth_css = projects_css_lst;
synth_css.append({"cssname": "/css/projects-synth.css",});

synth_js = projects_js_lst;
synth_js.append({"scriptname": "/js/synth.js",});

@app_bp.route("/projects/synth", methods=["GET",],)
@app_bp.route("/projects/synth.html", methods=["GET",],)
@app_bp.route("/projects/synth.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= synth_css,
   js_lst= projects_js_lst,
   title= "Synthesizer (www.tommypkeane.com)",
   description= "An interactive online Synthesizer developed by Tommy P. Keane, using the Web Audio API.",
   author= site_author,
)
def page_synth(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   content_dct = {
      "knob": knob_svg,
      "keys_octave_1": keys_svg,
      "keys_octave_2": keys_svg,
      "keys_octave_3": keys_svg,
   };

   template_file = (projects_src_dir / "synth.mustache");

   return (content_dct, template_file,);
# fed

