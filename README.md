Deep Zoom API
=====================

Installation
---------------------
    git clone git@github.com:scimk/path_deepzoom.git

	source /home/dgutman/osdTester/bin/activate 

	python run.py

Test using Swagger
----------------------
Go to: http://digitalslidearchive.emory.edu/swagger

In the explore box type: http://digitalslidearchive.emory.edu/dzi/docs

Public Access
----------------------
You can access the deepzoom image API through

http://digitalslidearchive.emory.edu/dzi instead of using port 8003

Endopints
----------------------
There are two endpoints only

`/{PATH}` Return a string containing the XML metadata for the Deep Zoom file

`/{PATH}/{level}/{x}/{y}` Return an RGB Image for a tile

Examples:
If the path is `ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi`

http://digitalslidearchive.emory.edu/dzi/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi

http://digitalslidearchive.emory.edu/dzi/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi/10/0/0