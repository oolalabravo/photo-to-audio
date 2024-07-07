import numpy as np
from PIL import Image
from scipy.io.wavfile import write

def image_to_wav(image_path, wav_path):
    # Open the image file
    image = Image.open(image_path)
    image_data = np.array(image)
    
    # Get the dimensions of the image
    height, width, channels = image_data.shape
    dimensions = np.array([height, width, channels], dtype=np.int16)
    
    # Flatten the image data to 1D array and normalize it to [-1, 1] range
    flattened_data = image_data.flatten()
    normalized_data = (flattened_data - 128) / 128.0
    
    # Convert the normalized data to 16-bit PCM format
    pcm_data = np.int16(normalized_data * 32767)
    
    # Concatenate dimensions and image data
    pcm_data_with_dimensions = np.concatenate((dimensions, pcm_data))

    # Save the PCM data as a WAV file
    write(wav_path, 44100, pcm_data_with_dimensions)

# Example usage to convert image to WAV
image_path = r'image path here'
wav_path = r'generated audio path here'

image_to_wav(image_path, wav_path)
print(f"Image '{image_path}' converted to WAV file '{wav_path}'.")
