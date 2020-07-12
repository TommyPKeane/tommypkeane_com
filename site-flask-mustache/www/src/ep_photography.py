import copy;
import os;

import flask;

from PIL import Image as PillowImage;
from PIL.ExifTags import TAGS as ExifTags;
from PIL import TiffImagePlugin;

from . import (
   _base,
   _util,
   http_request,
);


app_bp = flask.Blueprint('photography', __name__);


def _get_exif_info(img_file):
   exif_info_lst = [];

   img_obj = PillowImage.open(img_file);
   exif_obj = img_obj._getexif();

   for (key, val) in exif_obj.items():
      exifkey = ExifTags.get(key);
      exif_info_lst.append(
         {
            "key": (exifkey.encode("utf-8") if not exifkey is None else "[None]"),
            "val": (
               str(val)
               if not isinstance(val, bytes)
               else
                  "[Redacted Hex String]"
                  # " ".join(
                  #    [
                  #       (
                  #          "0x{0:s}".format(val.hex()[i:(i + 2):1])
                  #       )
                  #       for i in range(0, len(val.hex()), 2)
                  #    ]
                  # )
            ),
         }
      );
   # rof

   img_obj.close();

   return (exif_info_lst);
# fed


def _get_filesize(file_str):
   filesize_bytes = os.path.getsize(file_str);
   filesize_mib = (filesize_bytes / 1024 / 1024);
   return ("{0:0.02f}".format(filesize_mib));
# fed


