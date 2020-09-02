import copy;
import os;
import pathlib;

import commonmark;
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
# knob_svg = _util.get_file_contents_str("./img/tommytofu/knob.svg");


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
      # "knob": knob_svg,
      "keys_octave_1": keys_svg,
      "keys_octave_2": keys_svg,
      "keys_octave_3": keys_svg,
   };

   template_file = (projects_src_dir / "synth.mustache");

   return (content_dct, template_file,);
# fed

pinephone_css = projects_css_lst;
pinephone_css.append({"cssname": "/css/projects-pinephone.css",});

pinephone_js = projects_js_lst;
pinephone_js.append({"scriptname": "/js/pinephone.js",});

@app_bp.route("/projects/hw/pinephone", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone.html", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= pinephone_css,
   js_lst= projects_js_lst,
   title= "Pine64: PinePhone (www.tommypkeane.com)",
   description= "Index page for articles written by Tommy P. Keane about using and developing-for the Pine64 PinePhone.",
   author= site_author,
)
def page_pinephone(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   content_dct = {
      "articles": [
         {
            "page_link": "/projects/hw/pinephone/hardware",
            "img_src": "",
            "img_alt": "PinePhone Hardware",
            "card_title": "Hardware",
            "card_desc": "An article with details about the PinePhone hardware that we have access to.",
         },
         {
            "page_link": "/projects/hw/pinephone/os-manjaro-phosh",
            "img_src": "",
            "img_alt": "Manjaro",
            "card_title": "OS: Manjaro (Phosh)",
            "card_desc": "An article about setting-up and configuring the Phosh variant of Manjaro-ARM as the Operating System for the PinePhone.",
         },
      ],
   };

   template_file = (projects_src_dir / "pinephone" / "index.mustache");

   return (content_dct, template_file,);
# fed

@app_bp.route("/projects/hw/pinephone/hardware", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone/hardware.html", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone/hardware.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= pinephone_css,
   js_lst= projects_js_lst,
   title= "Pine64: PinePhone (www.tommypkeane.com)",
   description= "Article written by Tommy P. Keane, detailing the Hardware configuration and features of the Pine64 PinePhone.",
   author= site_author,
)
def page_pinephone_hardware(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   content_file = (projects_src_dir / "pinephone" / "hardware.md")

   parser_obj = commonmark.Parser();
   html_renderer = commonmark.HtmlRenderer();
   ast_obj = None;

   with open(content_file, "r") as file_obj:
      ast_obj = parser_obj.parse(
         file_obj.read(),
      );
   # htiw

   content_dct = {
      "main_contents": html_renderer.render(ast_obj),
   };

   template_file = (projects_src_dir / "pinephone" / "base.mustache");

   return (content_dct, template_file,);
# fed

@app_bp.route("/projects/hw/pinephone/os-manjaro-phosh", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone/os-manjaro-phosh.html", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone/os-manjaro-phosh.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= pinephone_css,
   js_lst= projects_js_lst,
   title= "PinePhone: Manjaro Phosh (www.tommypkeane.com)",
   description= "Article written by Tommy P. Keane, detailing the Hardware configuration and features of the Pine64 PinePhone running the Majaro ARM Phosh Linux-variant.",
   author= site_author,
)
def page_pinephone_os_manjaro_phosh(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   content_file = (projects_src_dir / "pinephone" / "manjaro-arm-phosh-alpha2.md")

   parser_obj = commonmark.Parser();
   html_renderer = commonmark.HtmlRenderer();
   ast_obj = None;

   with open(content_file, "r") as file_obj:
      ast_obj = parser_obj.parse(
         file_obj.read(),
      );
   # htiw

   content_dct = {
      "main_contents": html_renderer.render(ast_obj),
   };

   template_file = (projects_src_dir / "pinephone" / "base.mustache");

   return (content_dct, template_file,);
# fed


