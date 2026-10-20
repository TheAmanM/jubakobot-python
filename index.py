from PIL import Image, ImageDraw

images = {}

for i in range(12):
    images[str(i + 1)] = Image.open(f'./{i + 1}.png')
    print(f"Opened {i + 1}!")

rectWidth = 8

for i in range(12):
    for j in range(12):
        canvas = Image.new('RGBA', (256, 512), (255, 255, 255, 255))
        canvas.paste(images[str(i + 1)], (0, 0))
        canvas.paste(images[str(j + 1)], (0, 256))
        finalCanvas = ImageDraw.Draw(canvas)
        finalCanvas.rectangle(
            (0, 256 - rectWidth / 2, 256, 256 + rectWidth / 2), (255, 255, 255, 255))
        finalCanvas.rectangle(fill=None, outline=(
            255, 255, 255, 255), xy=(0, 0, 256, 512), width=8)
        canvas.save(f'./assets/{i + 1}-{j + 1}.png')
        print(f"{i * 12 + j + 1} / 144")
