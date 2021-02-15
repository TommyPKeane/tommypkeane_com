import copy;

import flask;

from . import (
   _base,
   _util,
   http_request,
);


app_bp = flask.Blueprint('cookies', __name__);

@app_bp.route('/set/cookie', methods=["POST",])
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
      max_age= (0 if (theme_value == "") else _base.TWO_WEEKS_SECONDS),
      path= "/",
      secure= False,
      httponly= True,
      samesite= "Lax",
   );

   response_obj.set_cookie(
      "gdpr_consent_date",
      value= gdpr_consent_date_value,
      max_age= (0 if (gdpr_consent_date_value == "") else _base.TWO_WEEKS_SECONDS),
      path= "/",
      secure= False,
      httponly= True,
      samesite= "Lax",
   );

   return (response_obj);
# fed