@app_bp.route("/photography", methods=["GET",],)
@app_bp.route("/photography.html", methods=["GET",],)
@app_bp.route("/photography.htm", methods=["GET",],)
def photography():
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
   stylesheets_lst.append({"cssname": "/css/photography.css",});
   stylesheets_lst.append({"cssname": "/css/photography-light.css",});
   stylesheets_lst.append({"cssname": "/css/photography-dark.css",});

   scripts_lst = copy.deepcopy(_base.BASE_SCRIPTS);
   scripts_lst.append({"scriptname": "/js/photography.js",});

   template_data = dict();
   template_data.update(
      http_request._get_template_data_icons()
   );
   template_data.update(
      {
         "title": "Photography (www.tommypkeane.com)",
         "description": "Hobby Photography and Captions by Tommy P. Keane, for entertainment or Computer-Vision research.",
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
   template_data.update(
      {
         "carouselphotos": [
            {
               "src": "/photos/20160611_Carol_0960w.jpg",
               "alt": "Lens flare and light glare through glazed window.",
               "caption_title": "\"Lisa 💡 Carol 💡 Fremont 💡\"",
               "caption_par": "black-and-white photo at night of a parking-lot streetlight through a window with privacy/glazing sheeting over the glass",
               "src_fullsize": "/photos/20160611_Carol_2752w.jpg",
               "filename": "20160611_Carol_2752w.jpg",
               "filesize": _get_filesize("./photos/20160611_Carol_2752w.jpg"),
               "exif_info": _get_exif_info("./photos/20160611_Carol_2752w.jpg"),
               "modal_id": "carol",
            },
            {
               "src": "/photos/20160703_Mushroom_0960w.jpg",
               "alt": "Sunset photo along Interstate-Highway I-90, USA.",
               "caption_title": "\"A Rare Gift\"",
               "caption_par": "occasionally i drop a teacup to shatter on the floor, on purpose. i'm not satisfied when it doesn't gather itself up again.",
               "src_fullsize": "/photos/20160703_Mushroom_2752w.jpg",
               "filename": "20160703_Mushroom_2752w.jpg",
               "filesize": _get_filesize("./photos/20160703_Mushroom_2752w.jpg"),
               "exif_info": _get_exif_info("./photos/20160703_Mushroom_2752w.jpg"),
               "modal_id": "mushroom",
            },
            {
               "src": "/photos/20160702_SummerPurfle_0960w.jpg",
               "alt": "Lens flare and light glare photo of sun along Interstate-Highway I-90, USA.",
               "caption_title": "\"Summer Purfle\"",
               "caption_par": "sweat's a summer purfle.",
               "src_fullsize": "/photos/20160702_SummerPurfle_4896w.jpg",
               "filename": "20160702_SummerPurfle_4896w.jpg",
               "filesize": _get_filesize("./photos/20160702_SummerPurfle_4896w.jpg"),
               "exif_info": _get_exif_info("./photos/20160702_SummerPurfle_4896w.jpg"),
               "modal_id": "summerpurfle",
            },
            {
               "src": "/photos/20160806_RockyRoad_0960w.jpg",
               "alt": "Photo of carve-out alongside Interstate-Highway I-90, USA.",
               "caption_title": "\"Rocky Road\"",
               "caption_par": "ice-cream <i>is</i> real...",
               "src_fullsize": "/photos/20160806_RockyRoad_4896w.jpg",
               "filename": "20160806_RockyRoad_4896w.jpg",
               "filesize": _get_filesize("./photos/20160806_RockyRoad_4896w.jpg"),
               "exif_info": _get_exif_info("./photos/20160806_RockyRoad_4896w.jpg"),
               "modal_id": "rockyroad",
            },
            {
               "src": "/photos/20160807_ConspiracyTheory_0960w.jpg",
               "alt": "Photo of sky alongside Interstate-Highway I-90, USA.",
               "caption_title": "\"Out There\"",
               "caption_par": "this is how conspiracy theories get started.",
               "src_fullsize": "/photos/20160807_ConspiracyTheory_4896w.jpg",
               "filename": "20160807_ConspiracyTheory_4896w.jpg",
               "filesize": _get_filesize("./photos/20160807_ConspiracyTheory_4896w.jpg"),
               "exif_info": _get_exif_info("./photos/20160807_ConspiracyTheory_4896w.jpg"),
               "modal_id": "conspiracy",
            },
            {
               "src": "/photos/20170315_CCR_0960w.jpg",
               "alt": "Chromatically-modified photo of a side-street during winter in an upstate NY, USA urban-suburb.",
               "caption_title": "\"YCbCr\"",
               "caption_par": "doo, doo, doo, lookin' out my back door.",
               "src_fullsize": "/photos/20170315_CCR_5184w.jpg",
               "filename": "20170315_CCR_5184w.jpg",
               "filesize": _get_filesize("./photos/20170315_CCR_5184w.jpg"),
               "exif_info": _get_exif_info("./photos/20170315_CCR_5184w.jpg"),
               "modal_id": "ccr",
            },
            {
               "src": "/photos/IMG_4275_0960w.jpg",
               "alt": "Photo of clouds somewhere in upstate NY, USA.",
               "caption_title": "\"Clouds (A)\"",
               "caption_par": "doesn't really seem that difficult.",
               "src_fullsize": "/photos/IMG_4275.jpg",
               "filename": "IMG_4275.jpg",
               "filesize": _get_filesize("./photos/IMG_4275.jpg"),
               "exif_info": _get_exif_info("./photos/IMG_4275.jpg"),
               "modal_id": "clouds_a",
            },
            {
               "src": "/photos/20130624_SoClose_0960w.jpg",
               "alt": "Photo of a bathrom full of urinals with dividers except one corner, in Reno, NV, USA.",
               "caption_title": "\"So Close\"",
               "caption_par": "i'd say \"you had one job\", but actually most mistakes are done by committee.",
               "src_fullsize": "/photos/20130624_SoClose.jpg",
               "filename": "20130624_SoClose.jpg",
               "filesize": _get_filesize("./photos/20130624_SoClose.jpg"),
               "exif_info": _get_exif_info("./photos/20130624_SoClose.jpg"),
               "modal_id": "soclose",
            },
            {
               "src": "/photos/20161230_ChristmasGhost_01_0960w.jpg",
               "alt": "_",
               "caption_title": "\"Christmas Ghost (01)\"",
               "caption_par": "tron heresy",
               "src_fullsize": "/photos/20161230_ChristmasGhost_01.jpg",
               "filename": "20161230_ChristmasGhost_01.jpg",
               "filesize": _get_filesize("./photos/20161230_ChristmasGhost_01.jpg"),
               "exif_info": _get_exif_info("./photos/20161230_ChristmasGhost_01.jpg"),
               "modal_id": "christmasghost01",
            },
            {
               "src": "/photos/20161230_ChristmasGhost_02_0960w.jpg",
               "alt": "_",
               "caption_title": "\"Christmas Ghost (02)\"",
               "caption_par": "does anyone else see a cow head?",
               "src_fullsize": "/photos/20161230_ChristmasGhost_02.jpg",
               "filename": "20161230_ChristmasGhost_02.jpg",
               "filesize": _get_filesize("./photos/20161230_ChristmasGhost_02.jpg"),
               "exif_info": _get_exif_info("./photos/20161230_ChristmasGhost_02.jpg"),
               "modal_id": "christmasghost02",
            },
            {
               "src": "/photos/20160920_PowerToPower_0960w.jpg",
               "alt": "_",
               "caption_title": "\"Power 2 Power\"",
               "caption_par": "dissipation unto dish-anticipation",
               "src_fullsize": "/photos/20160920_PowerToPower.jpg",
               "filename": "20160920_PowerToPower.jpg",
               "filesize": _get_filesize("./photos/20160920_PowerToPower.jpg"),
               "exif_info": _get_exif_info("./photos/20160920_PowerToPower.jpg"),
               "modal_id": "christmasghost02",
            },
         ],
      }
   );

   response_str = http_request.generate_html_common(
      "./src/templates/photography.mustache",
      template_data,
   );

   response_obj.set_data(response_str);

   return (response_obj);
# fed
