---
title: "Build System Missing Files"
date: 2022-08-11T15:00:00+01:00
categories:
  - Blog
  - Red Pitaya
  - Build System
  - GitHub
tags:
  - Red Pitaya
  - API
  - Build
  - Version Control
---

I have been trying to follow the [tutorial for making a web app](https://redpitaya.readthedocs.io/en/latest/developerGuide/software/build/webapp/firstApp.html).
I found that the rpApp.h file [is missing from the repository](https://forum.redpitaya.com/viewtopic.php?t=1727) but can be found in the images at /opt/redpitaya/include/apiApp/rpApp.h

The [JSON library 7.6.1 used seems to be abandoned](https://sourceforge.net/projects/libjson/) other libraries may need replacing to address CVEs for example crypto++ 5.6.2 is used, [that library is now at version 8.7](https://cryptopp.com/index.html) and it is [proably better to use OpenSSL](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/3980). 
It seems that crypto++ is mainly used for the GZIP function, so the CVEs may not be relevent.
