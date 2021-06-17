from pathlib import Path

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PIL import Image

root = Path(__file__).parent
source_image_path = root / "tux.png"
output_dir_path = root / "output"

key = b"Careful with ECB"
iv = b"Instead, use CBC"

resize_scale_factor = 16

# make the output directory
output_dir_path.mkdir(parents=True, exist_ok=True)

# get the source image's data and properties
with Image.open(source_image_path) as source_image:
    data = source_image.tobytes()

    size = source_image.size
    mode = source_image.mode

upscaled_size = (size[0] * resize_scale_factor, size[1] * resize_scale_factor)

# ========
# ECB mode
# ========
# create encryptor
ecb_cipher = Cipher(algorithms.AES(key), modes.ECB())
ecb_encryptor = ecb_cipher.encryptor()  # type: ignore

# encrypt the pixel data
ecb_ciphertext = ecb_encryptor.update(data) + ecb_encryptor.finalize()

# make new image from encrypted data and save
ecb_image = Image.frombytes(mode, size, ecb_ciphertext)
ecb_image.save(output_dir_path / "tux.aes-ecb.1x.png")

# do the same for an upscaled version
ecb_image_upscaled = ecb_image.resize(upscaled_size, Image.NEAREST)
ecb_image_upscaled.save(output_dir_path / f"tux.aes-ecb.{resize_scale_factor}x.png")

# ========
# CBC mode
# ========
cbc_cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
cbc_encryptor = cbc_cipher.encryptor()  # type: ignore

cbc_ciphertext = cbc_encryptor.update(data) + cbc_encryptor.finalize()

cbc_image = Image.frombytes(mode, size, cbc_ciphertext)
cbc_image.save(output_dir_path / "tux.aes-cbc.1x.png")

cbc_image_upscaled = cbc_image.resize(upscaled_size, Image.NEAREST)
cbc_image_upscaled.save(output_dir_path / f"tux.aes-cbc.{resize_scale_factor}x.png")
