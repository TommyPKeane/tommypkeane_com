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


webapp = flask.Flask(__name__);

stache_compiler = pystache.Renderer();

def _generate_html(source_file, data_dct,):
   """Generate HTML from a Mustache File and Data Dictionary.

   Args:
      source_file (str, path-like): Path to Mustache file, including filename.
      data_dct (dict): Dictionary of template replacements.

   Returns:
      A string of valid HTML contents after parsing the Mustache file and
      filling in the replacement contents from the data dictionary.
   """
   raw_str = None;

   with open(source_file, 'r') as file_obj:
      raw_str = file_obj.read();
   # htiw

   parsed_str = pystache.parse(raw_str);

   html_str = stache_compiler.render(
      parsed_str,
      data_dct,
   );

   return (html_str);
# fed


@webapp.route("/", methods=["GET",],)
@webapp.route("/index", methods=["GET",],)
@webapp.route("/index.html", methods=["GET",],)
@webapp.route("/index.htm", methods=["GET",],)
def intro():
   """Provide the Main Landing Page Response
   """
   response_str = _generate_html(
      "index.mustache",
      {
         "title": "tommypkeane-com",
         "ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
         "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
         "description": "Landing Page for tommypkeane.com, website of Tommy P. Keane, Data-Scientist and Software-Engineer.",
         "author": "Tommy P. Keane",
         "stylesheets": {
            "cssname": "/css/bootstrap.min.css",
         },
         "header_contents": """<h1>Tommy P. Keane</h1>""",
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
            { "scriptname": "/js/jquery.min.js" },
            { "scriptname": "/js/bootstrap.bundle.min.js" },
            { "scriptname": "/js/d3.min.js" },
            { "scriptname": "/js/cookie.js" },
         ],
      },
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

   response_str = _generate_html(
      "settings.mustache",
      {
         "title": "tommypkeane-com_settings",
         "ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
         "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
         "description": "Settings (Cookie Management) Page for www.tommypkeane.com with per GDPR compliance.",
         "author": "Tommy P. Keane",
         "stylesheets": {
            "cssname": "/css/bootstrap.min.css",
         },
         "header_contents": (
"""<h1>Tommy P. Keane</h1>
<h2>Settings Page</h2>
<h3>Manage Cookies and Review Configurable Settings</h3>
<hr/>
"""
         ),
         "main_contents": "",
         "footer_contents": "",
         "scriptfiles": [
            { "scriptname": "/js/jquery.min.js" },
            { "scriptname": "/js/bootstrap.bundle.min.js" },
            { "scriptname": "/js/d3.min.js" },
            { "scriptname": "/js/cookie.js" },
            { "scriptname": "/js/settings.js" },
         ],
         "cookies" : cookies_lst,
      },
   );

   response_obj.set_data(response_str);

   return (response_obj);
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