# Monodepth-GIFTest

This repository consists the code for the testing function of the continous frames and creating a gif output using the pretrained models weights. The pretrained model weights are downloaded from the monolab testing funtion to get the accurate results and the script for the video feed is written.

## How to run
The code runs on Python 3.6+, Pytorch 0.4.1 and has a couple of other requirements. The network architecture and the layers must be according to the Godard architecture because the pretrained weights we used are of their model. If any other wights are used then the networks must be changes accordingly.

You can test on a directory of the frames by running `gif_test.py`, which is parametrized with the following main arguments:
- `--image_path`: The path to the test image. In case of continous frames, provide the path to the image directory.
- `--ext`: Type of extension of the test image.(png,jpeg,jpg etc)

You can also test on a single image by running `test_simple.py`

![](./assets/output.gif)
