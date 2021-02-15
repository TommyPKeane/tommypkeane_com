# @file
# @brief HTTP Request Utility Methods (and Decorators)
#
# This module provides the functions to be used for wrapping and simplifying
# the common code for making custom HTTP responses with the Flask application.
# All Flask endpoints need to respond with a valid plaintext string or a fully
# formed HTTP response. This module is meant to compartmentalise a lot of the
# redundant code and configuration setup that would otherwise be duplicated in
# all our site's endpoints. So, things like headers, footers, styling, scripts,
# and images/files are embedded here in the functions and wrappers/decorators.
#
# The current design relies on the `.update()` method of the `dict` class to
# allow for custom overrides through function argument dictionaries.
#
# TODO:
# - `html_response` is still lacking certain overrides that could let it be
# used everywhere.
# - Caching could be enhanced and updated in these methods.
# - An Object-Oriented template instead of just using the base `dict` instances
# could be a nicer approach here, and allow for a more generic function by
# relying on base-class methods where derived classes for custom endpoints do
# proper overrides. This would also be more "pythonic".
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2020, Tommy P. Keane

import copy;
import datetime;
import os;

import commonmark;
import flask;
import yaml;

from . import _base;
from . import _images;
from . import _util;


def _get_template_data_icons():
   """Get the template replacement data for the common site navbar.
   """
   return (_images.icon_data_dct);
# fed


def generate_html_common(
      source_file,
      data_dct,
      partials_extra_dct= None,
   ):
   """Create an HTML Response String with common Header and Footer contents.
   """
   partials_dct = {
      "page_head": _util.get_file_contents_str("./src/templates/page_head.mustache"),
      "page_foot": _util.get_file_contents_str("./src/templates/page_foot.mustache"),
      "header_contents": _util.get_file_contents_str("./src/templates/header_contents.mustache"),
      "header_modal_help": _util.get_file_contents_str("./src/templates/header-modal-help.mustache"),
      "header_modal_settings": _util.get_file_contents_str("./src/templates/header-modal-settings.mustache"),
      "header_nav_main": _util.get_file_contents_str("./src/templates/header-nav-main.mustache"),
      "footer_contents": _util.get_file_contents_str("./src/templates/footer_contents.mustache"),
   };

   data_dct.update(
      {
         "nav_links": [
            {
               "target": "/",
               "icon": _images.icon_data_dct.get("icon_home", ""),
               "title": "tommypkeane.com",
            },
            {
               "target": "/resume",
               "icon": _images.icon_data_dct.get("icon_cv_resume", ""),
               "title": "professionalism",
            },
            {
               "target": "https://www.github.com/tommypkeane",
               "icon": _images.icon_data_dct.get("icon_github", ""),
               "title": "polyglotism",
            },
            {
               "target": "/projects",
               "icon": _images.icon_data_dct.get("icon_raspberrypi", ""),
               "title": "empiricism",
            },
            {
               "target": "/artsycrafts",
               "icon": _images.icon_data_dct.get("icon_photography", ""),
               "title": "aestheticism",
            },
            {
               "target": "/teaches",
               "icon": _images.icon_data_dct.get("icon_books", ""),
               "title": "gnosticism",
            },
            {
               "target": "/about",
               "icon": _images.icon_data_dct.get("icon_contact", ""),
               "title": "solipsism",
            },
         ],
         "ep_last_modified_date": datetime.datetime.fromtimestamp(
               os.path.getmtime(source_file),
               datetime.timezone.utc,
            ).isoformat(),
         "ep_last_modified_author": "tommy",
         "site_repo_url": "https://github.com/TommyPKeane/tommypkeane_com",
         "site_repo_title": "tommypkeane_com/www",
         "tommy": "<b>tommy</b>",
      },
   );

   contents_str = _util.generate_html(
      source_file,
      data_dct,
      partials_dct,
      partials_extra_dct,
   );

   return (contents_str);
# fed


