$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(
   function hst_ready_func() {
      for (let elm of document.getElementsByClassName("spinner-border")) {
         elm.style.display = "none";
      }
      $(window).scroll(
         function hst_window_scroll_func() {
            if ($(this).scrollTop() > 300) {
                $("#back-to-top").fadeIn();
            } else {
                $("#back-to-top").fadeOut();
            }
         }
      );
      $("#back-to-top").click(
         function () {
            $("body,html").animate(
               {
                  "scrollTop": 0
               },
               400
            );
            return false;
         }
      );
   }
);
