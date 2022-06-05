---
title: "FPGA AIX Stopwatch"
date: 2022-06-05T15:00:00+01:00
categories:
  - Blog
  - Red Pitaya
  - FPGA
  - AXI
tags:
  - Red Pitaya
  - FPGA
  - Interfaces
---

Today I started working with the FPGA fabric. I tried out the [FPGA lessons](https://redpitaya-knowledge-base.readthedocs.io/en/latest/learn_fpga/4_lessons/top.html) 1 to 4 by Anton Potočnik.
I found lesson 4 particulary interesting as it shows how to connect the PS and PL sections of the Zynq chip using AXI.
I also experimented with changing the clock speed of the PL fabric. I found that could reliably run from 300KHz to 2500MHz. It is rated for down to 100KHz, but I had timing problems with that,
maybe due to the latancy with transfering data of the Red Pitaya and to my web browser with a slow PL clock. I found that you need to stop the clock to make large changes to the speed.
[My notebook](https://github.com/M0JPI/red-pitaya-projects/blob/master/jupyter-notebooks/fpga_axi_interfaces/Stopwatch.ipynb) with the memory map in Python is in this repository.
