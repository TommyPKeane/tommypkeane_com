# PinePhone: Hardware

In July 2020, we received our April 2020 order of a Pine64 PinePhone, the UBports Community Edition, running Ubuntu Touch.

The 2020 SARS-CoV-2 Pandemic caused shipping delays, since the phone was coming from China, but it shipped in early July and arrived a few weeks later after getting through customs.

In this article we'll present some notes about things we've noticed with the hardware, as well as just pointing back to the official documentation with reference links.

As an introductory first impression: the phone is quite large -- we've been using an iPhone SE (2016) -- and can get quite hot, due to the still nascent software. The back case is plastic and separates from the phone _via_ an indentation on the front-bottom-right corner. It's relatively easy to remove the back cover, and this gives access to the removable battery, the hardware dip-switches, and the MicroSD Card slot.

The screen is plastic, not glass, so the phone arrived with a screen-protector already in place, and then a plastic sheet to protect the phone during shipping was placed over the screen-protector. We have not tried to remove the screen-protector. The touchscreen seems to miss a few touches, but it's hard to tell if that's from the screen-protector or is just innate. We did not get any dead-pixels.

Overall, we're super pleased with the quality and functionality of the phone for only 149.99 USD, especially since it's a fully functional (and accessible) ARM64 computer that supports Linux 5.7+ through the Manjaro ARM Linux Distribution.

Now, let's get into more of the hardware details.

## Dimensions (Size and Weight)

## Power and Battery

## Dip Switches

## MicroSD Card Slot

## GPS Chipset

## WiFi Chipset

## 4G Cellular Modem Chipset

## CPU (with GPU)

The CPU for the UBPorts CE PinePhone is the Allwinner A64 chipset, which includes the Mali400 MP2 as an embedded GPU.

- Sunxi Linux Wiki: [Allwinner A64](https://linux-sunxi.org/A64)

As the wiki states, the Allwinner A64 is considered a __System on Chip__ (SoC) device.

It is composed of a CPU and a GPU:

- CPU: ARM Cortex A53 (Quad-Core)
- GPU: Mali400 MP2

### CPU Features (ARM Cortex A53)

- [ARM Developer Page for Mali400 GPU](https://developer.arm.com/ip-products/processors/cortex-a/cortex-a53)

### GPU Features (Mali400 MP2)

The __Mali400__ GPU is part of the __Mali4XX__ family. Per the [Sunxi Linux Wiki](), the __Mali4XX__ family is compliant with the OpenGL ES 1.1, OpenGL ES 2.0, and OpenVG 1.1 standards.

The GPU has 1 Geometry Processor (GP) per Vertex-Shader, 2 Pixel Processors (PP) per Fragment-Shader, and 256 KiB of Level-2 (L2) CPU Cache Memory.

- [ARM Developer Page for Mali400 GPU](https://developer.arm.com/ip-products/graphics-and-multimedia/mali-gpus/mali-400-gpu)
