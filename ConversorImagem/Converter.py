from PIL import Image
import numpy as np


def main():

    img = Image.open("simple_icon.png")
    img.show()

    img_data = np.array(img)
    binary_data = img_data.tobytes()

    with open("original_img.bin", "wb") as file:
        file.write(binary_data)

    with open("original_img.bin", "rb") as original_file:
        data = original_file.read()

    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)

    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())

    data = data[::-1]

    with open("copy_img.bin", "wb") as file:
        file.write(data)

    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)
    modified_img = Image.fromarray(modified_data)
    modified_img.show()


if __name__ == "__main__":
    main()
