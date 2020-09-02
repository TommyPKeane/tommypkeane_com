# @file
# @brief Image Links, Functions, and Raw SVG Strings
# 
# This module provides "cached" image data or links. For SVG files that are
# going to be embedded in site pages as raw strings, this module will read-in
# all files once at the flask-app startup to "cache" the image data as valid
# XML (SVG) strings.
# 
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2020, Tommy P. Keane

from . import _util;


icon_data_dct = {
   # FEATHER ICONS
   "icon_bitbucket": _util.get_file_contents_str("./img/feather/droplet.svg"),
   "icon_google_scholar": _util.get_file_contents_str("./img/feather/award.svg"),
   "icon_instagram": _util.get_file_contents_str("./img/feather/instagram.svg"),
   "icon_facebook": _util.get_file_contents_str("./img/feather/facebook.svg"),
   "icon_twitter": _util.get_file_contents_str("./img/feather/twitter.svg"),
   "icon_linkedin": _util.get_file_contents_str("./img/feather/linkedin.svg"),
   "fullsize_icon": _util.get_file_contents_str("./img/feather/external-link.svg"),
   "icon_synth": _util.get_file_contents_str("./img/feather/music.svg"),
   # TOMMYTOFU ICONS
   "icon_contact": _util.get_file_contents_str("./img/tommytofu/help-01.svg"),
   "icon_cellular_automata": _util.get_file_contents_str("./img/tommytofu/cellular-automata-glider-0.svg"),
   "icon_raspberrypi": _util.get_file_contents_str("./img/tommytofu/circuit-board.svg"),
   "icon_pinetime": _util.get_file_contents_str("./img/tommytofu/watch.svg"),
   "icon_pinephone": _util.get_file_contents_str("./img/tommytofu/phone.svg"),
   "exif_icon": _util.get_file_contents_str("./img/tommytofu/camera-photo.svg"),
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
