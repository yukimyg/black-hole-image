import numpy as np
import numba
from numba import jit


@jit("f8(f8,f8)", nopython=True, nogil=True, cache=True, fastmath=True)
def f(rs, u):
    f = -u + 3 / 2 * rs * u ** 2
    return f


@jit(
    "f8[:](f8,f8,f8,f8,f8)",
    nopython=True,
    # parallel=True,
    nogil=True,
    cache=True,
    fastmath=True,
)
def runge_kutta(r0, x0, dx, b, rs):
    ui = 1 / r0
    u = ui
    v = -u * (1 - rs / r0) ** (1 / 2) / np.tan(np.pi - b)

    x = x0
    xi = x0
    while xi <= 5 * np.pi:

        if 1 / ui <= rs:
            xi = x
            ui = u
            break
        if 1 / ui >= 3.3 * 10 ** 10 * rs:
            xi = x
            ui = u
            break

        x = xi
        u = ui
        dv_1 = dx * f(rs, u)
        du_1 = dx * v
        dv_2 = dx * f(rs, u + du_1 / 2)
        du_2 = dx * (v + dv_1 / 2)
        dv_3 = dx * f(rs, u + du_2 / 2)
        du_3 = dx * (v + dv_2 / 2)
        dv_4 = dx * f(rs, u + du_3)
        du_4 = dx * (v + dv_3)

        xi = x + dx
        v = v + (1 / 6) * (dv_1 + 2 * dv_2 + 2 * dv_3 + dv_4)
        ui = u + (1 / 6) * (du_1 + 2 * du_2 + 2 * du_3 + du_4)

    a = np.array([xi, 1 / ui])
    return a


@jit(
    "f8[:,:,:](i8,i8,f8,f8,f8,f8[:,:,:],f8)",
    nopython=True,
    parallel=True,
    nogil=True,
    cache=True,
    fastmath=True,
)
def ray_tracing(H1, W1, r0, dx, x0, info, rs):
    image0 = np.zeros((H1, W1, 2))
    al = 0.0
    for i in numba.prange(H1):
        for j in numba.prange(W1):
            a = runge_kutta(r0, x0, dx, info[i, j, 0], rs)
            fai0 = a[0]
            r = a[1]
            al = info[i, j, 1]
            rotx = np.array(
                [
                    [1.0, 0.0, 0.0],
                    [0.0, np.cos(al), -np.sin(al)],
                    [0.0, np.sin(al), np.cos(al)],
                ]
            )
            if r <= 1.5 * rs:
                image0[i, j, :] = 1000
            elif np.isnan(r):
                image0[i, j, :] = 100
            else:
                xyz0 = np.array([np.cos(fai0), np.sin(fai0), 0])
                xyz = rotx @ xyz0
                fai = np.arcsin(xyz[2])
                if xyz[1] >= 0:
                    theta = np.arccos(xyz[0] / np.cos(fai))
                elif xyz[1] < 0:
                    theta = -np.arccos(xyz[0] / np.cos(fai))

                image0[i, j, 0] = fai
                image0[i, j, 1] = theta
    return image0


def grid_make(H1, W1):
    subangle = np.empty((H1, W1, 2))

    # fai
    subangle[:, :, 0] = -np.tile(
        np.linspace(np.pi / 2 - np.pi / 2 / H1 / 2, np.pi / 2 / H1 / 2, H1).reshape(
            H1, 1
        ),
        (1, W1),
    )

    # theta
    subangle[:, :, 1] = np.tile(
        np.linspace(np.pi / W1 / 2, np.pi - np.pi / W1 / 2, W1), (H1, 1)
    )

    # the viewing vector
    v2 = np.empty((H1, W1, 3))
    v2[:, :, 0] = np.cos(subangle[:, :, 1]) * np.cos(subangle[:, :, 0])
    v2[:, :, 1] = -np.sin(subangle[:, :, 1]) * np.cos(subangle[:, :, 0])
    v2[:, :, 2] = -np.sin(subangle[:, :, 0])

    # grid of tilt of impact parameter and rotation
    info = np.empty((H1, W1, 2))
    ryz = np.sqrt(v2[:, :, 1] * v2[:, :, 1] + v2[:, :, 2] * v2[:, :, 2])
    rxyz = np.sqrt(
        v2[:, :, 0] * v2[:, :, 0]
        + v2[:, :, 1] * v2[:, :, 1]
        + v2[:, :, 2] * v2[:, :, 2]
    )
    sina1 = ryz / rxyz
    cosa1 = v2[:, :, 0] / rxyz
    info[:, :, 0] = np.arctan2(sina1, cosa1)
    sina2 = v2[:, :, 2] / ryz
    cosa2 = v2[:, :, 1] / ryz
    info[:, :, 1] = np.arctan2(sina2, cosa2)
    return info


def main(H, W, dx, x0, rs, dis):
    W1 = int(W / 2)
    H1 = int(H / 2)

    info = grid_make(H1, W1)
    im0 = ray_tracing(H1, W1, dis, dx, x0, info, rs)

    image = np.zeros((H, W, 2))
    image[:H1, W1:, :] = im0
    image[H1:, W1:, 0] = -im0[::-1, :, 0]
    image[H1:, W1:, 1] = im0[::-1, :, 1]
    image[:, :W1, 0] = image[:, W : W1 - 1 : -1, 0]
    image[:, :W1, 1] = -image[:, W : W1 - 1 : -1, 1]

    fai = image[:, :, 0]
    theta = image[:, :, 1]

    np.save("./internal/angles_data/fai.npy", fai)
    np.save("./internal/angles_data/theta.npy", theta)


if __name__ == "__main__":
    main()
