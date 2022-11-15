from flask import Flask, request, redirect
from ocr import perform_ocr
import json

app = Flask(__name__)


@app.route('/')
def home():
        return 'Hello OCR'

@app.route('/ocr', methods = ['POST'])
def ocr():
    if request.method == 'POST':
        image_path = request.get_json()["image_path"]

        try:
            ocr_result = perform_ocr(str(image_path))
            msg = f'Process finished succesfully!. OCR result: {ocr_result}'
            response = app.response_class(
                response=json.dumps(msg),
                status=200,
                mimetype='application/json'
            )

        except Exception as err:
            msg = f'An error occured" {err}'
            response = app.response_class(
                response=json.dumps(msg),
                status=400,
                mimetype='application/json'
            )

        finally:
            return response

    return redirect("http://localhost:5000", code=302)

if __name__ == '__main__':
    app.run()

