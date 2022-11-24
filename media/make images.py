from PIL import Image

image = Image.new(mode="RGB", size=(1682, 1052), color="black")
image.save("input.png")
pixel_map = image.load()

for i in range(0, 1682):
    pixel_map[i, 0] = (255, 255, 255)
    pixel_map[i, 1051] = (255, 255, 255)

for i in range(0, 1052):
    pixel_map[0, i] = (255, 255, 255)
    pixel_map[1681, i] = (255, 255, 255)
image.save("output.png")
