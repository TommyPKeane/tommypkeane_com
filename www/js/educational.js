document.addEventListener("DOMContentLoaded", (event) => {
   hljs.initHighlightingOnLoad();
   hljs.initLineNumbersOnLoad({
      singleLine: true
   });
   document.querySelectorAll("pre code").forEach((block) => {
      // hljs.highlightBlock(block);
      hljs.lineNumbersBlock(block, {"singleLine": true});
   });
});
