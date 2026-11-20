"""Overlay an existing binary segmentation mask on an infrared frame."""

import argparse
from pathlib import Path

from PIL import Image


def overlay_mask(image_path: Path, mask_path: Path) -> Image.Image:
    with Image.open(image_path) as image, Image.open(mask_path) as mask:
        if image.size != mask.size:
            raise ValueError(f"Image size {image.size} must match mask size {mask.size}.")
        frame = image.convert("RGB")
        opacity = mask.convert("L").point(lambda value: 128 if value else 0)
        highlight = Image.new("RGB", frame.size, (255, 65, 50))
        return Image.composite(highlight, frame, opacity)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--image", required=True, type=Path, help="Input infrared image")
    parser.add_argument("--mask", required=True, type=Path, help="Binary mask with nonzero foreground")
    parser.add_argument("--output", required=True, type=Path, help="Path for the overlay image")
    args = parser.parse_args()

    if args.output.resolve() in {args.image.resolve(), args.mask.resolve()}:
        parser.error("The output path must differ from both input paths.")
    try:
        result = overlay_mask(args.image, args.mask)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        result.save(args.output)
    except (OSError, ValueError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
