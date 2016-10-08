from openslide import OpenSlide
import openslide
from openslide.deepzoom import DeepZoomGenerator

path = "/SLIDES/ADRC/DG_ADRC_Slides/ADRC36-04/pTDP/ADRC36-04_F_pTDP-1to10K.ndpi"
opts = {
    'tile_size': 256,
    'overlap': 1,
    'limit_bounds': 0
}
osr = OpenSlide(path)
slide = DeepZoomGenerator(osr, **opts)
print slide.level_tiles
