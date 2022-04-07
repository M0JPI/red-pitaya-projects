---
title: "Vagrant Setup"
date: 2022-03-29T18:00:00+01:00
categories:
  - Blog
  - Red Pitaya
  - DevOps
tags:
  - Red Pitaya
  - DevOps
  - Vagrant
  - Virtual Box
  - Update
  - Introduction
---

I'm interested in making code easy to follow and reproduce. I looked at what [Pynq](http://www.pynq.io/) was doing to manage a consistent environment for developers and found that [they are using](https://pynq.readthedocs.io/en/latest/pynq_sd_card.html) a virtual machine build environment called [Vagrant](https://www.vagrantup.com/).

As well as finding instructions on Pynq I also found Vagrant [Quick Start for Windows 10](https://www.swtestacademy.com/quick-start-vagrant-windows-10/).

I used both of these instructions to create a Vagrant instance to use as a development machine that can be conistant with what Pynq uses.

To setup Vitis 2020.1 I had to set `/etc/os-release` to `VERSION="18.04.4 LTS (Bionic Beaver)"`.
