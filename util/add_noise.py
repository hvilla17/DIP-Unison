# File: add_noise.py
import numpy as np


def add_gaussian_noise(image, mean=0, sigma=0.1):
    """Add Gaussian noise with mean and standard deviation sigma."""
    noise = np.random.normal(mean, sigma, image.shape)
    noisy_img = np.clip(image + noise, 0, 1)
    return noisy_img


def add_salt_and_pepper_noise(image, salt_prob=0.02, pepper_prob=0.02):
    """
    Add salt-and-pepper noise with independent salt and pepper probabilities.
    salt_prob: probability of a pixel turning white
    pepper_prob: probability of a pixel turning black
    """
    noisy_img = image.copy()
    rows, cols = image.shape[:2]

    # Random mask for salt
    salt_mask = np.random.rand(rows, cols) < salt_prob
    # Random mask for pepper
    pepper_mask = np.random.rand(rows, cols) < pepper_prob

    if image.ndim == 2:  # grayscale
        noisy_img[salt_mask] = 1
        noisy_img[pepper_mask] = 0
    else:  # color
        noisy_img[salt_mask, :] = 1
        noisy_img[pepper_mask, :] = 0

    return noisy_img
