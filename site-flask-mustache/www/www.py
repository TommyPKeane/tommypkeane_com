# @file
# @brief Main Module for Site Application
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com>
# @copyright 2020, Tommy P. Keane

import datetime;
import sys;

import flask;
import pystache;

TWO_WEEKS_SECONDS = 1_209_600;

THEME_CLASSES = {
   "default": {
      "body": "lightondark",
      "table": "table-dark",
      "btncls_cookies_store": "btn-outline-primary",
      "btncls_cookies_erase": "btn-outline-danger",
      "navbar": "navbar-dark bg-dark",
   },
   "light_on_dark": {
      "body": "lightondark",
      "table": "table-dark",
      "btncls_cookies_store": "btn-outline-primary",
      "btncls_cookies_erase": "btn-outline-danger",
      "navbar": "navbar-dark bg-dark",
   },
   "dark_on_light": {
      "body": "darkonlight",
      "table": "table-light",
      "btncls_cookies_store": "btn-outline-primary",
      "btncls_cookies_erase": "btn-outline-danger",
      "navbar": "navbar-light bg-light",
   },
}


webapp = flask.Flask(__name__);

def _generate_html(source_file, data_dct,):
   """Generate HTML from a Mustache File and Data Dictionary.

   Args:
      source_file (str, path-like): Path to Mustache file, including filename.
      data_dct (dict): Dictionary of template replacements.

   Returns:
      A string of valid HTML contents after parsing the Mustache file and
      filling in the replacement contents from the data dictionary.
   """

   with open("header_contents.mustache", "r") as header_file_obj:
      header_str = header_file_obj.read();
   # htiw

   stache_compiler = pystache.Renderer(
      partials= {
         "header_contents": header_str,
      }
   );

   raw_str = None;

   with open(source_file, "r") as file_obj:
      raw_str = file_obj.read();
   # htiw

   parsed_str = pystache.parse(raw_str);

   html_str = stache_compiler.render(
      parsed_str,
      data_dct,
   );

   return (html_str);
# fed

def _get_svg(filename,):
   """Get the SVG XML as a string, for raw injection into document.
   """
   contents_str = None;

   with open(filename, "r") as svg_file:
      contents_str = svg_file.read();
   # htiw

   return (contents_str);
# fed

def _get_nav_template_data():
   """Get the template replacement data for the common site navbar.
   """
   data_dct = {
      "icon_home": _get_svg("./img/feather/home.svg"),
      "icon_about_me": _get_svg("./img/feather/smile.svg"),
      "icon_cv_resume": _get_svg("./img/feather/briefcase.svg"),
      "icon_other_sites": _get_svg("./img/feather/menu.svg"),
      "icon_settings": _get_svg("./img/feather/settings.svg"),
      "icon_github": _get_svg("./img/feather/github.svg"),
      "icon_bitbucket": _get_svg("./img/feather/droplet.svg"),
      "icon_google_scholar": _get_svg("./img/feather/award.svg"),
      "icon_instagram": _get_svg("./img/feather/instagram.svg"),
      "icon_facebook": _get_svg("./img/feather/facebook.svg"),
      "icon_twitter": _get_svg("./img/feather/twitter.svg"),
      "icon_linkedin": _get_svg("./img/feather/linkedin.svg"),
      "icon_projects": _get_svg("./img/feather/tool.svg"),
      "icon_raspberrypi": _get_svg("./img/feather/cpu.svg"),
      "icon_odroid": _get_svg("./img/feather/cpu.svg"),
      "icon_pinetime": _get_svg("./img/feather/watch.svg"),
      "icon_pinephone": _get_svg("./img/feather/phone.svg"),
   };
   return (data_dct);
# fed


