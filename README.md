# tommypkeane.com Website

Currently, this is a basic HTML, CSS, and JS site of static assets for [tommypkeane.com](https://www.tommypkeane.com).

This is shared here only for educational reference, and because everything here could be scraped off the site anyways, so why make it difficult.

## Development

During the basic dev-loop, it helps to have the site hosted locally. The easiest way to do that is with Python v3.x, where you can call:

```bash
cd [/path/to]/tommypkeane_com;
python -m http.server;
```

The above assumes that you first navigate to this directory, and then you call the Python v3 interpreter (`python`) to run the `http.server` module, which will start a simple static-file server bound to `[::]` (IPv6 version of `0.0.0.0`) on port `8000` as the default.

If you want to specify the port or the address specifically, like if `8000` is already taken or you want to use `localhost` (`127.0.0.1`), then the equivalent to the above would be:

```bash
python -m http.server --bind :: 8000
```

## Libraries

- [MathJax](https://www.mathjax.org/)
- [highlight.js](https://highlightjs.org/)

## Fonts

- [Google Fonts](https://fonts.google.com/)

## License

All rights reserved to Tommy P. Keane, except where otherwise indicated by third-party licenses in the `/libs/` directory.
