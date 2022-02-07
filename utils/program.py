import numpy as np
from PIL import Image
from utils.functions import *
from algos.resize_bi import resize_i_bi

import matplotlib.pyplot as plt


class Program():
    def __init__(self, fator=0.6):
        self.fator = fator
        self.file_path = "benchmark.bmp"
        self.output_path = "outputs/compressed"
        self.compress_path = "outputs/compressed.npy"
        self.out_file = 'outputs/benchmark_descompressed.bmp'

        self.original_img = Image.open(self.file_path)
        self.original_img = np.array(self.original_img, np.uint8)

        self.shape = self.original_img.shape
        self.height, self.width = generate_hw(self.fator, self.shape)

    # compression
    def compress(self):
        # Resizing image
        print(f"Resizing Image to {self.fator*100:.0f}% of the size.........")
        smaller_original = resize_i_bi(self.original_img, self.fator)
        print("Resized successful\n")

        s_blue, s_green, s_red = split_channels(smaller_original)

        print("Encoding arrays with RLE algorithm.........")
        sencrypted_array = encode_arrays(s_blue, s_green, s_red)
        print("Encoded successful\n")

        np.save(self.output_path, sencrypted_array)

        output_path = self.compress_path
        calculate_stats(self.file_path, output_path)

    # descompression
    def descompress(self, show=False):
        compress_path = self.compress_path
        out_file = self.out_file

        sloaded = np.load(compress_path, allow_pickle=True)

        print("Decoding arrays.........")
        completed_img = decode_arrays(sloaded, self.width, self.height)
        print("Decoded successful\n")

        final_img = Image.fromarray(completed_img)
        final_img = final_img.resize((self.shape[1], self.shape[0]))
        final_img.save(out_file)

        print(f'Descompressed image generated as {out_file}\n')

        if show:
            print("Generating visualization of images.........")
            bar_generate_view()
            print("Generated successful\n")

            im = Image.open(self.file_path)
            m = np.array(im)

            im_c = Image.open(out_file)
            m_c = np.array(im_c)

            fig, axes = plt.subplots(1, 2, figsize=(
                16, 8), constrained_layout=True)

            axes[0].imshow(m)
            axes[1].imshow(m_c)
            plt.show()


if __name__ == '__main__':
    prog = Program()
    prog.descompress()
