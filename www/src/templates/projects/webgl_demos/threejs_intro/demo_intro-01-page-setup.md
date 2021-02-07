__Three.js__ is a free and open-source library for WebGL-based web-development.

Here, we go over the basics of first setting-up a site, like this one, to utilize __Three.js__ and display a WebGL Viewport with a `<canvas>` DOM element in a contemporary web-browser. As relatively simple as it is to get started, there's a few caveats to making things look "nice" and having your site be reactive (read: able to scale dynamically as the browser's viewport shape changes).

You'll also notice that we're talking about (at least) two "viewports" -- there's the Web-Browser's Viewport, referred to in JavaScript as the "window"; and then the WebGL Viewport, which basically equates to the bounds of the `<canvas>` element(s) in the DOM. This is an important concept to keep in mind as we go forward. A lot of the "tricks" for scaling your WebGL viewport rely on being able to appropriately integrate the current state and shape of the browser's viewport into your calculations and definitions of your WebGL Viewport, which in turn relies on your WebGL Camera definition.

All sizes are relative ... to what, though? -- that's the tricky part that we're here to try and clarify.


<h2 id="hScalableCanvas">Scalable Canvas and DOM Elements</h2>

We're going to use __Three.js__ to create the DOM element(s) for the WebGL Viewports, but that means that we're going to innately be disconnected from the DOM layout and styling. We can get around this though by starting with a default size and then being sure to update (re-scale) the WebGL viewport as the DOM `<canvas>` element gets updated and modified by the CSS. It's extra steps, but necessary steps, if we want things to coordinate nicely.

First things first, we want the aspect ratio of the current HTML Viewport (the webpage in the browser), so that we can set our WebGL viewport to share the same aspect ratio. This isn't mandatory, but this value is very useful to compute and hold onto.

```javascript
const aspect_ratio = window.innerWidth / window.innerHeight;
```

Remember to note that a `const` in JavaScript is a constant value and _instance_, meaning the instance cannot be modified and the value of the instance cannot be modified. It's a convenient optimization, but you may find yourself wanting to update this `aspect_ratio` value to make your site more reactive. In that case, you'd want to do the same calculation but swap `const` for `let`, to create a mutable (read: able to be modified) instance within the global scope.
