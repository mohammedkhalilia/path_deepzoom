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

In the explore box type: http://digitalslidearchive.emory.edu:8003/v1/docs

Public Access
----------------------
You can access the deepzoom image API through

http://digitalslidearchive.emory.edu/dzi instead of using port 8003

Endopints
----------------------
There are three endpoints only

`/{PATH}` Return a string containing the XML metadata for the Deep Zoom file

`/{PATH}/{level}/{x}/{y}` Return an RGB Image for a tile

`/view/{PATH}` Renders OpenSeadragon for demo the tile server

Examples:
If the path is `SLIDES/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi`

http://digitalslidearchive.emory.edu/dzi/SLIDES/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi

http://digitalslidearchive.emory.edu/dzi/SLIDES/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi/10/0/0

http://digitalslidearchive.emory.edu/dzi/view/SLIDES/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi