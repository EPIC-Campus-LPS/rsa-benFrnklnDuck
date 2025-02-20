from cv2 import VideoCapture, imwrite
from blake3 import blake3

cam = VideoCapture(0)
array = []

upper = int(input("Highest number to generate: "))
lower = int(input("Lowest number to generate: "))
diff = upper - lower

for j in range(100):
    result, image = cam.read()

    imwrite("Image.png", image)

    with open("Image.png", "rb") as file:
        image_bytes = file.read()

    image_hash = blake3(image_bytes).hexdigest()
    i = int(image_hash, 16)
    i = i % diff
    i = i + lower
    array.append(i)

print(array)