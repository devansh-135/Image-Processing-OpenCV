import cv2
import os

# Create output folder
if not os.path.exists("output"):
    os.makedirs("output")

# Load image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Edge Detection
edges = cv2.Canny(blur, 50, 150)

# Save outputs
cv2.imwrite("output/gray.jpg", gray)
cv2.imwrite("output/blur.jpg", blur)
cv2.imwrite("output/edges.jpg", edges)

# Show images
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()