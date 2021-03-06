# Black Hole Image

[![Maintainability](https://api.codeclimate.com/v1/badges/25f1b0c4e9d1ef1d1b9e/maintainability)](https://codeclimate.com/github/yukimyg/black_hole_image/maintainability) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/ccb0fbe17c6c4aaba4dc139ef3c33b48)](https://www.codacy.com/gh/yukimyg/black-hole-image/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=yukimyg/black-hole-image&amp;utm_campaign=Badge_Grade) [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/yukimyg/black-hole-image.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yukimyg/black-hole-image/context:python)
 [![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.0-4baaaa.svg)](CODE_OF_CONDUCT.md) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Note: This project is not yet ready for production.

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
- [SciPy](https://scipy.org/download/)
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

   Example

   ```py
   from internal.datas import Const as const
   from internal.datas import Image as image
   
   
   mass_bh = 100 * const.mass_sun
   
   # rs : Schwarzschild radius
   rs = 2 * mass_bh * const.newtonian_g / const.c ** 2
   distance = 5 * rs
   
   image_width = image.uhd.width
   image_height = image.uhd.height
   
   input_name = "input.png"
   output_name = "output.png"
   ```

4. Run the following command.

   ```sh
   python main.py
   ```

5. Result image are outputted to [`./outputs`](./outputs/)

<!-- ## Install -->

## Contribution

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Licence

This software is released under the MIT License, see [LICENSE](./LICENSE).

## Author

[Yuki Miyagi](https://github.com/yukimyg)
