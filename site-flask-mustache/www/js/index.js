$("#expand-intro").toggle("display");
$("#collapse-intro").fadeIn();

$("#collapse-intro").mouseover(
   function () {
      $("#collapse-intro").tooltip("show");
      return;
   }
);

$("#collapse-intro").mouseout(
   function () {
      $("#collapse-intro").tooltip("hide");
      return;
   }
);

$("#collapse-intro").click(
   function () {
      $("#collapse-intro").tooltip("hide");
      $("#expand-intro").tooltip("hide");
      $("#collapse-intro").toggle("display");
      $("#expand-intro").toggle("display");
      $(".intro_par").toggle("display");
      return false;
   }
);

$("#expand-intro").mouseover(
   function () {
      $("#expand-intro").tooltip("show");
      return;
   }
);

$("#expand-intro").mouseout(
   function () {
      $("#expand-intro").tooltip("hide");
      return;
   }
);

$("#expand-intro").click(
   function () {
      $("#collapse-intro").tooltip("hide");
      $("#expand-intro").tooltip("hide");
      $("#collapse-intro").toggle("display");
      $("#expand-intro").toggle("display");
      $(".intro_par").toggle("display");
      return false;
   }
);

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
