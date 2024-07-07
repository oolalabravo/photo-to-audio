import numpy as np
from PIL import Image
from scipy.io.wavfile import read

def wav_to_image(wav_path, output_image_path):
    # Read the WAV file
    sample_rate, pcm_data_with_dimensions = read(wav_path)
    
    # Extract dimensions
    height = pcm_data_with_dimensions[0]
    width = pcm_data_with_dimensions[1]
    channels = pcm_data_with_dimensions[2]
    original_image_shape = (height, width, channels)
    
    # Extract the image data
    pcm_data = pcm_data_with_dimensions[3:]
    
    # Convert the PCM data back to normalized data
    normalized_data = pcm_data / 32767.0
    
    # Convert the normalized data back to original range [0, 255]
    image_data = (normalized_data * 128 + 128).astype(np.uint8)
    
    # Reshape the data to original image shape
    reshaped_data = image_data.reshape(original_image_shape)
    
    # Create and save the image from reshaped data
    image = Image.fromarray(reshaped_data)
    image.save(output_image_path)

# Example usage to convert WAV back to image
wav_path = r'audio path here'
output_image_path = r'image path here'

wav_to_image(wav_path, output_image_path)
print(f"WAV file '{wav_path}' converted back to image '{output_image_path}'.")
