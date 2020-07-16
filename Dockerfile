# 1. python3のlatestのDocker imageをベースに、
FROM python:latest

# 2. tesseractと依存ライブラリをaptでインストールして、
RUN apt-get update
RUN apt-get -y install \
    tesseract-ocr \
    tesseract-ocr-jpn
RUN apt-get clean

# 3. 必要なpythonライブラリをpipでインストール
RUN pip install --upgrade pip; \
    pip install \
    pillow \
    pytesseract \
    pyocr

ENTRYPOINT ["/usr/bin/tail", "-f", "/dev/null"]