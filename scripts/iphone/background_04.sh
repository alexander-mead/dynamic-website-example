#!/bin/sh

real=-0.34852
imag=-0.60653
zoom=5000.
iterations=10000
sigma=0.5
transform='square_root'
width=750
height=1334
outdir='images'
outfile='iphone/background_04'
cmap='cubehelix'
format='png'
resample=10

poetry run python api/image.py real=$real imag=$imag zoom=$zoom iterations=$iterations sigma=$sigma transform=$transform\
    width=$width height=$height outdir=$outdir outfile=$outfile cmap=$cmap format=$format resample=$resample
