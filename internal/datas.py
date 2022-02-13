import numpy as np
import dataclasses
import internal.images as im


@dataclasses.dataclass(frozen=True)
class Const:
    newtonian_g: float = 6.6743 * 10 ** (-11)
    mass_sun: float = 2 * 10 ** 30
    c: float = 299792458


@dataclasses.dataclass(frozen=True)
class Image:
    sd = im.Sd
    hd = im.Hd
    fhd = im.Fhd
    qhd = im.Qhd
    uhd = im.Uhd
    fuhd = im.Fuhd


@dataclasses.dataclass(frozen=False)
class RayCalc:
    num_begin: float = 0
    num_end: float = np.pi
    step_num: float = 4380
