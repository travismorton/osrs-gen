import argparse
import io
import sys
from PIL import ImageFont, Image, ImageDraw


def gen_image(text, fo, size=28):
    font = ImageFont.truetype("runescape_uf.ttf", size)
    width, height = font.getsize_multiline(text)

    vbuffer = 10
    hbuffer = 10
    width = width + hbuffer * 2
    height = height + vbuffer * 2

    img = Image.new("RGBA", (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.multiline_text((hbuffer, vbuffer), text, font=font, fill=(255, 255, 0, 255))
    img.save(fo, "png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("text", type=str, help="string to generate image from")

    parser.add_argument(
        "--filename",
        "-f",
        help="path to output file",
        type=str,
        nargs="?",
        default=None,
    )
    args = parser.parse_args()

    if args.filename:
        with open(args.filename, "wb") as f:
            gen_image(args.text, f)
    else:
        f = io.BytesIO()
        gen_image(args.text, f)
        sys.stdout.buffer.write(f.getvalue())
