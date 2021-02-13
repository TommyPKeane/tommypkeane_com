The CPU for the UBPorts CE PinePhone is the Allwinner A64 chipset, which includes the Mali400 MP2 as an embedded GPU.

- Sunxi Linux Wiki: [Allwinner A64](https://linux-sunxi.org/A64)

As the wiki states, the Allwinner A64 is considered a __System on Chip__ (SoC) device.

It is composed of a CPU and a GPU:

- CPU: ARM Cortex A53 (Quad-Core)
- GPU: Mali400 MP2

## CPU Features (ARM Cortex A53)

- [ARM Developer Page for Mali400 GPU](https://developer.arm.com/ip-products/processors/cortex-a/cortex-a53)

## GPU Features (Mali400 MP2)

The __Mali400__ GPU is part of the __Mali4XX__ family. Per the [Sunxi Linux Wiki](), the __Mali4XX__ family is compliant with the OpenGL ES 1.1, OpenGL ES 2.0, and OpenVG 1.1 standards.

The GPU has 1 Geometry Processor (GP) per Vertex-Shader, 2 Pixel Processors (PP) per Fragment-Shader, and 256 KiB of Level-2 (L2) CPU Cache Memory.

- [ARM Developer Page for Mali400 GPU](https://developer.arm.com/ip-products/graphics-and-multimedia/mali-gpus/mali-400-gpu)
