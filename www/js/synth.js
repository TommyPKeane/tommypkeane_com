let audio_ctx = null;
let synth_osc = null;
let gain_node = null;
let display_elm = document.querySelector("#synthwaveform");
let audio_enable_modal = document.querySelector("#audio_modal");
let audio_enable_btn = document.querySelector("#audio_enable_btn");
let volume_ctrl = document.querySelector("#volume_ctrl");
let display_ctx = display_elm.getContext("2d");
let freq = 0;

display_elm.width *= 3;
display_elm.height *= 3;

class SynthKey {
   constructor(letter, variant, octave, freq, keyboard_key) {
      this.letter = letter;
      this.variant = variant;
      this.octave = octave;
      this.freq = freq;
      this.kb = keyboard_key;

      this.id = variant + letter + octave;
      return;
   }
};

const key_c3 = new SynthKey("C", "key", 3, 130.8128, "t");
const key_c4 = new SynthKey("C", "key", 4, 261.6256, "g");
const key_c5 = new SynthKey("C", "key", 5, 523.2511, "v");

const key_csharp3 = new SynthKey("C", "sharp", 3, 130.8128, "t");
const key_csharp4 = new SynthKey("C", "sharp", 4, 261.6256, "g");
const key_csharp5 = new SynthKey("C", "sharp", 5, 523.2511, "v");

const key_d3 = new SynthKey("D", "key", 3, 130.8128, "t");
const key_d4 = new SynthKey("D", "key", 4, 261.6256, "g");
const key_d5 = new SynthKey("D", "key", 5, 523.2511, "v");

const key_dsharp3 = new SynthKey("D", "sharp", 3, 130.8128, "t");
const key_dsharp4 = new SynthKey("D", "sharp", 4, 261.6256, "g");
const key_dsharp5 = new SynthKey("D", "sharp", 5, 523.2511, "v");

const key_e3 = new SynthKey("E", "key", 3, 130.8128, "t");
const key_e4 = new SynthKey("E", "key", 4, 261.6256, "g");
const key_e5 = new SynthKey("E", "key", 5, 523.2511, "v");

const key_f3 = new SynthKey("F", "key", 3, 130.8128, "t");
const key_f4 = new SynthKey("F", "key", 4, 261.6256, "g");
const key_f5 = new SynthKey("F", "key", 5, 523.2511, "v");

const key_fsharp3 = new SynthKey("F", "sharp", 3, 130.8128, "t");
const key_fsharp4 = new SynthKey("F", "sharp", 4, 261.6256, "g");
const key_fsharp5 = new SynthKey("F", "sharp", 5, 523.2511, "v");

const key_g3 = new SynthKey("G", "key", 3, 130.8128, "t");
const key_g4 = new SynthKey("G", "key", 4, 261.6256, "g");
const key_g5 = new SynthKey("G", "key", 5, 523.2511, "v");

const key_gsharp3 = new SynthKey("G", "sharp", 3, 130.8128, "t");
const key_gsharp4 = new SynthKey("G", "sharp", 4, 261.6256, "g");
const key_gsharp5 = new SynthKey("G", "sharp", 5, 523.2511, "v");

const key_a3 = new SynthKey("A", "key", 3, 130.8128, "t");
const key_a4 = new SynthKey("A", "key", 4, 261.6256, "g");
const key_a5 = new SynthKey("A", "key", 5, 523.2511, "v");

const key_asharp3 = new SynthKey("A", "sharp", 3, 130.8128, "t");
const key_asharp4 = new SynthKey("A", "sharp", 4, 261.6256, "g");
const key_asharp5 = new SynthKey("A", "sharp", 5, 523.2511, "v");

const key_b3 = new SynthKey("B", "key", 3, 130.8128, "t");
const key_b4 = new SynthKey("B", "key", 4, 261.6256, "g");
const key_b5 = new SynthKey("B", "key", 5, 523.2511, "v");


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

let keys = document.querySelector("#keys").getElementsByTagName("rect");

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
   let amp = gain_node ? gain_node.gain.value : 0;
  
   display_ctx.beginPath();
   display_ctx.moveTo(0, (hy / 2));
   display_ctx.strokeStyle = "orange";
   for(let i = 0; i < t; ++i) {
      a = get_sinewave_pt(5 * i / 130.818, freq, amp);
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
      ti += 1;
      if(ti > display_elm.width) {
         ti = 0;
      }
   },
   1
);


let key_handlers = {};

let start_audio = function hst_start_audio(tone_freq) {
   if (synth_osc !== null) {
      synth_osc.disconnect(gain_node);
      synth_osc.stop(0);
   }
   synth_osc = audio_ctx.createOscillator();
   synth_osc.type = "square";
   synth_osc.detune.value = 0;
   synth_osc.frequency.value = tone_freq;
   synth_osc.start(0);
   synth_osc.connect(gain_node);
   freq = tone_freq;
   $("#note_display").html(tone_freq.toFixed(4) + " Hz");
   return;
}

let stop_audio = function hst_stop_audio() {
   synth_osc.disconnect(gain_node);
   synth_osc = null;
   freq = 0;
   $("#note_display").html("");
   return;
}


let audo_enable_fnc = function hst_audio_enable_fnc() {
   audio_ctx = new (window.AudioContext || window.webkitAudioContext)();
   gain_node = audio_ctx.createGain();
   gain_node.connect(audio_ctx.destination);
   volume_ctrl.addEventListener(
      "input",
      function(evt) {
         gain_node.gain.value = this.value;
         document.querySelector("#volume_pcnt").innerHTML = (
            ((this.value / 1.0) * 100.0).toFixed(0) + "%"
         );
         return;
      },
      false, 
   );
   gain_node.gain.value = 0.50;
   keycount = 0;
   for (key of keys) {
      (function () {
         let crnt_key = key;
         let octave = (Math.floor(keycount / 12) + 3);
         let tone_freq = tones[crnt_key.id][octave];
         let tone_keypress = keyboardkeys[crnt_key.id][octave];
         crnt_key.addEventListener(
            "mouseenter",
            () => {start_audio(tone_freq); return;},
            false,
         );
         crnt_key.addEventListener(
            "mouseleave",
            stop_audio,
            false,
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

   $(audio_enable_modal).modal("hide");
   return;
}


let pageload = function hst_pageload() {
   $(audio_enable_modal).modal("show");
   // audio_enable_btn.addEventListener(
   //    "onclick",
   //    audo_enable_fnc,
   //    false,
   // );
   return;
}


window.addEventListener("load", pageload, false);

// CHROME / iOS FIX
function mousePressed() {
   return;
}
