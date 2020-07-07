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



def generate_html_common(source_file, data_dct, partials_extra_dct= None):
   partials_dct = {
      "header_contents": _util.get_file_contents_str("header_contents.mustache"),
      "footer_contents": _util.get_file_contents_str("footer_contents.mustache"),
   };

   contents_str = _util.generate_html(source_file, data_dct, partials_dct, partials_extra_dct,);

   return (contents_str);
# fed
