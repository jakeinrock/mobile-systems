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

NOTE: psutil does probably not work on Android! It is not supported on this system (or if I understood correctly - arm64 architecture).

Alternative solution  - reading from /proc/stat, can be done in python with inline shell scripting but `sudo` is required.
Probably impossible to implement without rooting phone.

### Building kivy app with buildozer

##### Ready Google Colab way

Following this article (https://towardsdatascience.com/3-ways-to-convert-python-app-into-apk-77f4c9cd55af) and 
its second method, you can simply create apk using Google Colab. Just put .py and/or .kv files to colab file manager
and run prepared commands. If some libraries are missing, just try to add code for installing them. Also this tutorial
(https://www.youtube.com/watch?v=GTkKul8sA-c) can be helpful.

##### On local environment

Setting everything up on local environment by downloading all required dependencies (libraries and python packages) and
then installing buildozer. An example of complex instruction is presented in this tutorial 
(https://www.youtube.com/watch?v=EupAeyL8zAo). Tutorial contains a way of downloading repository with buildozer setup, 
but sometimes it doesn't work, that's why entering some commands from earlier mentioned Colab is not a bad way. 
When having some troubles, check following command history:

```bash
 1927  sudo pip install buildozer
 1928  sudo pip install cython==0.29.19
 1929  sudo apt-get install -y     python3-pip     build-essential     git     python3     python3-dev     ffmpeg     libsdl2-dev     libsdl2-image-dev     libsdl2-mixer-dev     libsdl2-ttf-dev     libportmidi-dev     libswscale-dev     libavformat-dev     libavcodec-dev     zlib1g-dev
 1930  sudo apt-get install -y     libgstreamer1.0     gstreamer1.0-plugins-base     gstreamer1.0-plugins-good
 1931  sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6
 1933  sudo apt-get update
 1934  sudo apt-get install libffi6
 1935  sudo apt-get install libffi-dev
 1936  cd ..
 1937  cd Pycharms*
 1938  cd Py*
 1939  ls
 1940  cd mobil*
 1941  ls
 1942  buildozer init
 1943  sudo apt-get install libsdl2-dev
 1944  sudo apt-cache search libsdl
 1945  sudo apt-get update -y
 1946  sudo apt-get install -y libsdl2-dev
 1947  sudo apt-get install -y     libgstreamer1.0     gstreamer1.0-plugins-base     gstreamer1.0-plugins-good apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6
 1948  sudo apt-get install build-essential libsqlite3-dev sqlite3 bzip2 libbz2-dev zlib1g-dev libssl-dev openssl libgdbm-dev libgdbm-compat-dev liblzma-dev libreadline-dev libncursesw5-dev libffi-dev uuid-dev libffi6
 1949  sudo apt-get install libffi-dev
 1950  buildozer init
 1951  buildozer -v android debug deploy run
```

If some problems won't be solved by above commands, there are two more
advices:
- change python version to the older one (remember about reinstalling previously installed packages),
- updating and upgrading apt-get, checking archive availability (sometimes resetting /etc/apt/sources.list will be required),
- manually downloading some archives.
