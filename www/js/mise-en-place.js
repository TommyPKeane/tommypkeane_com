let pg_mouse_x = 0;
let pg_mouse_y = 0;
let mouse_pos_style = document.createElement("style");
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
         "click",
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
                  + `top: ${pg_mouse_y - ref_obj.offsetHeight - 20}px;\n`
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
   "click",
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