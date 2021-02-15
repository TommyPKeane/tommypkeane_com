document.querySelectorAll(".popup-launch").forEach(
   function hst_popup_launch_attach(elm) {
      elm.addEventListener(
         "mouseup",
         function hst_popup_launch(event_obj) {
            const dialog_elm = document.getElementById(elm.dataset.popupId); // data-popup-id
            dialog_elm.style.display = "block";
            dialog_elm.setAttribute("aria-hidden", false);
            return;
         },
         false
      );
      return;
   }
);

document.querySelectorAll(".floaty").forEach(
   function hst_popup_close_attach(elm) {
      elm.addEventListener(
         "click",
         function hst_popup_close(event_obj) {
            if (event_obj.target.classList.contains("floaty")) {
               elm.style.display = "none";
               elm.setAttribute("aria-hidden", true);
            }
            return;
         },
         false
      );
      return;
   }
);

var pg_mouse_x = 0;
var pg_mouse_y = 0;
var mouse_pos_style = document.createElement("style");
mouse_pos_style.setAttribute("id", "hover_style")

document.addEventListener(
   "mousemove",
   function doc_mousemove_func(event_obj) {
      pg_mouse_x = event_obj.pageX;
      pg_mouse_y = event_obj.pageY;
      return;
   },
   false
);

document.querySelectorAll(".hoverable").forEach(
   function hst_hoverable_func(elm) {
      elm.addEventListener(
         "mouseover",
         function hst_hoverable_click_func(event_obj) {
            let ref_id = elm.getAttribute("aria-describedby");
            let ref_obj = document.getElementById(ref_id);
            let style_ref_obj = document.getElementById("hover_style");
            if (!style_ref_obj) {
               mouse_pos_style.innerHTML = (
                  `.aria_hover#${ref_id} {\n`
                  + "display: block;\n"
                  + "visibility: visible;\n"
                  + "}"
               );
               ref_obj.parentNode.insertBefore(mouse_pos_style, ref_obj);
               ref_obj.focus();
               mouse_pos_style.innerHTML = (
                  `.aria_hover#${ref_id} {\n`
                  + "display: block;\n"
                  + "visibility: visible;\n"
                  + `top: ${pg_mouse_y - ref_obj.offsetHeight - 10}px;\n`
                  + `left:
                     ${(pg_mouse_x < (window.innerWidth / 2))
                     ? (pg_mouse_x - (ref_obj.offsetWidth / 4))
                     : (pg_mouse_x - (ref_obj.offsetWidth / 3))}px;\n`
                  + "}"
               );
            } else {
               style_ref_obj.remove();
            }
         },
         false
      );
      return;
   }
);

document.addEventListener(
   "mouseout",
   function hst_close_hovers_func(event_obj) {
      if (event_obj.target.className !== "hoverable") {
         let body_elm = document.getElementsByTagName("body")[0];
         let blocks_arr = body_elm.getElementsByTagName("style");
         for (block of blocks_arr) {
            block.remove();
         }
      }
      return;
   },
   false
);


document.querySelector("#expand-intro").toggle("display");
document.querySelector("#collapse-intro").fadeIn();

document.querySelectorAll(".collapser").mouseover(
   function () {
      document.querySelectorAll(".collapser").tooltip("show");
      return;
   }
);

document.querySelectorAll(".collapser").mouseout(
   function () {
      document.querySelectorAll(".collapser").tooltip("hide");
      return;
   }
);

document.querySelector(".collapser").click(
   function () {
      document.querySelector(".collapser").tooltip("hide");
      document.querySelector("#expand-intro").tooltip("hide");
      document.querySelector("#expand-intro").toggle("display");
      document.querySelector(".intro .billet-body").toggle("display");
      return false;
   }
);

document.querySelector("#expand-intro").mouseover(
   function () {
      document.querySelector("#expand-intro").tooltip("show");
      return;
   }
);

document.querySelector("#expand-intro").mouseout(
   function () {
      document.querySelector("#expand-intro").tooltip("hide");
      return;
   }
);

$("#expand-intro").click(
   function () {
      document.querySelector(".collapser").tooltip("hide");
      document.querySelector("#expand-intro").tooltip("hide");
      document.querySelector(".collapser").toggle("display");
      document.querySelector("#expand-intro").toggle("display");
      document.querySelector(".intro .billet-body").toggle("display");
      return false;
   }
);

document.querySelector(function () {
  document.querySelector('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(
   function hst_ready_func() {
      for (let elm of document.getElementsByClassName("spinner-border")) {
         elm.style.display = "none";
      }
      window.scroll(
         function hst_window_scroll_func() {
            if (this.scrollTop() > 300) {
                document.querySelector("#back-to-top").fadeIn();
            } else {
                document.querySelector("#back-to-top").fadeOut();
            }
         }
      );
      document.querySelector("#back-to-top").click(
         function () {
            document.querySelector("body,html").animate(
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
