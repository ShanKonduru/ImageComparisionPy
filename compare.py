import os
from PIL import Image
import cv2
import numpy as np

def compare_images(image1_path, image2_path):
    # File Size
    image1_size = os.path.getsize(image1_path)
    image2_size = os.path.getsize(image2_path)
    print("File Size Comparison:")
    print("Image 1 Size:", image1_size, "bytes")
    print("Image 2 Size:", image2_size, "bytes")
    
    # File Type
    image1_type = image1_path.split('.')[-1]
    image2_type = image2_path.split('.')[-1]
    print("\nFile Type Comparison:")
    print("Image 1 Type:", image1_type)
    print("Image 2 Type:", image2_type)

    # File Content Comparison
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)
    
    # Check if images have the same dimensions
    if image1.size != image2.size:
        print("Error: Images have different dimensions.")
        return

    image1_data = np.array(image1)
    image2_data = np.array(image2)
    content_diff = np.sum(image1_data != image2_data)
    print("\nFile Content Comparison:")
    print("Images differ in", content_diff, "pixels.")
    
    # Image Size Comparison
    image1_size_px = image1.size
    image2_size_px = image2.size
    print("\nImage Size Comparison:")
    print("Image 1 Size:", image1_size_px)
    print("Image 2 Size:", image2_size_px)
    
    # Confidence Levels (Mean Squared Error)
    print("\nConfidence Levels (Mean Squared Error):")
    mse = np.mean((image1_data - image2_data) ** 2)
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":
    image1_path = "testdata/image1.jpg"
    image2_path = "testdata/image2.jpg"
    compare_images(image1_path, image2_path)
