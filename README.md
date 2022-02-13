# <div style="text-align: center;">Black Hole Image</div>
 [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview
You can make gravitational lensing for any back ground image. 
## Description
### Feature
Make images that is view of static observer near the Black Hole.  
Able to set the following values.
- Mass of Black Hole
- Distance between the Observer and event horizon measured by Observer at the infinite point.

 Then, calculate geodesic raytracing in Schwarzschild time-space every pixels. For it, used automatic parallelization with `@jit` of Numba.

### Future feature
The following are not yet implemented.
- redshift and blueshift (doppler, gravitational)
- Set gass and dust around Black Hole. (Assume the existence of an accretion disk.)
- Kerr time-space

### Physical Explanation
comming soon...
<!-- ## Demo -->

<!-- ## VS.  -->

## Requirement

- [Python3](https://wiki.python.org/moin/BeginnersGuide/Download)
- [NumPy](https://numpy.org/install/)
- [Numba](https://numba.readthedocs.io/en/stable/user/installing.html)
- [Open CV](https://docs.opencv.org/4.x/df/d65/tutorial_table_of_content_introduction.html)


## Useage
1. Choose a image back ground of gravitational lensing.
   - For example, [
GAIA'S SKY IN COLOUR](https://sci.esa.int/web/gaia/-/60196-gaia-s-sky-in-colour-equirectangular-projection) ([ESA](https://www.esa.int/))
2. Set back ground image to [`./inputs`](./inputs)
3. Set values at [set_values.py](set_values.py)  
  The following arguments are required :
     - `mass_bh` : Mass of Blak Hole.
     - `distance` : Length between Event Horizon and Observer. It is measured from the infinite point.
     - `image_width` : Width of output image.(pixels)
     - `image_height` : Height of output image.(pixels)
     - `input_name` : Name of input image.
     - `output_name` : Name of output image.
   
   Then, you can use several included connstants.  Check [reference](./docs/value_refarence.md).
   #### Example
   ```py
   from internal.datas import Const as const
   from internal.datas import Image as image


   mass_bh = 100 * const.mass_sun

   # rs : Schwarzschild radius
   rs = 2 * mass_bh * const.newtonian_g / const.c**2
   distance = 3 * rs

   image_width = image.fhd.width
   image_height = image.fhd.height

   input_name = "input.png"
   output_name = "output.png"
   ```
4. Run the following command.
   ```sh
   python main.py
   ```
5. Result image are outputted to [`./outputs`](./outputs/)

<!-- ## Install -->

<!-- ## Contribution -->

## Licence
This software is released under the MIT License, see [LICENSE](./LICENSE).

## Author

[Yuki Miyagi](https://github.com/yukimyg)
