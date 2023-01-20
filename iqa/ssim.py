import math
import numpy as np
import cv2

def ssim(optical, sar2op):
    C1 = (0.01 * 255)**2
    C2 = (0.03 * 255)**2

    optical = optical.astype(np.float64)
    sar2op = sar2op.astype(np.float64)
    kernel = cv2.getGaussianKernel(11, 1.5)
    window = np.outer(kernel, kernel.transpose())

    mu1 = cv2.filter2D(optical, -1, window)[5:-5, 5:-5]  # valid
    mu2 = cv2.filter2D(sar2op, -1, window)[5:-5, 5:-5]
    mu1_sq = mu1**2
    mu2_sq = mu2**2
    mu1_mu2 = mu1 * mu2
    sigma1_sq = cv2.filter2D(optical**2, -1, window)[5:-5, 5:-5] - mu1_sq
    sigma2_sq = cv2.filter2D(sar2op**2, -1, window)[5:-5, 5:-5] - mu2_sq
    sigma12 = cv2.filter2D(optical * sar2op, -1, window)[5:-5, 5:-5] - mu1_mu2

    ssim_map = ((2 * mu1_mu2 + C1) * (2 * sigma12 + C2)) / ((mu1_sq + mu2_sq + C1) *
                                                            (sigma1_sq + sigma2_sq + C2))
    return ssim_map.mean()


def calculate_ssim(optical, sar2op):
    '''calculate SSIM
    the same outputs as MATLAB'
    optical, sar2op: [0, 255]
    '''
    if not optical.shape == sar2op.shape:
        raise ValueError('Input images must have the same dimensions.')
    if optical.ndim == 2:
        return ssim(optical, sar2op)
    elif optical.ndim == 3:
        if optical.shape[2] == 3:
            ssims = []
            for i in range(3):
                ssims.append(ssim(optical, sar2op))
            return np.array(ssims).mean()
        elif optical.shape[2] == 1:
            return ssim(np.squeeze(optical), np.squeeze(sar2op))
    else:
        raise ValueError('Wrong input image dimensions.')