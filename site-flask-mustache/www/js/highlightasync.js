addEventListener("load", () => {
   const code = document.querySelector("code");
   const worker = new Worker("/js/highlightworker.js");
   worker.onmessage = (event) => { code.innerHTML = event.data; }
   worker.postMessage(code.textContent);
   return;
});