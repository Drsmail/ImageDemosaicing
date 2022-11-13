
import os

import colour

import imageio
import numpy
import scipy

from colour_demosaicing import (
    EXAMPLES_RESOURCES_DIRECTORY,
    demosaicing_CFA_Bayer_bilinear,
    demosaicing_CFA_Bayer_Malvar2004,
    demosaicing_CFA_Bayer_Menon2007,
    mosaicing_CFA_Bayer)

colour.plotting.colour_style()

colour.utilities.describe_environment();


LIGHTHOUSE_IMAGE = colour.io.read_image("Images/Light_house.png")

test = colour.io.read_image_Imageio("Images/Light_house.png")

test = test[::-1] # todo удалить лишний слой прозрачности

colour.plotting.plot_image(
    colour.cctf_encoding(LIGHTHOUSE_IMAGE),
    text_kwargs={'text': 'Lighthouse - R914108 - Kodak'});


CFA = mosaicing_CFA_Bayer(LIGHTHOUSE_IMAGE)

colour.plotting.plot_image(
    colour.cctf_encoding(CFA),
    text_kwargs={'text': 'Lighthouse - CFA - RGGB'})

colour.plotting.plot_image(
    colour.cctf_encoding(mosaicing_CFA_Bayer(LIGHTHOUSE_IMAGE, 'BGGR')),
    text_kwargs={'text': 'Lighthouse - CFA - BGGR'});

colour.plotting.plot_image(
    colour.cctf_encoding(demosaicing_CFA_Bayer_bilinear(CFA)),
    text_kwargs={'text': 'Lighthouse - Demosaicing - Bilinear'});