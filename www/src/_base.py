# @file
# @brief Base Module of Variables and Constants
#
# This is a module of primitive constants and variables that are meant to be
# used anywhere else in the codebase. Since there's no real "theme" or any kind
# of specificity to the content in this module, we've just named it `_base` to
# indicate that anything in here is really basic/foundational.
#
# @author Tommy P. Keane
# @email talk@tommypkeane.com
# @copyright 2020, Tommy P. Keane

TWO_WEEKS_SECONDS = 1_209_600;

MODE_ANY = "any";
MODE_DARK = "dark"; # Dark Mode
MODE_LITE = "lite"; # Light Mode
MODE_CPNK = "cpnk"; # Seapunk
MODE_VAPR = "vapr"; # Vaporwave

THEME_CLASSES = {
   "default":        MODE_LITE,
   "light_on_dark":  MODE_DARK,
   "dark_on_light":  MODE_LITE,
   "seapunk":        MODE_CPNK,
   "vaporwave":      MODE_VAPR,
};

BASE_STYLESHEETS = [
   { "cssname": "/css/theme.css",          "mode": MODE_ANY, },
   { "cssname": "/css/theme-lite.css",     "mode": MODE_LITE, },
   { "cssname": "/css/theme-dark.css",     "mode": MODE_DARK, },
   { "cssname": "/css/theme-cpnk.css",     "mode": MODE_CPNK, },
   { "cssname": "/css/theme-vapr.css",     "mode": MODE_VAPR, },
   { "cssname": "/css/mise-en-place.css",    "mode": MODE_ANY, },
];

BASE_SCRIPTS = [
   { "scriptname": "/js/libs/jquery/jquery.min.js", },
   { "scriptname": "/js/libs/d3/d3.min.js", },
   { "scriptname": "/js/mise-en-place.js", },
   { "scriptname": "/js/cookie.js", },
   # { "scriptname": "/js/index.js", },
];
