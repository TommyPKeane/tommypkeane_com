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

TWO_WEEKS_SECONDS = 1_209_600;

THEME_CLASSES = {
   "default": {
      "body": "darkonlight",
      "table": "table-light",
      "btncls_cookies_store": "btn-outline-primary",
      "btncls_cookies_erase": "btn-outline-danger",
      "navbar": "navbar-light bg-light",
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
};

BASE_STYLESHEETS = [
   { "cssname": "/css/bootstrap.min.css", },
   { "cssname": "/css/index.css", },
];

BASE_SCRIPTS = [
   { "scriptname": "/js/jquery.min.js", },
   { "scriptname": "/js/bootstrap.bundle.min.js", },
   { "scriptname": "/js/d3.min.js", },
   { "scriptname": "/js/cookie.js", },
   { "scriptname": "/js/index.js", },
];


webapp = flask.Flask(__name__);

def _get_file_contents_str(filename,):
   """Get the SVG XML as a string, for raw injection into document.
   """
   contents_str = None;
   with open(filename, "r") as file_obj:
      contents_str = file_obj.read();
   # htiw
   return (contents_str);
# fed

def _get_resume_details():
   """Get the template replacement data for the resume/cv job details.
   """
   data_dct = {
      "job_unemployment": _get_file_contents_str("./resume_cv/job_unemployment.mustache"),
      "job_software_engineer_businessintelligence": _get_file_contents_str("./resume_cv/job_software_engineer_businessintelligence.mustache"),
      "job_software_engineer_satcom": _get_file_contents_str("./resume_cv/job_software_engineer_satcom.mustache"),
      "job_graduate_research_assistant": _get_file_contents_str("./resume_cv/job_graduate_research_assistant.mustache"),
      "job_graduate_teaching_assistant": _get_file_contents_str("./resume_cv/job_graduate_teaching_assistant.mustache"),
      "job_student_phd": _get_file_contents_str("./resume_cv/job_student_phd.mustache"),
      "job_student_msc": _get_file_contents_str("./resume_cv/job_student_msc.mustache"),
      "job_student_bsc": _get_file_contents_str("./resume_cv/job_student_bsc.mustache"),
      "job_student_hs": _get_file_contents_str("./resume_cv/job_student_hs.mustache"),
      "job_coop_videosecurity": _get_file_contents_str("./resume_cv/job_coop_videosecurity.mustache"),
      "job_coop_weatherdata": _get_file_contents_str("./resume_cv/job_coop_weatherdata.mustache"),
      "job_coop_touchscreen_repair": _get_file_contents_str("./resume_cv/job_coop_touchscreen_repair.mustache"),
      "job_coop_network_technician": _get_file_contents_str("./resume_cv/job_coop_network_technician.mustache"),
      "job_cashier_grocery": _get_file_contents_str("./resume_cv/job_cashier_grocery.mustache"),
      "job_cashier_electronics": _get_file_contents_str("./resume_cv/job_cashier_electronics.mustache"),
   };
   return (data_dct);
# fed

def _generate_html(source_file, data_dct,):
   """Generate HTML from a Mustache File and Data Dictionary.

   Args:
      source_file (str, path-like): Path to Mustache file, including filename.
      data_dct (dict): Dictionary of template replacements.

   Returns:
      A string of valid HTML contents after parsing the Mustache file and
      filling in the replacement contents from the data dictionary.
   """

   partials_dct = {
      "header_contents": _get_file_contents_str("header_contents.mustache"),
      "footer_contents": _get_file_contents_str("footer_contents.mustache"),
   };
   partials_dct.update(_get_resume_details());

   stache_compiler = pystache.Renderer(
      partials= partials_dct,
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

def _get_template_data_icons():
   """Get the template replacement data for the common site navbar.
   """
   data_dct = {
      # FEATHER ICONS
      "icon_home": _get_file_contents_str("./img/feather/home.svg"),
      "icon_about_me": _get_file_contents_str("./img/feather/smile.svg"),
      "icon_cv_resume": _get_file_contents_str("./img/feather/briefcase.svg"),
      "icon_bitbucket": _get_file_contents_str("./img/feather/droplet.svg"),
      "icon_google_scholar": _get_file_contents_str("./img/feather/award.svg"),
      "icon_instagram": _get_file_contents_str("./img/feather/instagram.svg"),
      "icon_facebook": _get_file_contents_str("./img/feather/facebook.svg"),
      "icon_twitter": _get_file_contents_str("./img/feather/twitter.svg"),
      "icon_linkedin": _get_file_contents_str("./img/feather/linkedin.svg"),
      "icon_projects_hw": _get_file_contents_str("./img/feather/tool.svg"),
      "icon_raspberrypi": _get_file_contents_str("./img/feather/cpu.svg"),
      "icon_odroid": _get_file_contents_str("./img/feather/cpu.svg"),
      "icon_pinetime": _get_file_contents_str("./img/feather/watch.svg"),
      "icon_pinephone": _get_file_contents_str("./img/feather/phone.svg"),
      "icon_projects_sw": _get_file_contents_str("./img/feather/tool.svg"),
      "icon_publications": _get_file_contents_str("./img/feather/file-text.svg"),
      "img_scroll_to_top": _get_file_contents_str("./img/feather/chevrons-up.svg"),
      "img_intro_collapse": _get_file_contents_str("./img/feather/chevrons-up.svg"),
      "img_intro_expand": _get_file_contents_str("./img/feather/chevrons-down.svg"),
      "icon_contact": _get_file_contents_str("./img/feather/phone.svg"),
      # TOMMYTOFU ICONS
      "icon_settings": _get_file_contents_str("./img/tommytofu/config.svg"),
      "icon_other_sites": _get_file_contents_str("./img/tommytofu/menu.svg"),
      "icon_github": _get_file_contents_str("./img/tommytofu/git-octocat.svg"),
      "icon_photography": _get_file_contents_str("./img/tommytofu/camera-photo.svg"),
      # OTHERS
      "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
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

   stylesheets_lst = copy.deepcopy(BASE_STYLESHEETS);
   # stylesheets_lst.append(...);

   scripts_lst = copy.deepcopy(BASE_SCRIPTS);

   template_data = dict();
   template_data.update(
      _get_template_data_icons()
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
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
      }
   );
   template_data.update(
      {
         "stylesheets": stylesheets_lst,
         "scriptfiles": scripts_lst,
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

   stylesheets_lst = BASE_STYLESHEETS;
   # stylesheets_lst.append(...);

   scripts_lst = copy.deepcopy(BASE_SCRIPTS);

   template_data = dict();
   template_data.update(_get_template_data_icons());
   template_data.update(
      {
         "title": "Settings (www.tommypkeane.com)",
         "description": "Settings (Cookie Management) Page for www.tommypkeane.com per GDPR compliance.",
         "author": "Tommy P. Keane",
      }
   );
   template_data.update(
      {
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "table_class": THEME_CLASSES[body_theme_class]["table"],
         "btncls_cookies_store": THEME_CLASSES[body_theme_class]["btncls_cookies_store"],
         "btncls_cookies_erase": THEME_CLASSES[body_theme_class]["btncls_cookies_erase"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
      }
   );
   template_data.update(
      {
         "stylesheets": stylesheets_lst,
         "scriptfiles": scripts_lst,
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

   stylesheets_lst = copy.deepcopy(BASE_STYLESHEETS);
   stylesheets_lst.append({"cssname": "/css/resume-cv.css",});

   scripts_lst = copy.deepcopy(BASE_SCRIPTS);
   scripts_lst.append({"scriptname": "/js/cvtimeline.js",});

   template_data = dict();
   template_data.update(_get_template_data_icons());
   template_data.update(_get_resume_details());
   template_data.update(
      {
         "title": "Resumé / CV (www.tommypkeane.com)",
         "description": "History and Details of Professional Experience of Tommy P. Keane.",
         "author": "Tommy P. Keane",
      }
   );
   template_data.update(
      {
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "table_class": THEME_CLASSES[body_theme_class]["table"],
         "btncls_cookies_store": THEME_CLASSES[body_theme_class]["btncls_cookies_store"],
         "btncls_cookies_erase": THEME_CLASSES[body_theme_class]["btncls_cookies_erase"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
      }
   );
   template_data.update(
      {
         "resume_cv_timeline": _get_file_contents_str("./img/cv_timeline_plain.svg"),
         "stylesheets": stylesheets_lst,
         "scriptfiles": scripts_lst,
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

   stylesheets_lst = copy.deepcopy(BASE_STYLESHEETS);
   stylesheets_lst.append({"cssname": "/css/error.css",});

   scripts_lst = BASE_SCRIPTS;
   scripts_lst.append({"scriptname": "/js/settings.js",});

   template_data = dict();
   template_data.update(_get_template_data_icons());
   template_data.update(_get_resume_details());
   template_data.update(
      {
         "title": "HTTP ERROR 404 (www.tommypkeane.com)",
         "description": "404 Error Page -- Requested Resource Not Found.",
         "author": "Tommy P. Keane",
      }
   );
   template_data.update(
      {
         "body_theme_class": THEME_CLASSES[body_theme_class]["body"],
         "navbar_class": THEME_CLASSES[body_theme_class]["navbar"],
         "http_404_error_svg": _get_file_contents_str("img/http_404_tommy-lost_plain.svg"),
      }
   );
   template_data.update(
      {
         "stylesheets": stylesheets_lst,
         "scriptfiles": scripts_lst,
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
