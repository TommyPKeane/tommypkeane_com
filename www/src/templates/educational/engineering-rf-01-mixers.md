A topic that I found a lot of confusion around in previous professional experience was the concept of "bands" for satellite communications, especially because of the need to up-convert and down-convert the signal frequencies.

First, to clarify, a __band__ is a Frequency Range that is associated with a name/label per some standardization entity like the [IEEE](https://en.wikipedia.org/wiki/Radio_spectrum#IEEE), [EU/NATO](https://en.wikipedia.org/wiki/Radio_spectrum#EU,_NATO,_US_ECM_frequency_designations), or [ITU](https://en.wikipedia.org/wiki/Radio_spectrum#ITU). There's certainly no issue in having a non-standard __band__, but in that case it would only have a colloquial or esoteric label, which ideally would be clarified to prevent miscommunication in any technological UI/UX or documentation.

The standardized bands are used in satellite communications technology for either Receiving (RX) or Transmitting (TX) a signal at the satellite antenna(e). To prevent confusion, we can abbreviate these as bands as \(P_{SAT}\) (RX) and \(T_{SAT}\) (TX).

But, in practice it's not actually useful to denote just the "band" of the satellite. That is because a satellite will actually communicate over a relatively large range of frequencies due to the effects of [modulation](https://en.wikipedia.org/wiki/Modulation), and the band, itself, is simply the outer bounds for the modulated-signals' bandwidth(s).

<aside>
__A brief Aside on Modulation:__

As a tone (a single energy level) becomes modulated, it either needs to "spread-out" across time or across frequency. Think of [Morse Code](https://en.wikipedia.org/wiki/Morse_code) as being an example of spreading-out the modulation across time. The problem with such an approach is that you have to wait, in time, for the entire message to be received as you have to wait for it to be transmitted. If you could instead "tap-out" all the characters in your message simultaneously by effectively varying each one's [pitch](https://en.wikipedia.org/wiki/Pitch_(music)), the superimposed tones of various pitches would then be spread-out across frequencies but all (essentially) at the same point in time.
</aside>

  Contemporary satellite communications that use HTTP or HTTPS digital data communications based-on TCP/IP are going to mainly be some kind of Frequency Modulated signals, thus requiring some __Modulation Bandwidth__ centered around the so-called __Carrier Frequency__ (or __Center Frequency__).

  So, it's actually more useful to talk about \(\zeta_{RX}\) and \(\zeta_{TX}\), for the Satellite's center frequencies, instead of worrying about what "band" they fall into.

The further complication, though, is that to successfully transmit signals through the atmosphere, we need high-energy, high-frequency signals. Visible Light is in the Terahertz (THz) ranges, and you'll find that most satellites communicate in the \(5\, -\, 100\, \text{[GHz]}\) range.

But, there is an issue with these high-frequency signals, in that they would create a <i>lot</i> of [Electromagnetic Interference (EMI)](https://en.wikipedia.org/wiki/Electromagnetic_interference) in standard cabling and electronics of a [VSAT](https://en.wikipedia.org/wiki/Very-small-aperture_terminal) Earth-Station.

To solve this problem in a cost-effective manner that allows for the use of contemporary, commercial electronics with minimal, special considerations, the Satellite signals are actually __down-converted__ when they are received by an Earth-Station. So, there is usually an electronic component called the __Low-Noise Block Down-Converter__ (LNB), and this device will take the high-frequency satellite signal and mix it down into a frequency that is (typically / historically) within the [IEEE L-Band](https://en.wikipedia.org/wiki/L_band) range.

A contemporary satellite <abbr title="MODulation-DEModulation Device">MODEM</abbr>, like this [Viasat CBM-400](https://www.viasat.com/products/satcom-cbm-400), for example, will have in its specifications a set of interface bandwidths (frequency ranges), which represent the acceptable/nominal <a href="https://en.wikipedia.org/wiki/Intermediate_frequency">Intermediate Frequency (IF)</a> ranges for Receiving (RX) into the modem and Transmitting (TX) out of the <abbr title="MODulation-DEModulation Device">MODEM</abbr>.

These <abbr title="Intermediate Frequency">IF</abbr> ranges don't need to adhere to any pre-defined range, these are actually just direct consequences of the electronics of the <abbr title="MODulation-DEModulation Device">MODEM</abbr> itself. So, really, it's only by circumstance and a loose convention that these ranges align with the [IEEE L-Band](https://en.wikipedia.org/wiki/L_band) range, but it's definitely not guaranteed.

For example, with our aforementioned CBM-400 <abbr title="MODulation-DEModulation Device">MODEM</abbr>, we see the following:</p>
<table class="tb_data_maths">
  <tr><th>Range Name</th><th>Range Minimum</th><th>Range Maximum</th></tr>
  <tr><td>CBM-400 RX</td><td>0.900 GHz</td><td>2.050 GHz</td></tr>
  <tr><td>CBM-400 TX</td><td>0.950 GHz</td><td>2.050 GHz</td></tr>
  <tr><td>IEEE L Band</td><td>1.000 GHz</td><td>2.000 GHz</td></tr>
  <caption>[Viasat CBM-400](https://www.viasat.com/products/satcom-cbm-400) Datasheet IF Frequency-Range compared to [IEEE L-Band](https://en.wikipedia.org/wiki/L_band).</caption>
</table>

Clearly, there's a \(50\, -\, 100\, \text{[MHz]}\) difference from the [IEEE L-Band](https://en.wikipedia.org/wiki/L_band), so again, there's no guarantee about "bands", and it's not really a useful talking-point except to give a quickly named point-of-reference. If you talk about [IEEE L-Band](https://en.wikipedia.org/wiki/L_band) in a colloquial, technical conversation, it can be a sort of shorthand for the \(1\, -\, 2\, \text{[GHz]}\) range, give or take a couple hundred MHz. Beyond that use, there's not really any actual information conveyed in saying something like: "...this is an [IEEE L-Band](https://en.wikipedia.org/wiki/L_band) <abbr title="MODulation-DEModulation Device">MODEM</abbr>...". Not only is that not strictly correct, it actually misrepresents the functionality of the <abbr title="MODulation-DEModulation Device">MODEM</abbr> when integrated into a VSAT system. And that leads to the final, further complication of all of this.

As the <abbr title="MODulation-DEModulation Device">MODEM</abbr>'s datasheet itself says: "Operates on any satellite band (C-, X-, Ka-, Ku-)", the <abbr title="MODulation-DEModulation Device">MODEM</abbr> itself is compatible with "any" satellite band -- which is both true and not really true. The reality is that the <abbr title="MODulation-DEModulation Device">MODEM</abbr> designers expect that it will be integrated into an Earth Station which will use down-mixers and up-mixers to facilitate the <abbr title="Radio Frequency">RF</abbr> communications. So, provided that you have compatible hardware that can take the TX signal out of the <abbr title="MODulation-DEModulation Device">MODEM</abbr> and up-mix it to be within the Satellite's RX frequency-range (its "RX Band", \(P_{RX}\)), then the <abbr title="MODulation-DEModulation Device">MODEM</abbr> can transmit to any satellite -- subject to the up-mixer. And likewise assuming that there is a compatible down-mixer for the Satellite's TX frequency-range to be down-converted to the <abbr title="MODulation-DEModulation Device">MODEM</abbr>'s RX frequency-range, then the <abbr title="MODulation-DEModulation Device">MODEM</abbr> can successfully receive transmissions from such a satellite.

So, in actually, the <abbr title="MODulation-DEModulation Device">MODEM</abbr> <i>does not</i> "know" anything, ever, about the "band(s)" of the satellite.

That can be a very tricky concept in satellite communications and systems integration for VSATs, because so much of the colloquial technical conversation is around "bands" -- arguably in a self-perpetuating kind of way.

For a VSAT operator, they'll be given the target longitude of a geosynchronous satellite and need to attempt to align the antenna of their Earth Station (VSAT) with that satellite. Once they've done that, they'll need to either have compatible static hardware, or make the necessary configurations in tunable hardware, to successfully down-mix and up-mix the Satellite signal(s) so that the <abbr title="MODulation-DEModulation Device">MODEM</abbr> and satellite can establish a communications link.

In this process, we have 2 paths: the Up-Link (<abbr title="MODulation-DEModulation Device">MODEM</abbr> TX to Satellite RX) and the Down-Link (Satellite TX to <abbr title="MODulation-DEModulation Device">MODEM</abbr> RX). Each end of each path is operating at a different frequency, despite their need to be compatible (identical) in order to facilitate communications. So, to achieve the compatibility, there are frequency-mixers sitting in the link-paths -- the Low-Noise Block Down-Converter (LNB) for the Down-Link and the (Low-Noise) Block Up-Converter (BUC) for the Up-Link.

For a concrete example, let's first look at the [Norsat 8515 LNB](https://www.satcomresources.com/norsat-8515-c-band-dro-lnb), which advertises itself as a "C Band" LNB. Why does it reference the IEEE C Band? Well, let's look at its data sheet and notice these Frequency values:

<table class="tb_data_maths">
  <tr><th>Name</th><th>Value</th></tr>
  <tr><td>Input Mininmum</td><td>3.400 GHz</td></tr>
  <tr><td>Input Maximum</td><td>4.200 GHz</td></tr>
  <tr><td>Local Oscillator (LO)</td><td>5.150 GHz</td></tr>
  <tr><td>Output Mininmum</td><td>0.950 GHz</td></tr>
  <tr><td>Output Maximum</td><td>1.750 GHz</td></tr>
  <caption>Selected [Norsat 8515 LNB](https://www.satcomresources.com/norsat-8515-c-band-dro-lnb) Datasheet Frequencies.</caption>
</table>

As the table, above, shows, there is a frequency value named the __Local Oscillator__ (LO) Frequency, and this is our down-mixer center Frequency. If we name this value as \(f_{LO}\) we end-up with the following input to output relationship:

$$f_{out} \overset{\Delta}{=} f_{LO} - f_{in}$$

This is actually an atypical arrangement, because most down-mixers would actually adhere to the following relationship:

$$f_{out} \overset{\Delta}{=} f_{in} - f_{LO}$$

And that's because C-Band is actually an outlier, in that it does "high-side" down-conversion. Which is a shorthand for saying that the <abbr title="Local Oscillator">LO</abbr> frequency is higher than the input frequencies. But this presents, potentially, a lot of confusion. When we go to design software or an integration approach that's sensible, we shouldn't need to know about named "bands", or do we?

  Before we answer that, let's look at a more conventional band example with the <a href="https://www.satcomresources.com/norsat-x1000ha-x-band-pll-lnb">Norsat X1000HA LNB</a>, which advertises itself as an "X Band" LNB:</p>

<table class="tb_data_maths">
  <tr><th>Name</th><th>Value</th></tr>
  <tr><td>Input Mininmum</td><td>`7.250 GHz`</td></tr>
  <tr><td>Input Maximum</td><td>`7.750 GHz`</td></tr>
  <tr><td>Local Oscillator (LO)</td><td>`6.300 GHz`</td></tr>
  <tr><td>Output Mininmum</td><td>`0.950 GHz`</td></tr>
  <tr><td>Output Maximum</td><td>`1.450 GHz`</td></tr>
  <caption>Selected [Norsat X1000HA LNB](https://www.satcomresources.com/norsat-x1000ha-x-band-pll-lnb) Datasheet Frequencies.</caption>
</table>

As already suggested, this is a more conventional design -- a low-side down-mixer -- where we have the following relationship:

$$f_{out} \overset{\Delta}{=} f_{in} - f_{LO}$$

So how do we square these competing equations?

We actually can get away without needing one-off labels or exceptions, if we simply rewrite our down-mixer input-output relationship in the following format:

$$f_{out} \overset{\Delta}{=} s \cdot \left(f_{LO} - f_{in}\right)$$

$$s \overset{\Delta}{=} \begin{cases} +1 \iff\ f_{LO} > f_{in} \\ -1 \iff\ f_{LO} < f_{in} \end{cases}$$

So, if we approach a down-mixer (LNB) as having an Input Minimum Frequency \(\alpha_{in}\) and an Input Maximum Frequency \(\beta_{in}\), as well as its mixing frequency, \(f_{LO}\), we have this summarizing, generic, relationship:

$$f_{IF} \overset{\Delta}{=} s \cdot \left(f_{LO} - f_{RF}\right)$$

$$s \overset{\Delta}{=} \begin{cases} +1 \iff\ f_{LO} > \alpha_{in},\, f_{LO} > \beta_{in} \\ -1 \iff\ f_{LO} < \alpha_{in},\, f_{LO} < \beta_{in} \end{cases}$$

While it's very likely that we could compare \(f_{RF}\) to \(f_{LO}\), instead of the input range frequencies, \(\alpha_{in}\) and \(\beta_{in}\), we're trying to frame this is a more conveniently programmatic sense. And, while possible, it's also unlikely that the Local Oscillator frequency would ever be between \(\alpha_{in}\) and \(\beta_{in}\).

Given the above relationships and conditions, we can now design a really simple base-class in an Object-Oriented Programming (OOP) fashion, like in this exemplar Python code:

```python
# mixer_down.py

class DownMixer(object):
  freq_in_min = None;  # alpha_in
  freq_in_max = None;  # beta_in
  freq_lo = None;  # f_LO
  mix_sgn = None;  # s

  def __init__(
    self,
    lo_freq,
    input_range,
  ):
    self.freq_in_min = input_range[0];
    self.freq_in_max = input_range[1];
    self.freq_lo = lo_freq;

    self.mix_sgn = (-1, 1)[int(self.freq_lo > self.freq_in_max)]

    return None;
  # fed

  def mix_down(self, new_freq):
    mixed_freq = self.mix_sgn * (self.freq_lo - new_freq)
    return (mixed_freq);
  # fed
#ssalc
```

Using the class as defined above, we can actually implement the down-mixing functionality of both of the exemplar LNBs that we mentioned earlier in this article. For convenience, let's assume all values are in \(\text{[GHz]}\):</p>

```python
>>> LNB_X1000HA = DownMixer(6.3, [7.25, 7.75])  # GHz
>>> "{0:0.3f} [GHz]".format(LNB_X1000HA.mix_down(7.35))
'1.050 [GHz]'
>>> "{0:0.3f} [GHz]".format(LNB_X1000HA.mix_down(7.25))
'0.950 [GHz]'
>>> "{0:0.3f} [GHz]".format(LNB_X1000HA.mix_down(7.75))
'1.450 [GHz]'

>>> LNB_8515 = DownMixer(5.15, [3.4, 4.2])  # GHz
>>> "{0:0.3f} [GHz]".format(LNB_8515.mix_down(3.9))
'1.250 [GHz]'
>>> "{0:0.3f} [GHz]".format(LNB_8515.mix_down(3.2))  # Out of spec, valid frequency, but
'1.950 [GHz]'                                        #  likely to be highly attenuated.
>>> "{0:0.3f} [GHz]".format(LNB_8515.mix_down(3.4))
'1.750 [GHz]'
>>> "{0:0.3f} [GHz]".format(LNB_8515.mix_down(4.2))
'0.950 [GHz]'
```

Success! The input-frequency limits result in the output-limits when mixed-down, and any frequency within the input range results in a frequency within the output range. For the 8515 device we also show that an "out-of-band" frequency will potentially produce a "valid" down-mixed frequency, but it's actually very likely to be invalid and will be highly attenuated. This will be verifiable by reviewing the Frequency Responce Curve of the LNB device, or by physically verifying the device with a benchtop Network Analyzer, or by using a Signal Generator (input) and a Spectrum Analyzer (output).

So, we've genericized this problem and we've avoided the use of bands entirely -- almost as if they're colloquial terms and not really converying any technical information ... hmmmm... interesting.

As the code of the __DownMixer__ class shows, we are using only the maximum input frequency to determine the sign modifier, \(s\), which is assuming, as stated above, that the Local Oscillator frequency will never be within the input-frequency range. This is an assumption, which introduces implicit limitations, but it's arguably a relatively safe assumption. Again, if you can't adhere to this assumption, you can always adjust the sign modifier by comparing the Local Oscillator frequency to the given frequency to be down-mixed (the __new_freq__ value in the code).

So, now, can we say the same thing about up-mixing in a [Block Up-Converter (BUC)](https://en.wikipedia.org/wiki/Block_upconverter)? Of course!

For up-mixing, we're almost always doing doing low-side up-mixing, so we could get away with being less generic and eliminate the need for a sign-modifier -- but why remove generic functionality? So let's just define it in a similarly generic way that supports low-side and high-side up-mixing:

$$f_{RF} \overset{\Delta}{=} f_{LO} + \left(s \cdot f_{IF}\right)$$

$$s \overset{\Delta}{=} \begin{cases} +1 \iff\ f_{LO} < \gamma_{in},\, f_{LO} < \eta_{in} \\ -1 \iff\ f_{LO} > \gamma_{in},\, f_{LO} > \eta_{in} \end{cases}$$

In this case, for sanity's sake, \(\gamma\) and \(\eta\) represent the mininum and maximum frequency values, respectively, for the <abbr title="Block Up-Converter">BUC</abbr>, to distinguish them from the <abbr title="Low-Noise Block Down-Converter">LNB</abbr> values.

You may realize also, that this new equation is actually just a rearrangement of the previous equation, where now we're interest in the RF value as the output of the <abbr title="Block Up-Converter">BUC</abbr>, instead of it being the input of the <abbr title="Low-Noise Block Down-Converter">LNB</abbr>.

So, again, we can now define a new base-class:</p>

```python
# mixer_up.py

class UpMixer(object):
   freq_in_min = None;  # gamma_in
   freq_in_max = None;  # eta_in
   freq_lo = None;  # f_LO
   mix_sgn = None;  # s

   def __init__(
      self,
      lo_freq,
      input_range,
   ):
      self.freq_in_min = input_range[0];
      self.freq_in_max = input_range[1];
      self.freq_lo = lo_freq;

      self.mix_sgn = (1, -1)[int(self.freq_lo > self.freq_in_max)]

      return None;
   # fed

   def mix_up(self, new_freq):
      mixed_freq = self.freq_lo + (self.mix_sgn * new_freq)
      return (mixed_freq);
   # fed
#ssalc
```

Now, very obviously, just like the descriptive equations, these two classes share a lot of redundant commonality. In essence, we really only have one equation and one base-class, describing a generic "mixer", and we can simply pass the up-mix/down-mix aspect as a boolean (flag) parameter. We'll leave out the details of that simplification, for now -- though it might show-up on my [GitHub account](https://github.com/TommyPKeane) at some point.

In summary, Frequency Bands are actually pretty rarely consequential in terms of VSAT integration, though they're used a lot for a kind of simplified conversational nomenclature. It's often easier, though far more confusing, to talk about Ku and X Band, instead of a bunch of very specific frequencies. But that's in conversation -- when it comes to technical integration of electronics, it absolutely does not help to carry around any kind of fuzzy or non-standard notion of Frequency Bands. As we've shown above, we can actually implement LNBs and BUCs as DownMixer and UpMixer instances (respectively) -- instantiating them very simply with their respective input frequency range and Local Oscillator (LO) frequency. Given the exemplar class designs, above, it'd be very easy to implement compatibility methods that could allow you to verify if a given Mixer is compatible with the Intermediary Frequency (IF) frequency-ranges of a specific <abbr title="MODulation-DEModulation Device">MODEM</abbr>. The <abbr title="MODulation-DEModulation Device">MODEM</abbr> itself would <i>not</i> be a mixer instance, it would instead have RX and TX frequency-ranges (otherwise referred to as the "support" or "domain-range") and report its current transmit frequency and its target (<abbr title="Intermediary Frequency">IF</abbr>) receive frequency. Those values would then, respectively, need to be within the input range of the BUC and the output range of the LNB, to have a functioning VSAT system.

If operators expect to work in named bands, or would like to know what named band their receive or transmit frequency is currently in, those could/should be User Interface (UI) layer mappings that are wholly distinct from the operational configuration and compatibility of devices. Why? Because, again, a <abbr title="MODulation-DEModulation Device">MODEM</abbr> does not operate in the same frequency range as the satellite and it does not do any mixing, so it actually has no possible compatibility or consideration of the Satellite's frequency band(s).

Yes, a <abbr title="MODulation-DEModulation Device">MODEM</abbr> that only supports limited frequencies may not be able to support certain IEEE Bands given certain LNBs or BUCs, but that's an integration issue, not a <abbr title="MODulation-DEModulation Device">MODEM</abbr> issue. It's all circumstantial, and it's all dependent on the actual, specific frequencies -- which are quite unlikely to perfect align with any specific IEEE or ITU Band.
