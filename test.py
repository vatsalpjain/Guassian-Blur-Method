import cv2

# Load the image
image = cv2.imread('original_image1.jpeg')

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Display the original and blurred images
cv2.imshow("Original", image)
cv2.imshow("Gaussian Blur", blurred_image)

# Save the blurred image
cv2.imwrite('blurred_image.jpg', blurred_image)

# Wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
