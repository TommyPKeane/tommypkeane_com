let settings_page_load = function hst_settings_page_load() {
   for (let elm of document.getElementsByClassName("spinner-border")) {
      elm.style.display = "none";
   }
   return;
}

window.onload = settings_page_load;
