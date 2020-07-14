onmessage = (event) => {
  importScripts("/js/hightlight/highlight.pack.js");
  const result = self.hljs.highlightAuto(event.data);
  postMessage(result.value);
  return;
};