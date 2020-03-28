from PIL import Image, ImageDraw, ImageFont


genome_file = open("sars-cov-2-genome-sequence.txt", "r")
genome_sequence = genome_file.readline()
print(len(genome_sequence))

VISUALIZATION_RESOLUTION = (800, 720)
BACKGROUND_COLOR = (128, 128, 128)
PIXEL_SIZE = 4
PADDING = 10
GUANINE_COLOR = (204, 0, 0)
URACIL_COLOR = (0, 128, 255)
ADENINE_COLOR = (255, 128, 0)
CYTOSINE_COLOR = (102, 255, 255)


def base_color(b: str) -> tuple:
    if b == 'g':
        return GUANINE_COLOR
    if b == 't':
        return URACIL_COLOR
    if b == 'a':
        return ADENINE_COLOR
    if b == 'c':
        return CYTOSINE_COLOR


image = Image.new('RGB', VISUALIZATION_RESOLUTION, BACKGROUND_COLOR)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype("Helvetica", size=14)

# TITLE
title = "SARS-CoV-2 RNA sequence visualization"
large_font = ImageFont.truetype("Helvetica", size=24)
title_w, title_h = draw.textsize(title, font=large_font)
draw.text((VISUALIZATION_RESOLUTION[0]/2 - title_w / 2, 10), title, font=large_font)

# GUANINE LEGEND TEXT
draw.rectangle((10, 10, 20, 20), fill=GUANINE_COLOR)
draw.text((25, 10), "GUANINE", fill=(0, 0, 0), font=font)

# URACIL LEGEND TEXT
draw.rectangle((10, 30, 20, 40), fill=URACIL_COLOR)
draw.text((25, 30), "URACIL", fill=(0, 0, 0), font=font)

# ADENINE LEGEND TEXT
draw.rectangle((10, 50, 20, 60), fill=ADENINE_COLOR)
draw.text((25, 50), "ADENINE", fill=(0, 0, 0), font=font)

# CYTOSINE LEGEND TEXT
draw.rectangle((10, 70, 20, 80), fill=CYTOSINE_COLOR)
draw.text((25, 70), "CYTOSINE", fill=(0, 0, 0), font=font)

x, y = (10, 90)
x_offset = 0
y_offset = 0
for base in genome_sequence:
    x_real = x + (x_offset * PIXEL_SIZE)
    y_real = y + (y_offset * PIXEL_SIZE)
    draw.rectangle((x_real, y_real, x_real + PIXEL_SIZE, y_real + PIXEL_SIZE), fill=base_color(base))

    if x_real >= (VISUALIZATION_RESOLUTION[0] - PADDING - 10):
        x_offset = 0
        y_offset = y_offset + 1
    else:
        x_offset = x_offset + 1

image.show()
