# @file
# @brief Endpoints and Blueprint for Project Pages
#
# This module provides the Flask endpoints' Blueprint to support the site pages
# for different research, hardware, and software projects that we want to share
# and provide on our site.
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2020, Tommy P. Keane

import copy;
import pathlib;

import commonmark;
import flask;

from . import (
   _base,
   _util,
   _images,
   http_request,
);


app_bp = flask.Blueprint("projects", __name__);

projects_src_dir = pathlib.Path("./src/templates/projects/");

author_name = "tommypkeane"
author_name_display = "Tommy P. Keane"

projects_css_lst = [
   { "cssname": "/js/libs/highlight/styles/default.css", "mode": _base.MODE_ANY, },
   { "cssname": "/css/highlight.css", "mode": _base.MODE_ANY, },
   { "cssname": "/css/projects.css", "mode": _base.MODE_ANY, },
   # { "cssname": "/css/projects-lite.css", "mode": _base.MODE_LITE, },
   # { "cssname": "/css/projects-dark.css", "mode": _base.MODE_DARK, },
];

projects_js_lst = [
   { "scriptname": "/js/libs/highlight/highlight.pack.js", },
   { "scriptname": "/js/libs/highlight-plugins/linenumbers/highlightjs-line-numbers.min.js", },
   { "scriptname": "/js/projects.js", },
];

projects_desc = (
   "An projects page by Tommy P. Keane for continuous-education and infotainment purposes."
);

site_author = "Tommy P. Keane";

synth_img_path = pathlib.Path("./img/projects-synth/");

keys_svg = _util.get_file_contents_str(synth_img_path / "music-piano-octave-plain.svg");
computer_keyboard_svg = _util.get_file_contents_str(synth_img_path / "computer-keyboard-plain.svg");
skull_open_svg = _util.get_file_contents_str(synth_img_path / "objet_spooky_skeleton-skull_side-maw-open-00_plain.svg");
skull_clsd_svg = _util.get_file_contents_str(synth_img_path / "objet_spooky_skeleton-skull_side-maw-clsd-00_plain.svg");


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

   content_dct = {
      "articles": [
         {
            "page_link": "/projects/hw/pinephone/hardware",
            "img_src": _images.icon_data_dct["icon_raspberrypi"],
            "img_alt": "PinePhone Hardware",
            "card_title": "Hardware",
            "card_desc": "An article with details about the PinePhone hardware that we have access to.",
         },
         {
            "page_link": "/projects/hw/pinephone/os-manjaro-phosh",
            "img_src": _images.icon_data_dct["icon_pinephone"],
            "img_alt": "Manjaro",
            "card_title": "OS: Manjaro (Phosh)",
            "card_desc": (
               "An article about setting-up and configuring the Phosh variant of Manjaro-ARM"
               " as the Operating System for the PinePhone."
            ),
         },
         {
            "page_link": "/projects/webgl/threejs/intro",
            "img_src": _images.icon_data_dct["icon_photography"],
            "img_alt": "WebGL",
            "card_title": "Three.js: Introduction",
            "card_desc": (
               "A basic example of WebGL with a 3D object created in Blender, animating on a loop."
            ),
         },
      ],
   };

   template_file = (projects_src_dir / "pinephone" / "index.mustache");

   return (content_dct, template_file,);
# fed


synth_css = copy.deepcopy(projects_css_lst);
synth_css.extend(
   [
      { "cssname": "/css/projects-synth.css", "mode": _base.MODE_ANY, },
      # { "cssname": "/css/projects-synth-lite.css", "mode": _base.MODE_LITE, },
      # { "cssname": "/css/projects-synth-dark.css", "mode": _base.MODE_DARK, },
      # { "cssname": "/css/projects-synth-vapr.css", "mode": _base.MODE_VAPR, },
      # { "cssname": "/css/projects-synth-cpnk.css", "mode": _base.MODE_CPNK, },
   ]
);

synth_js = copy.deepcopy(projects_js_lst);
synth_js.append({"scriptname": "/js/synth.js",});

@app_bp.route("/projects/synth", methods=["GET",],)
@app_bp.route("/projects/synth.html", methods=["GET",],)
@app_bp.route("/projects/synth.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= synth_css,
   js_lst= synth_js,
   title= "Synthesizer (www.tommypkeane.com)",
   description= (
      f"An interactive online Synthesizer developed by {author_name_display},"
      " using the Web Audio API."
   ),
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
      "computer_keyboard": computer_keyboard_svg,
      "skull_open": skull_open_svg,
      "skull_clsd": skull_clsd_svg,
   };

   template_file = (projects_src_dir / "musics" / "synth.mustache");

   return (content_dct, template_file,);
# fed

pinephone_css = copy.deepcopy(projects_css_lst);
pinephone_css.append(
   { "cssname": "/css/projects-pinephone.css", "mode": _base.MODE_ANY, }
);

pinephone_js = copy.deepcopy(projects_js_lst);
pinephone_js.append(
   { "scriptname": "/js/pinephone.js", }
);

