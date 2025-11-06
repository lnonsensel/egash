import cv2

def put_text(img, text, color, scale, thickness):
    text = text
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontColor = color
    fontScale = scale
    thickness = thickness

    text_size, baseline = cv2.getTextSize(text, fontFace, fontScale, thickness)
    text_width, text_height = text_size

    img_height, img_width, _ = img.shape
    center_x = int((img_width - text_width) / 2)
    center_y = int((img_height + text_height) / 2) - baseline 
    text_origin = (center_x, center_y)

    cv2.putText(img, text, text_origin, fontFace, fontScale, fontColor, thickness)


