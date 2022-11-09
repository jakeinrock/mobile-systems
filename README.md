# mobile-systems
Mobile systems project.

### Datasets for OCR 

If we want to focus on OCR results (to say that we have 
correct text at output), we could use one of these datasets:

- https://www.kaggle.com/datasets/sthabile/noisy-and-rotated-scanned-documents
- https://www.kaggle.com/datasets/urbikn/sroie-datasetv2

They both contain not only images but also expected OCR result (text/rotation angle etc.)

If we do not want to focus on OCR results, it should be sufficient:

- https://github.com/clovaai/cord

It contains JSON files with not really expected results (categorized).

### Resources monitoring

In Android Studio, we have a special API as HardwarePropertiesManager class: 
https://developer.android.com/reference/android/os/HardwarePropertiesManager

In Python, most solutions are based on psutil library or receiving data from logs 
located on mobile phone. Libraries are not connected with Android App technology.

- Kivy example: https://kanishkanamdeo.medium.com/writing-a-simple-kivy-based-cpu-monitoring-app-in-python-74e1a7e872


