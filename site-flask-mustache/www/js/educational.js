document.addEventListener("DOMContentLoaded", (event) => {
   hljs.initHighlightingOnLoad();
   hljs.initLineNumbersOnLoad();
   document.querySelectorAll("pre code").forEach((block) => {
      // hljs.highlightBlock(block);
      hljs.lineNumbersBlock(block);
   });
});
