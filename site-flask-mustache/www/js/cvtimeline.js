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

let block_to_details_map = {
   "block_grocery": "job_grocery",
   "block_electronics": "job_electronics",
   "block_networking": "job_networktech",
   "block_hs": "job_student_hs",
   "block_bsc": "job_student_bsc",
   "block_msc": "job_student_msc",
   "block_phd": "job_student_phd",
   "block_sw_bi": "job_software_engineer_bi",
   "block_grad_teaching": "job_assistant_teaching",
   "block_grad_research": "job_assistant_research",
   "block_touchscreen": "job_touchscreen",
   "block_security": "job_videosecurity",
   "block_satcom": "job_satcom",
   "block_weather": "job_weather",
   "unemployment": "job_furlough"
}

let hide_jobs = function hst_hide_jobs() {
   for (let block_div of document.getElementsByClassName("job-container")) {
      block_div.style.display = "none";
   }
   return;
}

let hide_title = function hst_hide_title(clicked_elm_id) {
   let title_hover_div = document.getElementById("hover_title");
   title_hover_div.style.visibility = "hidden";
   return;
}

let reveal_title = function hst_reveal_title(clicked_elm_id) {
   let hovered_block = document.getElementById(
      block_to_details_map[clicked_elm_id]
   );
   let title_hover_div = document.getElementById("hover_title");
   title_hover_div.innerHTML = hovered_block.getElementsByClassName("card-title")[0].innerHTML;
   title_hover_div.style.visibility = "visible";
   return;
}

let hide_info = function hst_hide_info(clicked_elm_id) {
   let selected_block = document.getElementById(
      block_to_details_map[clicked_elm_id]
   );
   selected_block.style.display = "none";
   return;
}

let reveal_info = function hst_reveal_info(clicked_elm_id) {
   hide_jobs();
   let selected_block = document.getElementById(
      block_to_details_map[clicked_elm_id]
   );
   selected_block.style.display = "block";
   $("body,html").animate(
      {
         "scrollTop": $(selected_block).offset().top
      },
      250
   );
   return;
}

window.onload = hide_jobs;

let $mouseX = 0;
let $mouseY = 0;
let $xp = 0;
let $yp = 0;
let drag_factor = 2;

$(document).mousemove(
   function(e) {
      $mouseX = e.pageX;
      $mouseY = e.pageY;    
   }
);

var $loop = setInterval(
   function() {
      $xp += (($mouseX - $xp) / drag_factor);
      $yp += (($mouseY - $yp) / drag_factor);
      $("#hover_title").css(
         {
            "left": $xp - 40 +'px',
            "top": $yp - 50 +'px'
         }
      );
   },
   30
);
