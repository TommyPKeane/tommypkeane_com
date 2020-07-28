[D3.js](https://d3js.org/) is an advanced graphics library for JavaScript based-on the SVG XML standard for text-based web-graphics.

The benefit of SVG images is that not only are they vector-graphics ("infinitely" scalable), but they're also text-based, meaning that they can easily be committed to a Version Control System (VCS) like git, Mercurial (Hg), or Subversion (SVN) to track changes.

This can be a huge benefit for scientific and engineering graphics, since it adds a level of traceability and design evolution that otherwise would be very difficult to track with standard raster graphics (PNG, JPG, BMP, _etc._).

Before getting into all the advanced features of D3.js, this page will cover the intros of creating the SVG canvas, manipulating it, and adding basic graphical shapes like lines and polygons.

While SVGs are typically only 2D, all 2D display graphics are in 2D, so it's certainly possible to create 3D graphics by (mathematically) projecting 3D shapes onto a 2D viewport, to create a 3D effect of depth. That is how all 3D-appearing illustrations, movies, television shows, videogames, and computer graphics currently achieve their sense of depth.

If you're already familiar with D3.js, this article probably isn't useful, so we'd suggest going back to the Educational landing page and check out the other articles.