@webapp.route("/", methods=["GET",],)
@webapp.route("/index", methods=["GET",],)
@webapp.route("/index.html", methods=["GET",],)
@webapp.route("/index.htm", methods=["GET",],)
def intro():
   """Provide the Main Landing Page Response
   """
   cookies_dct = flask.request.json;
   if (cookies_dct is None):
      cookies_dct = flask.request.cookies.to_dict();
   # fi

   body_theme_class = flask.request.cookies.get("theme");

   if (body_theme_class is None):
      body_theme_class = "default";
   # fi

   template_data = dict();
   template_data.update(_get_nav_template_data());
   template_data.update(
      {
         "title": "tommypkeane-com",
         "ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
         "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
         "description": "Landing Page for tommypkeane.com, website of Tommy P. Keane, Data-Scientist and Software-Engineer.",
         "author": "Tommy P. Keane",
         "stylesheets": [
            { "cssname": "/css/bootstrap.min.css", },
            { "cssname": "/css/index.css", },
         ],
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
         "header_contents": """<h1>Tommy P. Keane</h1>""",
         "icon_home": _get_svg("./img/feather/home.svg"),
         "main_contents": (
"""<h1>Hiya!</h1>
<select name="theme" id="id_theme_choice">
  <option value="light_on_dark">Light Text on Dark Background</option>
  <option value="dark_on_light">Dark Text on Light Background</option>
</select>
<button type="button" onclick="cookie_submit();">Set Cookies</button>
"""
         ),
         "footer_contents": "",
         "scriptfiles": [
            { "scriptname": "/js/jquery.min.js", },
            { "scriptname": "/js/bootstrap.bundle.min.js", },
            { "scriptname": "/js/d3.min.js", },
            { "scriptname": "/js/cookie.js", },
         ],
      }
   );

   response_str = _generate_html(
      "index.mustache",
      template_data,
   );
   
   return (response_str);
# fed


