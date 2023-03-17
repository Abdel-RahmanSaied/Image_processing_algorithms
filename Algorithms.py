import numpy as np
from PIL import Image

class Algorithms():
    def __init__(self, img_path):
        self.img_path = img_path
        img = Image.open('image.jpg').convert('L')
        self.data = np.array(img)

    def thresholding(self):
        threshold = 128
        thresholded_data = ((self.data > threshold) * 255).astype(np.uint8)
        thresholded_img = Image.fromarray(thresholded_data)
        thresholded_img.save('result/thresholded.png')
        return "done and saved"

    def Error_diffusion_dithering(self):
        fs_data = self.data.copy()
        for i in range(fs_data.shape[0]):
            for j in range(fs_data.shape[1]):
                old_pixel = fs_data[i, j]
                new_pixel = 255 if old_pixel > 128 else 0
                fs_data[i, j] = new_pixel
                quant_error = old_pixel - new_pixel
                if j < fs_data.shape[1] - 1:
                    fs_data[i, j+1] += quant_error * 7 / 16
                if i < fs_data.shape[0] - 1 and j > 0:
                    fs_data[i+1, j-1] += quant_error * 3 / 16
                if i < fs_data.shape[0] - 1:
                    fs_data[i+1, j] += quant_error * 5 / 16
                if i < fs_data.shape[0] - 1 and j < fs_data.shape[1] - 1:
                    fs_data[i+1, j+1] += quant_error * 1 / 16
        fs_img = Image.fromarray(fs_data)
        fs_img.save('result/fs.png')
        return "done and saved"

    def Ordered_dithering(self):
        order_data = np.zeros_like(self.data)
        for i in range(order_data.shape[0]):
            for j in range(order_data.shape[1]):
                if self.data[i, j] > np.array([[0, 128], [192, 64]])[i%2, j%2]:
                    order_data[i, j] = 255
                else:
                    order_data[i, j] = 0
        order_img = Image.fromarray(order_data)
        order_img.save('result/order.png')
        return "done and saved"

    def Pattern_dithering(self):
        patterns = np.array([
            [[0, 128], [192, 64]],
            [[192, 64], [0, 128]],
            [[64, 192], [128, 0]],
            [[128, 0], [64, 192]]
        ])
        pattern_data = np.zeros_like(self.data)
        for i in range(self.data.shape[0]):
            for j in range(self.data.shape[1]):
                x = i % patterns.shape[0]
                y = j % patterns.shape[1]
                # threshold = patterns[x, y][i % 2, j % 2]
                threshold = patterns[x][i % 2, j % 2]
                new_pixel = 255 if self.data[i, j] > threshold else 0
                pattern_data[i, j] = new_pixel

        pattern_img = Image.fromarray(pattern_data)
        pattern_img.save('result/pattern.png')
        return "done and saved"
