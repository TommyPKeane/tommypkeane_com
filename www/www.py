# @file
# @brief Main Module for Site Application
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com>
# @copyright 2020, Tommy P. Keane

import copy;
import datetime;
import sys;

import flask;
import pystache;

from src import (
   _base,
   _util,
   ep_main,
   ep_cookies,
   ep_errors,
   ep_educational,
   ep_projects,
   ep_resume,
   ep_static,
   ep_photography,
   http_request,
);


webapp = flask.Flask(__name__);

webapp.register_blueprint(ep_main.app_bp);

webapp.register_blueprint(ep_projects.app_bp);

webapp.register_blueprint(ep_resume.app_bp);

webapp.register_blueprint(ep_errors.app_bp);

@webapp.errorhandler(404)
def error_404(error_code):
   """Provide the Settings (Customisation) Page.
   """
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

   stylesheets_lst = [];

   for css_dct in tmp_stylesheets_lst:
      if (css_dct["mode"] in (_base.MODE_ANY, crnt_theme_mode,)):
         stylesheets_lst.append(css_dct);
      # fi
   # rof

   scripts_lst = copy.deepcopy(_base.BASE_SCRIPTS);
   scripts_lst.append({"scriptname": "/js/settings.js",});

   template_data = dict();
   template_data.update(http_request._get_template_data_icons());
   template_data.update(
      {
         "title": "HTTP ERROR 404 (www.tommypkeane.com)",
         "description": "404 Error Page -- Requested Resource Not Found.",
         "author": "Tommy P. Keane",
      }
   );
   template_data.update(
      {
         "theme_class": _base.THEME_CLASSES[theme_class],
         "http_404_error_svg": _util.get_file_contents_str("img/http_404_tommy-lost_plain.svg"),
         "ck_theme_lightondark_selected": ck_theme_lightondark_selected,
         "ck_theme_darkonlight_selected": ck_theme_darkonlight_selected,
      }
   );
   template_data.update(
      {
         "stylesheets": stylesheets_lst,
         "scriptfiles": scripts_lst,
         "cookies" : cookies_lst,
      }
   );

   response_str = http_request.generate_html_common(
      "./src/templates/404.mustache",
      template_data,
   );

   response_obj.set_data(response_str);

   return (response_obj, 404,);
# fed

webapp.register_blueprint(ep_static.app_bp);

webapp.register_blueprint(ep_cookies.app_bp);

webapp.register_blueprint(ep_photography.app_bp);

webapp.register_blueprint(ep_educational.app_bp);


if (__name__ == "__main__"):
   # FOR LOCAL DEVELOPMENT TESTING ONLY
   webapp.run(
      host= "0.0.0.0",
      port= "80",
      debug= True,
   );
# fi

