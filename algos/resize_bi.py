import numpy as np
from PIL import Image
from alive_progress import alive_bar


def resize_i_bi(img_now, fator=0.5):
    w1 = img_now.shape[0]
    h1 = img_now.shape[1]

    w2 = int(np.floor(w1*fator))
    h2 = int(np.floor(h1*fator))

    if len(img_now.shape) < 3:
        temp = np.empty((w2, h2))
    else:
        temp = np.empty((w2, h2, 3))
    with alive_bar(h2, force_tty=True) as bar:
        for j in range(h2):
            for i in range(w2):
                scalerx = i/fator
                scalery = j/fator
                x = min(int(np.floor(i/fator)), w1-1)
                y = min(int(np.floor(j/fator)), h1-1)
                x2 = min(x+1, w1-1)
                y2 = min(y+1, h1-1)
                p1 = (x2-scalerx)*img_now[x, y]+(scalerx-x)*img_now[x2, y]
                p2 = (x2-scalerx)*img_now[x, y2]+(scalerx-x)*img_now[x2, y2]
                if x == x2:
                    p1 = img_now[x, y]
                    p2 = img_now[x2, y2]
                if y == y2:
                    p = img_now[x2, y2]
                else:
                    p = (y2-scalery)*p1+(scalery-y)*p2
                temp[i, j] = p
            bar()

    img_now = temp.astype(np.uint8)

    return img_now
