import cv2
import numpy as np

img = "images/watch.jpg"

image = cv2.imread(img, cv2.IMREAD_COLOR)


# To draw line: cv2.line(where_to_draw, (start_x, start_y), (end_x, end_y), (B, G, R), (optional_line_width))
cv2.line(image, (100, 200), (250, 250), (255, 255, 255), (15))

# To draw rectangle: cv2.rectangle(where_to_draw, (start_x, start_y), (end_x, end_y), (B, G, R), (optional_line_width or -1 to fill in))
cv2.rectangle(image, (200, 400), (250, 450), (255, 255, 255), (15))

# To draw Circle: cv2.circle(where_to_draw, (center_x, center_y), radius, (B, G, R), (optional_line_width or -1 to fill in))
cv2.circle(image, (300, 100), 100, (0, 255, 255), (-1))

# To draw Polygon: cv2.circle(where_to_draw, all_the_points, Complete and make it a full polygon or not,(B, G, R), (optional_line_width))
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
cv2.polylines(image, [pts], True, (255, 0, 255), 5)

# Write in image: cv2.rectangle(where_to_write, (start_x, start_y), font, size, (B, G, R), thickness, anti_aliasing)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(image, "Kapil's watch", (150, 350), font, 3.5, (0, 0, 255), 2, cv2.LINE_AA)


cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
