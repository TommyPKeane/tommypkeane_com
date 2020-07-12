let getphoto = function hst_getphoto(url_str) {
   window.open(url_str, "_blank");
   return;
}

$(document).ready(
   function hst_ready_func() {
      $('.carousel').carousel(
         {
            "interval": false,
            "keyboard": true,
            "wrap": true,
            "touch": true
         }
      )
      $(".carousel-item")[0].className += " active";

      return;
   }
);
