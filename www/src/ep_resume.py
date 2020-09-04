# @file
# @brief Endpoints and Blueprint for Business (Professional) Pages
# 
# This module provides the Flask endpoints' Blueprint to support the site pages
# for our "Business" life -- basically anything related to professional roles,
# availability, job searches, and our resumé or CV.
# 
# Currently it's just an interactive CV timeline, but future updates should be
# able to provide a bit more related to our professional experiences and skills.
# We generally want to be ambiguous and vague about the previous companies or
# institutions where we've worked, because we don't want to create any perceived
# linkages between this site and those companies. Nothing on this site has been
# provided or built by any time, tools, or resources from our previous roles at
# any organisation. This is solely a personal site, so even though we may "lose"
# out on any possible personal advertisement of institute or company names for
# places we've worked before, it seems better to just talk about our role and
# what we did, no matter what the company was/is.
# 
# As such, company names should also be redacted in all the file names and any
# associated metadata. Would be pretty dumb to try to be anonymous but then have
# names show up in URLs and HTTP requests.
# 
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2020, Tommy P. Keane

import copy;
import pathlib;

import flask;

from . import (
   _base,
   _util,
   http_request,
);


base_dir = pathlib.Path("./src/templates/resume_cv/")


app_bp = flask.Blueprint("resume_cv", __name__);


@app_bp.route("/business", methods=["GET",],)
@app_bp.route("/professional", methods=["GET",],)
@app_bp.route("/resume", methods=["GET",],)
@app_bp.route("/resume.html", methods=["GET",],)
@app_bp.route("/resume.htm", methods=["GET",],)
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

   ck_theme_lightondark_selected = None;
   ck_theme_darkonlight_selected = None;
   theme_class = flask.request.cookies.get("theme");

   if (theme_class is None):
      theme_class = "default";
      ck_theme_lightondark_selected = "selected";
      ck_theme_darkonlight_selected = "";
   else:
      ck_theme_lightondark_selected = ("", "selected")[int(theme_class == "light_on_dark")];
      ck_theme_darkonlight_selected = ("", "selected")[int(theme_class == "dark_on_light")];
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
   stylesheets_lst.append({"cssname": "/css/resume-cv.css",});
   stylesheets_lst.append({"cssname": "/css/resume-cv-light.css",});
   stylesheets_lst.append({"cssname": "/css/resume-cv-dark.css",});

   scripts_lst = copy.deepcopy(_base.BASE_SCRIPTS);
   scripts_lst.append({"scriptname": "/js/cvtimeline.js",});

   template_data = dict();
   template_data.update(http_request._get_template_data_icons());
   template_data.update(
      {
         "title": "Resumé / CV (www.tommypkeane.com)",
         "description": "History and Details of Professional Experience of Tommy P. Keane.",
         "author": "Tommy P. Keane",
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
         "resume_cv_timeline": _util.get_file_contents_str("./img/cv_timeline_plain.svg"),
         "stylesheets": stylesheets_lst,
         "scriptfiles": scripts_lst,
         "cookies" : cookies_lst,
      }
   );

   response_str = http_request.generate_html_common(
      "./src/templates/resume.mustache",
      template_data,
      partials_extra_dct= {
         "job_unemployment": _util.get_file_contents_str(base_dir / "job_unemployment.mustache"),
         "job_software_engineer_businessintelligence": _util.get_file_contents_str(base_dir / "job_software_engineer_businessintelligence.mustache"),
         "job_software_engineer_satcom": _util.get_file_contents_str(base_dir / "job_software_engineer_satcom.mustache"),
         "job_graduate_research_assistant": _util.get_file_contents_str(base_dir / "job_graduate_research_assistant.mustache"),
         "job_graduate_teaching_assistant": _util.get_file_contents_str(base_dir / "job_graduate_teaching_assistant.mustache"),
         "job_student_phd": _util.get_file_contents_str(base_dir / "job_student_phd.mustache"),
         "job_student_msc": _util.get_file_contents_str(base_dir / "job_student_msc.mustache"),
         "job_student_bsc": _util.get_file_contents_str(base_dir / "job_student_bsc.mustache"),
         "job_student_hs": _util.get_file_contents_str(base_dir / "job_student_hs.mustache"),
         "job_coop_videosecurity": _util.get_file_contents_str(base_dir / "job_coop_videosecurity.mustache"),
         "job_coop_weatherdata": _util.get_file_contents_str(base_dir / "job_coop_weatherdata.mustache"),
         "job_coop_touchscreen_repair": _util.get_file_contents_str(base_dir / "job_coop_touchscreen_repair.mustache"),
         "job_coop_network_technician": _util.get_file_contents_str(base_dir / "job_coop_network_technician.mustache"),
         "job_cashier_grocery": _util.get_file_contents_str(base_dir / "job_cashier_grocery.mustache"),
         "job_cashier_electronics": _util.get_file_contents_str(base_dir / "job_cashier_electronics.mustache"),
      },
   );

   response_obj.set_data(response_str);

   return (response_obj);
# fed