D3.js graphics are rendered by SVG viewers. The most common SVG viewer (renderer) is your web-browser. All contemporary web-browsers support the XML standard for SVGs. So, alongside security concerns, if you're using an outdated browser that doesn't support SVGs, you will want to upgrade to take advantage of the latest technology.

First, we need to make sure that we have the most basic HTML code required to support D3.js:

```html
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <header>
      <h1>Example</h1>
    </header>
    <main>
      <div id="idMyCanvas" class="svg_container"></div>
    </main>
    <footer></footer>
    <script src="/js/libs/d3/d3.min.js"></script>
    <script src="/js/mycode.js"></script>
  </body>
</html>
```

There's a little bit extra there, but that's a pretty minimal example of how to setup an HTML page for starting to create D3.js SVGs. The main element is the `idMyCanvas` element (the `<div>`), which we'll be accessing by its `id` in JavaScript.

The other important thing to note is the `src` attribute for the first `script` tag. In this case we're setting it to `/js/libs/d3/d3.min.js`, which indicates that we're hosting the code "locally" on the webserver.

This is preferred in production situations instead of using the recommended `https://d3js.org/d3.v5.min.js` URL, because we want to have control over our version, and not necessarily have to reach out to the internet to get it. By locally storing the file in a special `/js/libs/d3/` directory, we can then commit it into our version control system (git, for example) and keep track of the version that we've stored.

As new versions are released, we can do a regression-testing Pull-Request, make any code changes required to use the latest version, and then merge the commits with that new version and any related changes to keep things working. If we were using the URL, we'd be at the mercy of whenever `d3js.org` decides to update the code. So, while it's great to get all the latest features and bugfixes, it's probably not preferable to randomly be at risk of everything crashing.

Also notice that we loaded `d3.min.js` _before_ our custom JavaScript code that'll be in `mycode.js`. This is necessary to make sure that the JavaScript engine in the web-browser understands to load D3.js before our code, since our code will reference the D3.js library's functions and objects.

So now, we have our scripts loaded and our `div` (`idMyCanvas`) is ready to be written into with our custom SVG ... so let's do that in JavaScript:

```javascript
let container_id = "idMyCanvas";

// let container_elm = document.getElementById(container_id);

d3.select("#" + container_id)
  .append("svg")
    .attr("viewbox", "0 0 1280 720")  // min-x, min-y, width, height [px]
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("preserveAspectRatio", "xMidYMid meet")
    .attr("xmlns", "http://www.w3.org/2000/svg")
    .attr("version", "1.1")
    .attr("id", "my_canvas");
```

If we have the above code in `/js/mycode.js`, it's grabbing the `idMyCanvas` element by `id` (symbolized with the `#` character), appending a new element (an `<svg>...</svg>`), and then setting a bunch of attributes on that `<svg>` tag.

To clarify this, let's show what the HTML looks like _after_ the page has loaded and implicitly run the `/js/mycode.js` code.

```html
<!doctype html>
<html lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
  </head>
  <body>
    <header>
      <h1>Example</h1>
    </header>
    <main>
      <div id="idMyCanvas" class="svg_container">
        <svg
          viewbox="0 0 1280 720"
          width="100%"
          height="100%"
          preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg"
          version="1.1"
          id="my_canvas">
        </svg>
      </div>
    </main>
    <footer></footer>
    <script src="/js/libs/d3/d3.min.js"></script>
    <script src="/js/mycode.js"></script>
  </body>
</html>
```

I cheated a bit and made the styling easier to read, but that's essentially what gets added by our `mycode.js` code with that call to the `d3` object.

At this point, we won't see anything rendered on the page unless we use CSS to color the `svg`'s background or draw a border or something like that.

Without getting out of scope on this section, let's expand `mycode.js` just a bit by placing a simple text statement into the canvas.

```javascript
let container_id = "idMyCanvas";
let svg_id = "my_canvas";

// let container_elm = document.getElementById(container_id);

let svg_obj = d3.select("#" + container_id)
                .append("svg")
                  .attr("viewbox", "0 0 1280 720")
                  .attr("width", "100%")
                  .attr("height", "100%")
                  .attr("preserveAspectRatio", "xMidYMid meet")
                  .attr("xmlns", "http://www.w3.org/2000/svg")
                  .attr("version", "1.1")
                  .attr("id", svg_id);

let text_obj = svg_obj.append("text");

let text_label = text_obj
                  .attr("x", 30)
                  .attr("y", 30)
                  .attr("font-family", "sans-serif")
                  .attr("font-size", "20px")
                  .attr("fill", "red")
                  .text("sup, gurl.");
```

Now we should see the text `sup, gurl.` show up in the system standard `sans-serif` font family for your web-browser, colored red and at a height of `20` pixels.

<div class="container_svg">
  <svg viewbox="0 0 1280 720" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg" version="1.1" id="my_canvas"><text x="30" y="30" font-family="sans-serif" font-size="20px" fill="red">sup, gurl.</text></svg>
</div>

It's position will be `30` pixels to the right of the top-left corner, and `30` pixels down from the top-left corner. The `(0, 0)` point of the SVG canvas is always the ___top-left___ corner and extends positively to the ___bottom-right___ corner which will be at point `(width, height)`. So, this means that your "visible" canvas area is all points in the `(0, 0)` to `(width, height)` rectangle.

Obviously, this is configurable by the `viewbox` attribute, which lists these 4 points as: `"0 0 width height"`, in our example. If you change these values, you'll change what's visible. The `viewbox` is the definition of the 2D "viewport" for the SVG drawing.

Above, you'll see that we've embedded the resultant SVG, and actually it is a `1280x720` pixel canvas, but scaled to bounds of this article width. The scale is preserved, thanks to our options in the `preserveAspectRatio` attribute, and the font that would be `20` pixels tall on a `1280x720` canvas is now some proportional height based on however much the canvas width has been shrunk, depending on your browser viewport size and our CSS designs.

In the standalone example, if you copied all the required code that we've shown above, you might see something different. If you try messing around with the `x` and `y` positional attributes for the `text_label` instance to move the text around, you might run into an odd problem.

See, we've clearly defined our viewport as being `1280x720`, but you may notice that the `idMyCanvas` div in the standalone HTML file is an odd shape -- likely it'll be as wide as your browser window, but only like `150` pixels tall. In that case, if you set `y` for the text larger than `140`, you may see the text cut-off or completely not visible. Why is this happening?

Well, without any CSS styling for the `svg_container` HTML class for the `idMyCanvas` element, it's height just defaults to whatever the renderer (your browser) thinks it should be to contain the content. You'd think that this should be the height of the `svg` element as you defined the viewport, but since we set the `height` to `100%`, we're caught in a catch-22 self-referential loop of "whose percentage?". Nobody defined the height, but it's set to `100%`, but `100%` of what? The container height is undefined ... so the browser just says, fine, here, take `153` pixels, or whatever.

