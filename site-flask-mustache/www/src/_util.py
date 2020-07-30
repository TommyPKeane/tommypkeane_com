import pystache;


def get_file_contents_str(filename,):
   """Get the SVG XML as a string, for raw injection into document.
   """
   contents_str = None;
   with open(filename, "r") as file_obj:
      contents_str = file_obj.read();
   # htiw
   return (contents_str);
# fed


def generate_html(source_file, data_dct, partials_dct, partials_extra_dct= None):
   """Generate HTML from a Mustache File and Data Dictionary.
   Args:
      source_file (str, path-like): Path to Mustache file, including filename.
      data_dct (dict): Dictionary of template replacements.
   Returns:
      A string of valid HTML contents after parsing the Mustache file and
      filling in the replacement contents from the data dictionary.
   """

   if not (partials_extra_dct is None):
      partials_dct.update(partials_extra_dct);
   # fi

   stache_compiler = pystache.Renderer(
      partials= partials_dct,
   );

   raw_str = None;

   with open(source_file, "r") as file_obj:
      raw_str = file_obj.read();
   # htiw

   parsed_str = pystache.parse(raw_str);

   html_str = stache_compiler.render(
      parsed_str,
      data_dct,
   );

   return (html_str);
# fed
