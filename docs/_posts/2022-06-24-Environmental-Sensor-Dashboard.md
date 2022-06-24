---
title: "Environmental Sensor Dashboard"
date: 2022-06-24T15:00:00+01:00
categories:
  - Blog
  - Red Pitaya
  - Sensors
  - Sensor Board
  - Jupyter
tags:
  - Red Pitaya
  - FPGA
  - Grove
  - Interfaces
  - YouTube
  - Temperature Measurement
---

Using Grove Environmental Sensors and the [Red Pitaya Sensor Board](https://redpitaya.readthedocs.io/en/latest/appsFeatures/remoteControl/jupyter/Jupyter.html#hardware-extension-module) I created a dashboard.
The software of the dashboard is made using Jupyter Notebooks and the [jupyter_dashboards](https://jupyter-dashboards-layout.readthedocs.io/en/latest/) library.

I connected sensors to the analog, I2C and serial UART connections as shown in the diagram below:
![Sensor Setup Diagram](/red-pitaya-projects/assets/images/Sensor-Setup.png)

The Grove analog alcohol sensor needs the SCL pin to be held LOW to operate. I did this using jumper wires to connect the SCL pin to ground.
The [Jupyter Notebook can be found here](https://github.com/M0JPI/red-pitaya-projects/blob/master/jupyter-notebooks/dashboard/air_quality_dashboard.ipynb).

![Sensor Setup Diagram](/red-pitaya-projects/assets/images/Sensor-Setup.png)
