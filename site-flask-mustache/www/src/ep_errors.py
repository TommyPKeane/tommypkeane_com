import copy;

import flask;

from . import _util;
from . import http_request;


app_bp = flask.Blueprint('errors', __name__);


@app_bp.errorhandler(404)
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
         "navbar_class": _base.THEME_CLASSES[body_theme_class]["navbar"],
         "http_404_error_svg": _util.get_file_contents_str("img/http_404_tommy-lost_plain.svg"),
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
      "404.mustache",
      template_data,
   );

   response_obj.set_data(response_str);

   return (response_obj, 404,);
# fed
