import easyocr
import sys

sys.stdout.reconfigure(encoding='utf-8')

def perform_ocr(image_path):

    # specify languages and other configs
    reader = easyocr.Reader(['en'], gpu=False)

    # provide image url instead of path
    result = reader.readtext(image_path, detail=0)

    return result
