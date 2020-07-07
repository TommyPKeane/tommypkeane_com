let cookie_submit = function hst_cookie_submit() {
   let spinner = document.getElementById("id_button_spin_set_cookies");
   spinner.style.display = "inline-block";

   let button = document.getElementById("id_button_set_cookies");
   button.disabled = true;

   let theme_elm = document.getElementById("id_theme_choice");
   let gdpr_consent_dt = new Date();

   let req_obj = new XMLHttpRequest();
   req_obj.open("POST", "/set/cookie");
   req_obj.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
   req_obj.onreadystatechange = function () {
      if (req_obj.readyState === 4) {
         button.disabled = false;
         spinner.style.display = "none";
         location.reload();
      }
      return;
   }
   
   req_obj.send(
      JSON.stringify(
         {
            "theme": theme_elm.value,
            "gdpr_consent": gdpr_consent_dt.toISOString()
         }
      )
   );
   return;
}

let cookie_erase = function hst_cookie_erase() {
   let spinner = document.getElementById("id_button_spin_erase_cookies");
   spinner.style.display = "inline-block";

   let button = document.getElementById("id_button_erase_cookies");
   button.disabled = true;

   let theme_elm = document.getElementById("id_theme_choice");
   let gdpr_consent_dt = new Date();

   let req_obj = new XMLHttpRequest();
   req_obj.open("POST", "/set/cookie");
   req_obj.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
   req_obj.onreadystatechange = function () {
      if (req_obj.readyState === 4) {
         button.disabled = false;
         spinner.style.display = "none";
         location.reload();
      }
      return;
   }

   req_obj.send(
      JSON.stringify(
         {
            "theme": "",
            "gdpr_consent": ""
         }
      )
   );
   return;
}
