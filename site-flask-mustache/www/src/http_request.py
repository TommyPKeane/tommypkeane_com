import copy;
import os;

import commonmark;
import flask;
import yaml;

from . import _base;
from . import _util;

icon_data_dct = {
   # FEATHER ICONS
   "icon_bitbucket": _util.get_file_contents_str("./img/feather/droplet.svg"),
   "icon_google_scholar": _util.get_file_contents_str("./img/feather/award.svg"),
   "icon_instagram": _util.get_file_contents_str("./img/feather/instagram.svg"),
   "icon_facebook": _util.get_file_contents_str("./img/feather/facebook.svg"),
   "icon_twitter": _util.get_file_contents_str("./img/feather/twitter.svg"),
   "icon_linkedin": _util.get_file_contents_str("./img/feather/linkedin.svg"),
   "icon_raspberrypi": _util.get_file_contents_str("./img/feather/cpu.svg"),
   "icon_pinetime": _util.get_file_contents_str("./img/feather/watch.svg"),
   "icon_pinephone": _util.get_file_contents_str("./img/feather/phone.svg"),
   "icon_contact": _util.get_file_contents_str("./img/feather/phone.svg"),
   "exif_icon": _util.get_file_contents_str("./img/feather/film.svg"),
   "fullsize_icon": _util.get_file_contents_str("./img/feather/external-link.svg"),
   "icon_synth": _util.get_file_contents_str("./img/feather/music.svg"),
   # TOMMYTOFU ICONS
   "icon_home": _util.get_file_contents_str("./img/tommytofu/home-cabin-a.svg"),
   "icon_cv_resume": _util.get_file_contents_str("./img/tommytofu/skull-round-a.svg"),
   "icon_books": _util.get_file_contents_str("./img/tommytofu/book-closed.svg"),
   "icon_settings": _util.get_file_contents_str("./img/tommytofu/config.svg"),
   "icon_other_sites": _util.get_file_contents_str("./img/tommytofu/menu.svg"),
   "icon_github": _util.get_file_contents_str("./img/tommytofu/git-octocat.svg"),
   "icon_photography": _util.get_file_contents_str("./img/tommytofu/camera-photo.svg"),
   "img_scroll_to_top": _util.get_file_contents_str("./img/tommytofu/bracket-angle-d-up.svg"),
   "img_intro_collapse": _util.get_file_contents_str("./img/tommytofu/bracket-angle-d-up.svg"),
   "img_intro_expand": _util.get_file_contents_str("./img/tommytofu/bracket-angle-d-dn.svg"),
   # OTHERS
   "ico_png_file": "/img/tommypkeane-com_ico_circle-t.png",
   "ico_ico_file": "/img/tommypkeane-com_ico_circle-t.ico",
};


def _get_template_data_icons():
   """Get the template replacement data for the common site navbar.
   """
   return (icon_data_dct);
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
               "theme_class": _base.THEME_CLASSES[theme_class],
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
         ) = func(theme_class, *args, **kwargs);

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

   article_content_dct["page_topic"] = yaml_config["page_topic"];
   article_content_dct["page_name"] = yaml_config["page_name"];

   intro_file = os.path.join(
      yaml_config["src_dir"],
      yaml_config["intro"]["filename"],
   );

   with open(intro_file, "r") as file_obj:
      ast_obj = parser_obj.parse(
         file_obj.read(),
      );
   # htiw

   article_content_dct[
      yaml_config["intro"]["template_key"]
   ] = html_renderer.render(ast_obj);

   article_content_dct["intro_title"] = yaml_config["intro_title"];
   article_content_dct["intro_subtitle"] = yaml_config["intro_subtitle"];

   article_content_dct["toc"] = [];
   article_content_dct["content"] = [];

   template_file = yaml_config["template"];


   if (yaml_config["content"] is None):
      pass;
   else:
      for content in yaml_config["content"]:
         config_file = os.path.join(
            yaml_config["src_dir"],
            content["filename"],
         );

         with open(config_file, "r") as file_obj:
            ast_obj = parser_obj.parse(
               file_obj.read(),
            );
         # htiw

         article_content_dct["content"].append(
            {
               "article_id": content["article_id"],
               "article_title": content["article_title"],
               "article": html_renderer.render(ast_obj),
            },
         );

         article_content_dct["toc"].append(
            {
               "article_id": content["article_id"],
               "article_title": content["article_title"],
               "subtitles": content["subtitles"],
            },
         );
      # rof
   #fi

   if (yaml_config["raw_content_key"] is None):
      pass;
   else:
      article_content_dct[
         yaml_config["raw_content_key"]
      ] = yaml_config["raw_content"];
   # fi

   return (article_content_dct, template_file,);
# fed
