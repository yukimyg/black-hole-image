import numpy as np

import internal.calculation as calc
import internal.mapping as _map
from internal.datas import Const as const
import set_values as sv


def main():
    distance = sv.distance
    W = sv.image_width
    H = sv.image_height
    input_name = sv.input_name
    output_name = sv.output_name

    x0 = np.pi
    dx = np.pi / W
    rs = 2 * sv.mass_bh * const.newtonian_g / const.c ** 2

    calc.main(H, W, dx, x0, rs, distance)
    _map.main(H, W, input_name, output_name)


if __name__ == "__main__":
    main()
