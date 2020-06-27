let fn_toggle = function hst_fn_toggle(body_id, display_mode) {
	let body_elm = document.getElementById(body_id);
	let body_style = window.getComputedStyle(body_elm);
	if (body_style.display !== "none") {
		body_elm.style.display = "none";
	} else {
		body_elm.style.display = display_mode;
	}
	return;
}

let fn_post_load = function hst_fn_post_load() {
	for (let body_elm of document.getElementsByClassName("article_body")) {
		fn_toggle(body_elm.id, "block");
	}
	return;
}

document.addEventListener("DOMContentLoaded", fn_post_load, false);
