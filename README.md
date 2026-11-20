# MOPNet

MOPNet is a research project for multi-frame infrared small target detection.
It uses a sequence of infrared frames to locate and segment small targets in the current frame.

The model implementation will be released after the associated paper is published.

## Mask visualization

The visualization utility overlays an existing binary segmentation mask on an infrared frame.
Use a mask with the same dimensions as the input frame. Nonzero mask pixels are shown in red.

```sh
python -m pip install Pillow
python tools/visualize_mask.py --image frame.png --mask mask.png --output overlay.png
```
