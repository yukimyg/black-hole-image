import cv2
import numpy as np


def mapping(xim, yim, im0, im1):
    yim1 = yim.astype(np.uint64)
    xim1 = xim.astype(np.uint64)

    imb = im0[:, :, 0]
    img = im0[:, :, 1]
    imr = im0[:, :, 2]

    im1[:, :, 0] = imb[yim1, xim1]
    im1[:, :, 1] = img[yim1, xim1]
    im1[:, :, 2] = imr[yim1, xim1]
    return im1


def main(H, W, input_name, output_name):
    theta = np.load("./internal/angles_data/theta.npy")
    fai = np.load("./internal/angles_data/fai.npy")
    im0 = cv2.imread(f"./inputs/{input_name}")
    H0, W0, _ = im0.shape
    im1 = np.empty((H, W, 3), dtype="u8")

    xim = np.round((1 + theta / np.pi) * W0 / 2)
    xim = np.where(xim > W0 - 1, xim % W0, xim)
    xim = np.where(xim < 0, W0 - (-xim) % W0, xim)

    yim = np.round((1 + 2 * fai / np.pi) * H0 / 2)
    yim = np.where(yim > H0 - 1, yim % H0, yim)
    yim = np.where(yim < 0, H0 - (-yim) % H0, yim)

    im1 = mapping(xim, yim, im0, im1)
    zeros = np.zeros((H, W))
    # Blacken the shadow
    for i in range(3):
        im1[:, :, i] = np.where(np.abs(theta) >= 100, zeros, im1[:, :, i])

    cv2.imwrite(f"outputs/{output_name}", im1)


if __name__ == "__main__":
    main()
