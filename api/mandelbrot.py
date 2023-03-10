import io
import numpy as np
import matplotlib.pyplot as plt
import hydra
from omegaconf import DictConfig, OmegaConf


def sample_area(real_start, real_end, imag_start, image_end, max_iters, width, height):
    """
    Loops over an area and assigns points to the Mandelbrot set
    Thanks chatGPT for this vectorized version (although it was wrong to begin with)
    """
    x, y = np.meshgrid(np.linspace(real_start, real_end, width),
                       np.linspace(imag_start, image_end, height))
    mandelbrot_set = np.zeros((height, width))
    c = x + y * 1j        # Map x, y to their complex values
    z = np.zeros_like(c)  # Initialise the value of 'z' at each location
    for i in range(max_iters):
        z = z**2 + c               # Iterate
        mask = np.abs(z) > 2.      # Select points that are diverging
        mandelbrot_set[mask] = i   # Set is number of iterations for divergence
        z[mask], c[mask] = 0., 0.  # Reset the diverging point so that it will not diverge in future
    return mandelbrot_set


def create_image(real_start, real_end, imag_start, image_end, max_iters, width, height,
                 cmap="cubehelix", figsize=(8, 8), dpi=150):
    """
    Create a png and return it as a binary
    """
    array = sample_area(real_start, real_end, imag_start,
                        image_end, max_iters, width, height)
    plt.subplots(figsize=figsize, dpi=dpi, frameon=False)
    plt.imshow(array, cmap=cmap, vmin=0, vmax=max_iters)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches='tight',
                pad_inches=0)  # Place the png as a binary in memory
    return buffer.getvalue()   # Return the png binary (avoids saving to disk)


@hydra.main(version_base=None, config_path="../.", config_name="config")
def run(cfg : DictConfig):

    # Parameters for part of set to display
    iterations = cfg["iterations"]
    width, height = cfg["width"], cfg["height"]
    outdir, outfile = cfg["outdir"], cfg["outfile"]
    verbose = cfg["verbose"]
    rmin = cfg["real"]-(1./cfg["zoom"])*cfg["width"]/cfg["height"]
    rmax = cfg["real"]+(1./cfg["zoom"])*cfg["width"]/cfg["height"]
    imin, imax = cfg["imag"]-(1./cfg["zoom"]), cfg["imag"]+(1./cfg["zoom"])
    cmap = cfg["cmap"]

    # Write to screen
    if verbose:
        print()
        print('Mandelbrot set parameters:')
        print('Minimum and maximum real values:', rmin, rmax)
        print('Minimum and maximum imaginary values:', imin, imax)
        print('Maximum number of iterations:', iterations)
        print('Width and height of image:', width, height)
        print('Output directory and file:', outdir, outfile)
        print()


    # Display an image on screen and simulatanouesly save it
    create_image(rmin, rmax, imin, imax, iterations, width, height, dpi=224, cmap=cmap)
    plt.savefig(outdir+"/"+outfile, bbox_inches='tight', pad_inches=0)
    plt.show()
    plt.close()

if __name__ == "__main__":
    run()
