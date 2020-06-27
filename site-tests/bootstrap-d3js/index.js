// !# JavaScript ES6
// @file
// @brief Resizable d3.js Chart
//
// @copyright 2020, Tommy P. Keane
// @authoer Tommy P. Keane <talk@tommypkeane.com>

let svg = d3.select('#chartArea').append('svg');

let div_size_x = document.getElementById('chartArea').clientWidth;
let div_size_y = div_size_x / 3.236;

let graph_resize = function hst_resize() {
   div_size_x = document.getElementById('chartArea').clientWidth;
   div_size_y = div_size_x / 3.236;
   d3.select('#chartArea svg')
      .attr('width', div_size_x)
      .attr('height', div_size_y);
}

let circles = svg.selectAll("circle").data(d3.range(90))
                  .enter().append("circle")
                  .attr("cx", function(d){ return ((d + 0.5) * (div_size_x / 40)); })
                  .attr("r", div_size_x / (180))
                  .attr("fill", "blue");

let rects = svg.selectAll("rect").data(d3.range(120))
                  .enter().append("rect")
                  .attr("x", function(d){ return ((d + 0.75) * (div_size_x / 90)); })
                  .attr("width", div_size_x / (250))
                  .attr("height", div_size_x / (250))
                  .attr("fill", "red");

let triangles = svg.selectAll("polygon").data(d3.range(120))
                  .enter().append("polygon")
                  .attr(
                     "points",
                     function (d) {
                        pc = (d + 0.75) * (div_size_x / 90);
                        return `${pc-3},${pc-3} ${pc},${pc+3} ${pc+3},${pc-3}`;
                     }
                  )
                  .attr("fill", "green");

let tick = true;

d3.timer(
   function (time) {
      let seconds = Math.floor(new Date().getTime() / 10);
      if ((seconds % 10) == 0) {
         tick = !tick;
      }
      triangles.attr(
         "points",
         function(d) {
            px = (d + 0.75) * (div_size_x / 90);
            py = (
               (div_size_y / 3) * (Math.sin((d / 5) + (time / 1000)))
               * (tick ? 0.85 * Math.sin((d / 25) + (time / 1000)) : 1)
               + (div_size_y / 3)
            );
            return (`${px-3},${py-3} ${px},${py+3} ${px+3},${py-3}`);
         }
      );
      rects.attr(
         "y",
         function(d) {
            return (
               (Math.sin((d / 25) + 0.25 + (time / 1000)) * (div_size_y / 4))
               + (div_size_y / 2)
            );
         }
      );
      circles.attr(
         "cy",
         function(d) {
            return (
               (Math.sin((d / 5) + (time / 1000)) * (div_size_y / 4))
               + (div_size_y / 2)
            );
         }
      );
   }
);

window.onload = graph_resize;
window.onresize = graph_resize;
