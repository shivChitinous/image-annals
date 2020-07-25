import numpy as np
import scipy as sp
import skimage as ski
import skimage.filters
import image_analysis as anl

def preprocessor(pic,sigma=15,op_sz=2):
    bkg = ski.filters.gaussian(pic,sigma)
    pic_hp = pic-bkg
    thresh = ski.filters.threshold_otsu(pic_hp)
    pic_th = anl.thresher(pic_hp,thresh)
    pic_op = ski.morphology.opening(pic_th,ski.morphology.disk(op_sz))
    pic_fill = sp.ndimage.binary_fill_holes(pic_op)
    labelled = ski.measure.label(pic_fill,connectivity=2)
    return labelled
 