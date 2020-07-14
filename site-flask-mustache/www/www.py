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
   ep_cookies,
   ep_errors,
   ep_educational,
   ep_resume,
   ep_static,
   ep_photography,
   http_request,
);


webapp = flask.Flask(__name__);


@webapp.route("/", methods=["GET",],)
@webapp.route("/index", methods=["GET",],)
@webapp.route("/index.html", methods=["GET",],)
@webapp.route("/index.htm", methods=["GET",],)
def intro():
   """Provide the Main Landing Page Response
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
   body_theme_class = flask.request.cookies.get("theme");

   if (body_theme_class is None):
      body_theme_class = "default";
      ck_theme_lightondark_selected = "selected";
      ck_theme_darkonlight_selected = "";
   else:
      ck_theme_lightondark_selected = ("", "selected")[int(body_theme_class == "light_on_dark")];
      ck_theme_darkonlight_selected = ("", "selected")[int(body_theme_class == "dark_on_light")];
   # fi

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

   stylesheets_lst = copy.deepcopy(_base.BASE_STYLESHEETS);
   # stylesheets_lst.append(...);

   scripts_lst = copy.deepcopy(_base.BASE_SCRIPTS);

   template_data = dict();
   template_data.update(
      http_request._get_template_data_icons()
   );
   template_data.update(
      {
         "title": "Tommy P. Keane - Professional Website",
         "description": "Landing Page for www.tommypkeane.com, website of Tommy P. Keane, Data-Scientist and Software-Engineer.",
         "author": "Tommy P. Keane",
      }
   );
   template_data.update(
      {
         "body_theme_class": _base.THEME_CLASSES[body_theme_class]["body"],
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
      "./src/templates/index.mustache",
      template_data,
   );
   
   return (response_str);
# fed


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

   body_theme_class = flask.request.cookies.get("theme");

   if (body_theme_class is None):
      body_theme_class = "default";
      ck_theme_lightondark_selected = "selected";
      ck_theme_darkonlight_selected = "";
   else:
      ck_theme_lightondark_selected = ("", "selected")[int(body_theme_class == "light_on_dark")];
      ck_theme_darkonlight_selected = ("", "selected")[int(body_theme_class == "dark_on_light")];
   # fi

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

   stylesheets_lst = copy.deepcopy(_base.BASE_STYLESHEETS);
   stylesheets_lst.append({"cssname": "/css/error.css",});

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
         "body_theme_class": _base.THEME_CLASSES[body_theme_class]["body"],
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
   webapp.run(
      host= "0.0.0.0",
      port= "80",
      debug= True,
   );
# fi

