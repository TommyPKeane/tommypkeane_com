let audio_ctx = null;
let synth_osc = null;
let display_elm = document.getElementById("synthwaveform");
let display_ctx = display_elm.getContext("2d");
let freq = 0;

display_elm.width *= 3;
display_elm.height *= 3;

let tones = {
   "keyC": {
      3: 130.8128,
      4: 261.6256,
      5: 523.2511,
   },
   "sharpC": {
      3: 138.5913,
      4: 277.1826,
      5: 554.3653,
   },
   "keyD": {
      3: 146.8324,
      4: 293.6648,
      5: 587.3295,
   },
   "sharpD": {
      3: 155.5635,
      4: 311.1270,
      5: 622.2540,
   },
   "keyE": {
      3: 164.8138,
      4: 329.6276,
      5: 659.2551,
   },
   "keyF": {
      3: 174.6141,
      4: 349.2282,
      5: 698.4565,
   },
   "sharpF": {
      3: 184.9972,
      4: 369.9944,
      5: 739.9888,
   },
   "keyG": {
      3: 195.9977,
      4: 391.9954,
      5: 783.9909,
   },
   "sharpG": {
      3: 207.6523,
      4: 415.3047,
      5: 830.6094,
   },
   "keyA": {
      3: 220.0000,
      4: 440.0000,
      5: 880.0000,
   },
   "sharpA": {
      3: 233.0819,
      4: 466.1638,
      5: 932.3275,
   },
   "keyB": {
      3: 246.9417,
      4: 493.8833,
      5: 987.7666,
   },
}; // Hz

let keyboardkeys = {
   "keyC": {
      3: "t",
      4: "g",
      5: "v",
   },
   "sharpC": {
      3: "T",
      4: "G",
      5: "V",
   },
   "keyD": {
      3: "y",
      4: "h",
      5: "b",
   },
   "sharpD": {
      3: "Y",
      4: "H",
      5: "B",
   },
   "keyE": {
      3: "u",
      4: "j",
      5: "n",
   },
   "keyF": {
      3: "i",
      4: "k",
      5: "m",
   },
   "sharpF": {
      3: "I",
      4: "K",
      5: "M",
   },
   "keyG": {
      3: "o",
      4: "l",
      5: ",",
   },
   "sharpG": {
      3: "O",
      4: "L",
      5: "<",
   },
   "keyA": {
      3: "p",
      4: ";",
      5: ".",
   },
   "sharpA": {
      3: "P",
      4: ":",
      5: ">",
   },
   "keyB": {
      3: "[",
      4: "\'",
      5: "/",
   },
}; // Hz

let keys = document.getElementById("keys").getElementsByTagName("rect");

let get_sinewave_pt = function hst_get_sinewave_pt(t, f, a) {
   let wx = display_elm.width;
   let hy = display_elm.height;

   let amp = a * hy / 2;

   let wave_pt = (
      (hy / 2) - (amp * Math.sin(2 * Math.PI * (t * f) / wx))
   );
   return (wave_pt);
}

let draw_sinewave = function hst_draw_sinewave(t) {
   let wx = display_elm.width;
   let hy = display_elm.height;
  
   display_ctx.beginPath();
   display_ctx.moveTo(0, (hy / 2));
   display_ctx.strokeStyle = "orange";
   for(let i = 0; i < t; ++i) {
      a = get_sinewave_pt(i, freq / 1, 0.85);
      display_ctx.quadraticCurveTo(i, a, i, a);
   }
   display_ctx.stroke();

   return;
}

let ti = 0;

let draw_loop = setInterval(
   function() {
      display_ctx.clearRect(0, 0, ti, display_elm.height);
      draw_sinewave(ti);
      ti++;
      if(ti > display_elm.width) {
         ti = 0;
      }
   },
   1
);


let key_handlers = {};

let enable_audio = function hst_enable_audio() {
   if (audio_ctx.state !== "running") {
      audio_ctx.resume();
   }
   $("#audio_modal").modal("hide");
   return;
}

let start_audio = function hst_start_audio(tone_freq) {
   if (synth_osc !== null) {
      synth_osc.disconnect(audio_ctx.destination);
      synth_osc.stop(0);
   }
   synth_osc = audio_ctx.createOscillator();
   synth_osc.type = "square";
   synth_osc.detune.value = 0;
   synth_osc.frequency.value = tone_freq;
   synth_osc.start(0);
   synth_osc.connect(audio_ctx.destination);
   freq = tone_freq;
   return;
}

let stop_audio = function hst_stop_audio() {
   synth_osc.disconnect(audio_ctx.destination);
   synth_osc = null;
   freq = 0;
   return;
}

let pageload = function hst_pageload() {
   $("#audio_modal").modal("show");
   try {
      audio_ctx = new (window.AudioContext || window.webkitAudioContext)();
      keycount = 0;
      for (key of keys) {
         console.log(key.id);
         (function () {
            let crnt_key = key;
            let octave = (Math.floor(keycount / 12) + 3);
            let tone_freq = tones[crnt_key.id][octave];
            let tone_keypress = keyboardkeys[crnt_key.id][octave];
            crnt_key.addEventListener(
               "mouseenter",
               () => {start_audio(tone_freq); return;},
               false
            );
            crnt_key.addEventListener(
               "mouseleave",
               stop_audio,
               false
            );
            document.addEventListener(
               "keydown",
               function(evt) {
                  if ((synth_osc === null) && (evt.key == tone_keypress)) {
                     $(crnt_key).toggleClass("active");
                     start_audio(tone_freq);
                     evt.preventDefault();
                  }
                  return;
               },
               false
            );
            document.addEventListener(
               "keyup",
               function(evt) {
                  if ((synth_osc !== null) && (evt.key == tone_keypress)) {
                     $(crnt_key).toggleClass("active");
                     stop_audio();
                  };
                  return;
               },
               false
            );
         }());
         keycount += 1;
      }
   }
   catch(evt) {
      alert("Web Audio API is not supported in this browser.\nThis Page will not work, sorrys.");
   }
   return;
}

window.addEventListener("load", pageload, false);


// CHROME / iOS FIX
function mousePressed() {
   return;
}
