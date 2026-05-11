#create image brightness matrix and add it to the image
import numpy as np
def add_brightness(image, brightness):
    #create brightness matrix
    brightness_matrix = np.ones(image.shape) * brightness
    print("Brightness Matrix:\n", brightness_matrix)
    #add brightness matrix to image
    brightened_image = image + brightness_matrix
    return brightened_image.astype(np.uint8)

#example usage
if __name__ == "__main__":
    #create a sample image (3x3 pixels, RGB)
    #create single row image for simplicity
    image = np.array([[[100, 150, 200],
                       [50, 75, 125],
                       [200, 255, 255]]], dtype=np.uint8)
    brightness = 50
    brightened_image = add_brightness(image, brightness)
    print("Original Image:\n", image)
    print("Brightened Image:\n", brightened_image)