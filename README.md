# aes-tux

Encrypts the pixel data of an image to demonstrate a weakness of the
[ECB](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_codebook_(ECB))
block cipher mode (in contrast to the stronger
[CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC))
mode).

This project was inspired by the images on the Wikipedia article linked to above, which is a
popular reference for learning about ECB:

> Lots of people know that when you encrypt something in ECB mode, you can **see penguins** through
> it.

-- "Byte-at-a-time ECB decryption (Simple)", <https://cryptopals.com/sets/2/challenges/12>,
  emphasis mine

## Demonstration

### Original

![original Tux image](https://raw.githubusercontent.com/t-mart/aes-tux/master/tux.png)

[source](https://raw.githubusercontent.com/t-mart/aes-tux/master/tux.png)

### ECB Encrypted

![ECB encrypted Tux image](https://raw.githubusercontent.com/t-mart/aes-tux/master/output/tux.aes-ecb.1x.png)

[source](https://raw.githubusercontent.com/t-mart/aes-tux/master/output/tux.aes-ecb.1x.png),
[source 16x upscaled](https://raw.githubusercontent.com/t-mart/aes-tux/master/output/tux.aes-ecb.16x.png)

### CBC Encrypted

![CBC encrypted Tux image](https://raw.githubusercontent.com/t-mart/aes-tux/master/output/tux.aes-cbc.1x.png)

[source](https://raw.githubusercontent.com/t-mart/aes-tux/master/output/tux.aes-cbc.1x.png),
[source 16x upscaled](https://raw.githubusercontent.com/t-mart/aes-tux/master/output/tux.aes-cbc.16x.png)

## Image Used

The image used is of the Linux mascot, Tux.

### Permission

The Tux image contained in this project is derived from one by Larry Ewing. According to his
webpage, [permission has been granted](https://isc.tamu.edu/~lewing/linux/) to
use/modify this image by acknowledging:

- the author himself, Larry Ewing, at [lewing@isc.tamu.edu](mailto://lewing@isc.tamu.edu)
- the GIMP project at <https://gimp.org>

### Image Modifications

Some modifications have been done to Larry's image to make them more acceptable for this exercise:

- The image has been saved in the PNG format, a more modern alternative to GIF.

- The image palette has been removed.

  This is necessary because the original pixel data refers to a palette of a fixed size.
  Encrypting the pixel data might cause it to then refer to palette indexes that don't exist.

- Transparency has been replaced with simply white pixels. (I'm not completely sure how alpha layers
  work at the binary level, so I just converted the transparency to white.)

- The image has been resized so that the number of pixels is divisible by the AES block size of
  16 bytes. Specifically, the image has been made square by adding some columns to the left
  and right of the original. (A square image is not necessary -- its just a pleasing
  size that happens to divide by 16 in this case.)

## Encryption Process

This project uses the [AES](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard) algorithm
to encrypt pixel data of the image. An image processing library has been used to ensure that the
encryption is only done on the pixel data and NOT any image container data.

### Parameters

- **Key** (for ECB and CBC mode):

  ```plaintext
  Careful with ECB
  ```

- **IV** (for CBC mode):

  ```plaintext
  Instead, use CBC
  ```

Both of the them are 16-byte (128-bit) ASCII-encoded pieces of data.

### Why not pad?

Usually, data to be encrypted with a block cipher (like AES) is padded to ensure that it can work
on evenly-sized blocks. Various schemes like [PKCS #7](https://en.wikipedia.org/wiki/PKCS_7) can do
this.

An interesting quality about these schemes (as far as I know) is that they *always* adding some
padding to the original data, even if it was already divisible by the cipher's block size.

That presents a problem because the pixel data will be unconditionally augmented with padding bytes.
Which then means the encrypted pixel data will no longer fit in the dimensions of the original
image.

To avert that problem, we ensured that the size of the original pixel data was already divisible by
the block size and just feed it into the cipher unpadded.

## Dependencies

- [Pillow](https://github.com/python-pillow/Pillow)
- [cryptography](https://github.com/pyca/cryptography)

## Installation

1. Get Python 3.9 or greater.
2. Install the dependencies with `pip install -r requirements.txt`.

## Running

1. Run `python aes_tux.py`.
2. See output images in `output` directory.

## License

Copyright 2021 Tim Martin

Licensed under the MIT License: <https://spdx.org/licenses/MIT.html>
