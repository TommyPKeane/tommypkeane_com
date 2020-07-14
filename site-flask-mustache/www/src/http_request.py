import copy;
import os;

import commonmark;
import flask;
import yaml;

from . import _base;
from . import _util;


def _get_template_data_icons():
   """Get the template replacement data for the common site navbar.
   """
   data_dct = {
      # FEATHER ICONS
      "icon_home": _util.get_file_contents_str("./img/feather/home.svg"),
      "icon_about_me": _util.get_file_contents_str("./img/feather/smile.svg"),
      "icon_cv_resume": _util.get_file_contents_str("./img/feather/briefcase.svg"),
      "icon_bitbucket": _util.get_file_contents_str("./img/feather/droplet.svg"),
      "icon_google_scholar": _util.get_file_contents_str("./img/feather/award.svg"),
      "icon_instagram": _util.get_file_contents_str("./img/feather/instagram.svg"),
      "icon_facebook": _util.get_file_contents_str("./img/feather/facebook.svg"),
      "icon_twitter": _util.get_file_contents_str("./img/feather/twitter.svg"),
      "icon_linkedin": _util.get_file_contents_str("./img/feather/linkedin.svg"),
      "icon_projects_hw": _util.get_file_contents_str("./img/feather/tool.svg"),
      "icon_raspberrypi": _util.get_file_contents_str("./img/feather/cpu.svg"),
      "icon_odroid": _util.get_file_contents_str("./img/feather/cpu.svg"),
      "icon_pinetime": _util.get_file_contents_str("./img/feather/watch.svg"),
      "icon_pinephone": _util.get_file_contents_str("./img/feather/phone.svg"),
      "icon_projects_sw": _util.get_file_contents_str("./img/feather/tool.svg"),
      "icon_publications": _util.get_file_contents_str("./img/feather/file-text.svg"),
      "img_scroll_to_top": _util.get_file_contents_str("./img/feather/chevrons-up.svg"),
      "img_intro_collapse": _util.get_file_contents_str("./img/feather/chevrons-up.svg"),
      "img_intro_expand": _util.get_file_contents_str("./img/feather/chevrons-down.svg"),
      "icon_contact": _util.get_file_contents_str("./img/feather/phone.svg"),
      "exif_icon": _util.get_file_contents_str("./img/feather/film.svg"),
      "fullsize_icon": _util.get_file_contents_str("./img/feather/external-link.svg"),
      # TOMMYTOFU ICONS
      "icon_settings": _util.get_file_contents_str("./img/tommytofu/config.svg"),
      "icon_other_sites": _util.get_file_contents_str("./img/tommytofu/menu.svg"),
      "icon_github": _util.get_file_contents_str("./img/tommytofu/git-octocat.svg"),
      "icon_photography": _util.get_file_contents_str("./img/tommytofu/camera-photo.svg"),
      # OTHERS
      "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
   };
   return (data_dct);
# fed



def generate_html_common(
      source_file,
      data_dct,
      partials_extra_dct= None,
   ):
   """Create an HTML Response String with common Header and Footer contents.
   """
   partials_dct = {
      "header_contents": _util.get_file_contents_str("./src/templates/header_contents.mustache"),
      "footer_contents": _util.get_file_contents_str("./src/templates/footer_contents.mustache"),
   };

   contents_str = _util.generate_html(
      source_file,
      data_dct,
      partials_dct,
      partials_extra_dct,
   );

   return (contents_str);
# fed


def html_response(css_lst, js_lst, title, description, author,):

   def argumentless_wrapper(func,):

      def inner_call(*args, **kwargs):
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
         stylesheets_lst.extend(css_lst);

         scripts_lst = copy.deepcopy(_base.BASE_SCRIPTS);
         scripts_lst.extend(js_lst);

         template_data = dict();
         template_data.update(
            _get_template_data_icons()
         );
         template_data.update(
            {
               "title": title,
               "description": description,
               "author": author,
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

         (
           content_dct,
           template_file,
         ) = func(body_theme_class, *args, **kwargs);

         template_data.update(content_dct);

         response_str = generate_html_common(
            template_file,
            template_data,
         );

         response_obj.set_data(response_str);

         return (response_obj);
      # fed

      inner_call.__name__ = (func.__name__);

      return (inner_call);
   # fed

   return (argumentless_wrapper);
# fed


def parse_content_config(filename):

   parser_obj = commonmark.Parser();
   html_renderer = commonmark.HtmlRenderer();
   ast_obj = None;

   article_content_dct = dict();
   yaml_config = None;

   with open(filename, "r") as file_obj:

      yaml_config = yaml.safe_load(file_obj.read());

   # htiw

   template_file = None;

   for article in yaml_config["entries"]:

      template_file = os.path.join(
         yaml_config["src_dir"],
         article["template"],
      );

      for content in article["content"]:

         config_file = os.path.join(
            yaml_config["src_dir"],
            content["filename"],
         );

         with open(config_file, "r") as file_obj:

            ast_obj = parser_obj.parse(
               file_obj.read(),
            );

         # htiw

         article_content_dct[content["template_key"]] = html_renderer.render(ast_obj);

      # rof

      if ("raw_content_key" in article):

         article_content_dct[article["raw_content_key"]] = article["raw_content"];

      else:

         pass;

      # fi

   # rof

   return (article_content_dct, template_file,);
# fed