@webapp.route("/settings", methods=["GET",],)
@webapp.route("/settings.html", methods=["GET",],)
@webapp.route("/settings.htm", methods=["GET",],)
def customise():
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
            "lifetime": TWO_WEEKS_SECONDS,
         },
      );
   # rof

   template_data = dict();
   template_data.update(_get_nav_template_data());
   template_data.update(
      {
         "title": "tommypkeane-com_settings",
         "ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
         "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
         "description": "Settings (Cookie Management) Page for www.tommypkeane.com with per GDPR compliance.",
         "author": "Tommy P. Keane",
         "stylesheets": [
            { "cssname": "/css/bootstrap.min.css", },
            { "cssname": "/css/index.css", },
         ],
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "table_class": THEME_CLASSES[body_theme_class]["table"],
         "btncls_cookies_store": THEME_CLASSES[body_theme_class]["btncls_cookies_store"],
         "btncls_cookies_erase": THEME_CLASSES[body_theme_class]["btncls_cookies_erase"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
         "main_contents": "",
         "footer_contents": "",
         "scriptfiles": [
            { "scriptname": "/js/jquery.min.js", },
            { "scriptname": "/js/bootstrap.bundle.min.js", },
            { "scriptname": "/js/d3.min.js", },
            { "scriptname": "/js/cookie.js", },
            { "scriptname": "/js/settings.js", },
         ],
         "cookies" : cookies_lst,
      }
   );

   response_str = _generate_html(
      "settings.mustache",
      template_data,
   );

   response_obj.set_data(response_str);

   return (response_obj);
# fed


@webapp.route("/resume", methods=["GET",],)
@webapp.route("/resume.html", methods=["GET",],)
@webapp.route("/resume.htm", methods=["GET",],)
def resume_cv():
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
            "lifetime": TWO_WEEKS_SECONDS,
         },
      );
   # rof

   template_data = dict();
   template_data.update(_get_nav_template_data());
   template_data.update(
      {
         "title": "tommypkeane-com_resume",
         "ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
         "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
         "description": "History and Details of Professional Experience of Tommy P. Keane.",
         "author": "Tommy P. Keane",
         "stylesheets": [
            { "cssname": "/css/bootstrap.min.css", },
            { "cssname": "/css/index.css", },
         ],
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "table_class": THEME_CLASSES[body_theme_class]["table"],
         "btncls_cookies_store": THEME_CLASSES[body_theme_class]["btncls_cookies_store"],
         "btncls_cookies_erase": THEME_CLASSES[body_theme_class]["btncls_cookies_erase"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
         "main_contents": "",
         "footer_contents": "",
         "scriptfiles": [
            { "scriptname": "/js/jquery.min.js", },
            { "scriptname": "/js/bootstrap.bundle.min.js", },
            { "scriptname": "/js/d3.min.js", },
            { "scriptname": "/js/cookie.js", },
            { "scriptname": "/js/settings.js", },
         ],
         "cookies" : cookies_lst,
      }
   );

   response_str = _generate_html(
      "resume.mustache",
      template_data,
   );

   response_obj.set_data(response_str);

   return (response_obj);
# fed

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
   # fi

   for (index, (key, value)) in enumerate(cookies_dct.items()):
      cookies_lst.append(
         {
            "index": index,
            "key": key,
            "value": value,
            "lifetime": TWO_WEEKS_SECONDS,
         },
      );
   # rof

   template_data = dict();
   template_data.update(_get_nav_template_data());
   template_data.update(
      {
         "title": "tommypkeane-com_resume",
         "ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
         "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
         "description": "404 Error Page (Requested Resource Not Found).",
         "author": "Tommy P. Keane",
         "stylesheets": [
            { "cssname": "/css/bootstrap.min.css", },
            { "cssname": "/css/index.css", },
         ],
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
         "main_contents": "",
         "footer_contents": "",
         "scriptfiles": [
            { "scriptname": "/js/jquery.min.js", },
            { "scriptname": "/js/bootstrap.bundle.min.js", },
            { "scriptname": "/js/d3.min.js", },
            { "scriptname": "/js/cookie.js", },
            { "scriptname": "/js/settings.js", },
         ],
         "cookies" : cookies_lst,
      }
   );

   response_str = _generate_html(
      "404.mustache",
      template_data,
   );

   response_obj.set_data(response_str);

   return (response_obj, 404,);
# fed

@webapp.route('/img/<path:path>', methods=["GET",])
def get_static_img(path):
   """Provide the static image files when requested.
   """
   response_obj = flask.send_from_directory("img", path);
   return (response_obj);
# fed


@webapp.route('/js/<path:path>', methods=["GET",])
def get_static_js(path):
   """Provide the static JavaScript files when requested.
   """
   response_obj = flask.send_from_directory("js", path);
   return (response_obj);
# fed


@webapp.route('/css/<path:path>', methods=["GET",])
def get_static_css(path):
   """Provide the static CSS files when requested.
   """
   response_obj = flask.send_from_directory("css", path);
   return (response_obj);
# fed


@webapp.route('/fonts/<path:path>', methods=["GET",])
def get_static_font(path):
   """Provide the static Font (Typeface) files when requested.
   """
   response_obj = flask.send_from_directory("fonts", path);
   return (response_obj);
# fed


@webapp.route('/set/cookie', methods=["POST",])
def setcookie():
   """Store Cookies for Site
   """
   response_obj = flask.Response();
   response_obj.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
   response_obj.headers["Pragma"] = "no-cache"
   response_obj.headers["Expires"] = "0"
   
   theme_value = flask.request.json.get("theme");
   gdpr_consent_date_value = flask.request.json.get("gdpr_consent");

   response_obj.set_cookie(
      "theme",
      value= theme_value,
      max_age= (0 if (theme_value == "") else TWO_WEEKS_SECONDS),
      # domain= "0.0.0.0",
      # domain= "www.tommypkeane.com",
      path= "/",
      secure= False,
      # secure= True,
      httponly= True,
      # samesite= "Strict",
      samesite= "Lax",
   );
   
   response_obj.set_cookie(
      "gdpr_consent_date",
      value= gdpr_consent_date_value,
      max_age= (0 if (gdpr_consent_date_value == "") else TWO_WEEKS_SECONDS),
      # domain= "0.0.0.0",
      # domain= "www.tommypkeane.com",
      path= "/",
      secure= False,
      # secure= True,
      httponly= True,
      # samesite= "Strict",
      samesite= "Lax",
   );
   
   return (response_obj);
# fed

if (__name__ == "__main__"):
   webapp.run(
      host= "0.0.0.0",
      port= "80",
      debug= True,
   );
# fi