def html_response(
   css_lst,
   js_lst,
   title,
   description,
   author,
   partials_dct= None,
):
   """Wrapper function to use for HTML Response from Endpoints."""
   def argumentless_wrapper(func,):

      def inner_call(*args, **kwargs):
         response_obj = flask.Response();
         response_obj.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
         response_obj.headers["Pragma"] = "no-cache"
         response_obj.headers["Expires"] = "0"

         cookies_lst = [];

         cookies_dct = flask.request.json;
         if (cookies_dct is None):
            cookies_dct = flask.request.cookies.to_dict();
         # fi

         ck_theme_lightondark_selected = None;
         ck_theme_darkonlight_selected = None;
         ck_theme_vaporwave_selected = None;
         ck_theme_seapunk_selected = None;
         theme_class = flask.request.cookies.get("theme");

         if (theme_class is None):
            theme_class = "default";
            ck_theme_lightondark_selected = "selected";
            ck_theme_darkonlight_selected = "";
            ck_theme_vaporwave_selected = "";
            ck_theme_seapunk_selected = "";
         else:
            ck_theme_lightondark_selected = ("selected" if (theme_class == "light_on_dark") else "");
            ck_theme_darkonlight_selected = ("selected" if (theme_class == "dark_on_light") else "");
            ck_theme_vaporwave_selected = ("selected" if (theme_class == "vaporwave") else "");
            ck_theme_seapunk_selected = ("selected" if (theme_class == "seapunk") else "");
         # fi

         crnt_theme_mode = _base.THEME_CLASSES[theme_class];

         for (index, (key, value)) in enumerate(cookies_dct.items()):
            cookies_lst.append(
               {
                  "index": index,
                  "key": key,
                  "value": value,
                  "lifetime": _base.TWO_WEEKS_SECONDS,
               },
            );
         # rof

         tmp_stylesheets_lst = copy.deepcopy(_base.BASE_STYLESHEETS);
         tmp_stylesheets_lst.extend(css_lst);

         stylesheets_lst = [];

         for css_dct in tmp_stylesheets_lst:
            if (css_dct["mode"] in (_base.MODE_ANY, crnt_theme_mode,)):
               stylesheets_lst.append(css_dct);
            # fi
         # rof

         scripts_lst = copy.deepcopy(_base.BASE_SCRIPTS);
         scripts_lst.extend(js_lst);

         template_data = dict();
         template_data.update(
            _get_template_data_icons()
         );
         template_data.update(
            {
               "title": title,
               "description": description,
               "author": author,
            }
         );
         template_data.update(
            {
               "theme_class": _base.THEME_CLASSES[theme_class],
               "ck_theme_lightondark_selected": ck_theme_lightondark_selected,
               "ck_theme_darkonlight_selected": ck_theme_darkonlight_selected,
            }
         );
         template_data.update(
            {
               "stylesheets": stylesheets_lst,
               "scriptfiles": [script_obj for script_obj in scripts_lst if "scriptname" in script_obj],
               "modulefiles": [module_obj for module_obj in scripts_lst if "module" in module_obj],
               "cookies" : cookies_lst,
            }
         );

         (
           content_dct,
           template_file,
         ) = func(theme_class, *args, **kwargs);

         template_data.update(content_dct);

         response_str = generate_html_common(
            template_file,
            template_data,
            partials_dct,
         );

         response_obj.set_data(response_str);

         return (response_obj);
      # fed

      inner_call.__name__ = (func.__name__);

      return (inner_call);
   # fed

   return (argumentless_wrapper);
# fed


def parse_content_config(filename):

   parser_obj = commonmark.Parser();
   html_renderer = commonmark.HtmlRenderer();
   ast_obj = None;

   article_content_dct = dict();
   yaml_config = None;

   with open(filename, "r") as file_obj:
      yaml_config = yaml.safe_load(file_obj.read());
   # htiw

   article_content_dct["bc_base_href"] = yaml_config.get("bc_base_href", "");
   article_content_dct["bc_topic_href"] = yaml_config.get("bc_topic_href", "");
   article_content_dct["page_bc_base"] = yaml_config.get("page_bc_base", "");
   article_content_dct["page_topic"] = yaml_config.get("page_topic", "");
   article_content_dct["page_name"] = yaml_config.get("page_name", "");

   intro_file = os.path.join(
      yaml_config["src_dir"],
      yaml_config["intro"]["filename"],
   );

   with open(intro_file, "r") as file_obj:
      ast_obj = parser_obj.parse(
         file_obj.read(),
      );
   # htiw

   article_content_dct[
      yaml_config["intro"]["template_key"]
   ] = html_renderer.render(ast_obj);

   article_content_dct["intro_title"] = yaml_config["intro_title"];
   article_content_dct["intro_subtitle"] = yaml_config["intro_subtitle"];

   article_content_dct["toc"] = [];
   article_content_dct["content"] = [];

   template_file = yaml_config["template"];


   if (yaml_config["content"] is None):
      pass;
   else:
      for content in yaml_config["content"]:
         config_file = os.path.join(
            yaml_config["src_dir"],
            content["filename"],
         );

         with open(config_file, "r") as file_obj:
            ast_obj = parser_obj.parse(
               file_obj.read(),
            );
         # htiw

         article_content_dct["content"].append(
            {
               "article_id": content["article_id"],
               "article_title": content["article_title"],
               "article": html_renderer.render(ast_obj),
            },
         );

         article_content_dct["toc"].append(
            {
               "article_id": content["article_id"],
               "article_title": content["article_title"],
               "subtitles": content["subtitles"],
            },
         );
      # rof
   #fi

   if (yaml_config["raw_content_key"] is None):
      pass;
   else:
      article_content_dct[
         yaml_config["raw_content_key"]
      ] = yaml_config["raw_content"];
   # fi

   return (article_content_dct, template_file,);
# fed
