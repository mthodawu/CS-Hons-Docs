import cv2

# Load images
img1 = cv2.imread("images/road.jpg")
img2 = cv2.imread("images/car2.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Denoise and filter image
img2_gray = cv2.bilateralFilter(img2_gray, 25, 45, 45)

# Thresholding
ret, mask = cv2.threshold(img2_gray, 242, 255, cv2.THRESH_BINARY)
cv2.imshow('mask', mask)
cv2.waitKey(0)

# Create the inverse mask
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Inv_mask', mask_inv)
cv2.waitKey(0)

# Masking using bitwise_and
car_masked = cv2.bitwise_and(img2, img2, mask=mask)
car_masked_on_black = cv2.bitwise_and(img2, img2, mask=mask_inv)

# Display car image with mask
cv2.imshow('Car Masked', car_masked)
cv2.imshow('Car on Black', car_masked_on_black)
cv2.waitKey(0)

# Add the cut out road image to the cropped car
result = cv2.bitwise_and(img1, img1, mask=mask) + car_masked_on_black

# Display images
cv2.imshow('Road and Car Added', result)
cv2.waitKey(0)
cv2.destroyAllWindows()