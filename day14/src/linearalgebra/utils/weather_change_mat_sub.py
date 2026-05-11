#weather change matrix and subtract it from the image
import numpy as np
def weather_change_mat_sub(image, weather_change_mat):
    #check if the weather change matrix is the same size as the image
    if weather_change_mat.shape != image.shape:
        raise ValueError("Weather change matrix must be the same size as the image")
    #subtract the weather change matrix from the image
    result = image - weather_change_mat
    #clip the result to be between 0 and 255
    result = np.clip(result, 0, 255)
    return result.astype(np.uint8)
if __name__ == "__main__":
    #test the function
    image = np.array([[255, 255, 255], [255, 255, 255], [255, 255, 255]], dtype=np.uint8)
    weather_change_mat = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]], dtype=np.uint8)
    result = weather_change_mat_sub(image, weather_change_mat)
    print("Original Image:\n", image)
    print("Weather Change Matrix:\n", weather_change_mat)
    print("Resulting Image:\n", result)