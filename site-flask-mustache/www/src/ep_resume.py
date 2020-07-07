import copy;

import flask;

from . import _base;
from . import _util;
from . import http_request;


app_bp = flask.Blueprint('resume_cv', __name__);


def _get_resume_details():
   """Get the template replacement data for the resume/cv job details.
   """
   data_dct = {
      "job_unemployment": _util.get_file_contents_str("./resume_cv/job_unemployment.mustache"),
      "job_software_engineer_businessintelligence": _util.get_file_contents_str("./resume_cv/job_software_engineer_businessintelligence.mustache"),
      "job_software_engineer_satcom": _util.get_file_contents_str("./resume_cv/job_software_engineer_satcom.mustache"),
      "job_graduate_research_assistant": _util.get_file_contents_str("./resume_cv/job_graduate_research_assistant.mustache"),
      "job_graduate_teaching_assistant": _util.get_file_contents_str("./resume_cv/job_graduate_teaching_assistant.mustache"),
      "job_student_phd": _util.get_file_contents_str("./resume_cv/job_student_phd.mustache"),
      "job_student_msc": _util.get_file_contents_str("./resume_cv/job_student_msc.mustache"),
      "job_student_bsc": _util.get_file_contents_str("./resume_cv/job_student_bsc.mustache"),
      "job_student_hs": _util.get_file_contents_str("./resume_cv/job_student_hs.mustache"),
      "job_coop_videosecurity": _util.get_file_contents_str("./resume_cv/job_coop_videosecurity.mustache"),
      "job_coop_weatherdata": _util.get_file_contents_str("./resume_cv/job_coop_weatherdata.mustache"),
      "job_coop_touchscreen_repair": _util.get_file_contents_str("./resume_cv/job_coop_touchscreen_repair.mustache"),
      "job_coop_network_technician": _util.get_file_contents_str("./resume_cv/job_coop_network_technician.mustache"),
      "job_cashier_grocery": _util.get_file_contents_str("./resume_cv/job_cashier_grocery.mustache"),
      "job_cashier_electronics": _util.get_file_contents_str("./resume_cv/job_cashier_electronics.mustache"),
   };
   return (data_dct);
# fed


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
         "body_theme_class": _base.THEME_CLASSES[body_theme_class]["body"],
         "table_class": _base.THEME_CLASSES[body_theme_class]["table"],
         "btncls_cookies_store": _base.THEME_CLASSES[body_theme_class]["btncls_cookies_store"],
         "btncls_cookies_erase": _base.THEME_CLASSES[body_theme_class]["btncls_cookies_erase"],
         "navbar_class": _base.THEME_CLASSES[body_theme_class]["navbar"],
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
      partials_extra_dct= _get_resume_details(),
   );

   response_obj.set_data(response_str);

   return (response_obj);
# fed
