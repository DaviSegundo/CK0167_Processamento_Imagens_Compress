import numpy as np


def encode(image):
    encoded_string = []
    image = np.array(image).astype(np.uint8)
    image_flatten = image.flatten()
    previous = None
    count = 0
    for element in image_flatten:
        if (previous == None):
            previous = element
            count += 1
        else:
            if (previous == element):
                if(count < (2**8)-1):
                    count += 1
                else:
                    encoded_string.append(previous)
                    encoded_string.append(count)
                    previous = element
                    count = 1
            else:
                encoded_string.append(previous)
                encoded_string.append(count)
                previous = element
                count = 1

    encoded_string.append(previous)
    encoded_string.append(count)

    return encoded_string


def decode(coded_image, shape):
    decoded = []
    for index in range(0, len(coded_image), 2):
        element = coded_image[index]
        quantity = coded_image[index+1]
        decoded.extend([element]*quantity)
    decoded_array = np.array(decoded).reshape(shape)

    return decoded_array