@app_bp.route("/projects/hw/pinephone", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone.html", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= pinephone_css,
   js_lst= pinephone_js,
   title= "Pine64: PinePhone (www.tommypkeane.com)",
   description= (
      f"Index page for articles written by {author_name_display}"
      " about using and developing-for the Pine64 PinePhone."
   ),
   author= site_author,
)
def page_pinephone(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   content_dct = {
      "articles": [
         {
            "page_link": "/projects/hw/pinephone/hardware",
            "img_src": _images.icon_data_dct["icon_raspberrypi"],
            "img_alt": "PinePhone Hardware",
            "card_title": "Hardware",
            "card_desc": "An article with details about the PinePhone hardware that we have access to.",
         },
         {
            "page_link": "/projects/hw/pinephone/os-manjaro-phosh",
            "img_src": _images.icon_data_dct["icon_pinephone"],
            "img_alt": "Manjaro",
            "card_title": "OS: Manjaro (Phosh)",
            "card_desc": (
               "An article about setting-up and configuring the Phosh variant of Manjaro-ARM"
               " as the Operating System for the PinePhone."
            ),
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
   js_lst= pinephone_js,
   title= "Pine64: PinePhone (www.tommypkeane.com)",
   description= (
      f"Article written by {author_name_display},"
      " detailing the Hardware configuration and features of the Pine64 PinePhone."
   ),
   author= site_author,
)
def page_pinephone_hardware(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   yaml_content, template_file = http_request.parse_content_config(
      projects_src_dir / "pinephone" / "hardware.yaml"
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed

@app_bp.route("/projects/hw/pinephone/os-manjaro-phosh", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone/os-manjaro-phosh.html", methods=["GET",],)
@app_bp.route("/projects/hw/pinephone/os-manjaro-phosh.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= pinephone_css,
   js_lst= pinephone_js,
   title= "PinePhone: Manjaro Phosh (www.tommypkeane.com)",
   description= (
      f"Article written by {author_name_display},"
      " detailing the Hardware configuration and features of"
      " the Pine64 PinePhone running the Majaro ARM Phosh Linux-variant."
   ),
   author= site_author,
)
def page_pinephone_os_manjaro_phosh(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   yaml_content, template_file = http_request.parse_content_config(
      projects_src_dir / "pinephone" / "manjaro-arm.yaml"
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   return (content_dct, template_file,);
# fed



webgl_css = [
   { "cssname": "/js/libs/highlight/styles/default.css", "mode": _base.MODE_ANY, },
   { "cssname": "/css/highlight-dark.css", "mode": _base.MODE_DARK, },
   { "cssname": "/css/highlight-lite.css", "mode": _base.MODE_LITE, },
   { "cssname": "/css/highlight.css", "mode": _base.MODE_ANY, },
   { "cssname": "/css/projects.css", "mode": _base.MODE_ANY, },
   { "cssname": "/css/webgl.css", "mode": _base.MODE_ANY, },
   # { "cssname": "/css/projects-lite.css", "mode": _base.MODE_LITE, },
   # { "cssname": "/css/projects-dark.css", "mode": _base.MODE_DARK, },
];

webgl_js = [
   {"scriptname": "/js/libs/threejs/three.min.js"},
   {"scriptname": "/js/libs/threejs/js/loaders/GLTFLoader.js"},
];


@app_bp.route("/projects/webgl/threejs/intro", methods=["GET",],)
@app_bp.route("/projects/webgl/threejs/intro.html", methods=["GET",],)
@app_bp.route("/projects/webgl/threejs/intro.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= webgl_css,
   js_lst= webgl_js + [
      {"module": "/js/threejs-demo-intro.js"},
   ],
   title= "WebGL: ThreeJS Intro (www.tommypkeane.com)",
   description= (
      f"Example Demo with Three.js written by {author_name_display},"
      " to show how to setup and use WebGL interactively in a webpage."
   ),
   author= site_author,
)
def page_webgl_demos_threejs_intro(theme_class):
   """Provide the Settings (Customisation) Page.
   """

   yaml_content, template_file = http_request.parse_content_config(
      projects_src_dir / "webgl_demos" / "threejs_intro" / "demo_intro.yaml"
   );

   content_dct = dict();
   content_dct.update(yaml_content);

   # content_file = (projects_src_dir / "webgl_demos" / "threejs_intro" / "demo_intro.md")

   # parser_obj = commonmark.Parser();
   # html_renderer = commonmark.HtmlRenderer();
   # ast_obj = None;

   # with open(content_file, "r") as file_obj:
   #    ast_obj = parser_obj.parse(
   #       file_obj.read(),
   #    );
   # # htiw

   # content_dct = {
   #    "main_contents": html_renderer.render(ast_obj),
   # };

   # template_file = (projects_src_dir / "webgl_demos" / "threejs_intro" / "demo_intro.mustache");

   return (content_dct, template_file,);
# fed


