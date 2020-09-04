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


main_dir = pathlib.Path("./src/templates");
content_dir = (main_dir / "resume_cv");


app_bp = flask.Blueprint("resume_cv", __name__);

site_author = "Tommy P. Keane";

resume_css_lst = [
   { "cssname": "/css/resume-cv.css",        "mode": _base.MODE_ANY },
   { "cssname": "/css/resume-cv-dark.css",   "mode": _base.MODE_DARK },
   { "cssname": "/css/resume-cv-lite.css",   "mode": _base.MODE_LITE },
   { "cssname": "/css/resume-cv-vapr.css",   "mode": _base.MODE_VAPR },
   { "cssname": "/css/resume-cv-cpnk.css",   "mode": _base.MODE_CPNK },
];

resume_js_lst = [
   { "scriptname": "/js/cvtimeline.js", },
];


@app_bp.route("/business", methods=["GET",],)
@app_bp.route("/professional", methods=["GET",],)
@app_bp.route("/resume", methods=["GET",],)
@app_bp.route("/business/", methods=["GET",],)
@app_bp.route("/professional/", methods=["GET",],)
@app_bp.route("/resume/", methods=["GET",],)
@app_bp.route("/resume.html", methods=["GET",],)
@app_bp.route("/resume.htm", methods=["GET",],)
@http_request.html_response(
   css_lst= resume_css_lst,
   js_lst= resume_js_lst,
   title= "Resumé / CV (www.tommypkeane.com)",
   description= "History and Details of Professional Experience of Tommy P. Keane, Data Scientist and Software Engineer.",
   author= site_author,
   partials_dct= {
      "job_unemployment": _util.get_file_contents_str(content_dir / "job_unemployment.mustache"),
      "job_software_engineer_businessintelligence": _util.get_file_contents_str(content_dir / "job_software_engineer_businessintelligence.mustache"),
      "job_software_engineer_satcom": _util.get_file_contents_str(content_dir / "job_software_engineer_satcom.mustache"),
      "job_graduate_research_assistant": _util.get_file_contents_str(content_dir / "job_graduate_research_assistant.mustache"),
      "job_graduate_teaching_assistant": _util.get_file_contents_str(content_dir / "job_graduate_teaching_assistant.mustache"),
      "job_student_phd": _util.get_file_contents_str(content_dir / "job_student_phd.mustache"),
      "job_student_msc": _util.get_file_contents_str(content_dir / "job_student_msc.mustache"),
      "job_student_bsc": _util.get_file_contents_str(content_dir / "job_student_bsc.mustache"),
      "job_student_hs": _util.get_file_contents_str(content_dir / "job_student_hs.mustache"),
      "job_coop_videosecurity": _util.get_file_contents_str(content_dir / "job_coop_videosecurity.mustache"),
      "job_coop_weatherdata": _util.get_file_contents_str(content_dir / "job_coop_weatherdata.mustache"),
      "job_coop_touchscreen_repair": _util.get_file_contents_str(content_dir / "job_coop_touchscreen_repair.mustache"),
      "job_coop_network_technician": _util.get_file_contents_str(content_dir / "job_coop_network_technician.mustache"),
      "job_cashier_grocery": _util.get_file_contents_str(content_dir / "job_cashier_grocery.mustache"),
      "job_cashier_electronics": _util.get_file_contents_str(content_dir / "job_cashier_electronics.mustache"),
   },
)
def ep_resume_cv(theme_class):
   """Provide the response for the Business/Resumé endpoint.
   """
   content_dct = dict();
   content_dct.update(
      {
         "resume_cv_timeline": _util.get_file_contents_str("./img/cv_timeline_plain.svg"),
      }
   );


   template_file = (main_dir / "resume.mustache");

   return (content_dct, template_file,);
# fed
