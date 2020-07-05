$(document).ready(
   function hst_ready_func() {
      $(window).scroll(
         function hst_window_scroll_func() {
            if ($(this).scrollTop() > 50) {
                $("#back-to-top").fadeIn();
            } else {
                $("#back-to-top").fadeOut();
            }
         }
      );
      $("#back-to-top").click(
         function () {
            $("#back-to-top").tooltip("hide");
            $("body,html").animate(
               {
                  "scrollTop": 0
               },
               400
            );
            return false;
         }
      );
      $("#back-to-top").tooltip("show");
   }
);
