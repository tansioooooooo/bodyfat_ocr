from pytesseract import pytesseract
from PIL import Image
from PIL import ImageEnhance
import os

if __name__ == '__main__':
    mag = 1
    contrast = 1
    brightness = 1
    sharpness = 1

    for imgid in range(1, 4):
        img = Image.open(os.path.dirname(os.path.abspath(__file__)) +"/sample/sample" + str(imgid) + ".png", "r")

        # インストールしたtesseractコマンドのパス
        pytesseract.tesseract_cmd = "/usr/bin/tesseract"

        # 画像サイズ変更
        # img = img.resize(size=(int(img.width * mag), int(img.height * mag)), resample=Image.LANCZOS)

        # 彩度変更
        # contrast = ImageEnhance.Brightness(img)
        # img = contrast.enhance(brightness)

        # シャープネス変更
        # contrast = ImageEnhance.Sharpness(img)
        # img = contrast.enhance(sharpness)


        result = pytesseract.image_to_string(img, config="--psm 3", lang="eng")

        img.save(os.path.dirname(os.path.abspath(__file__)) + "/result/sample" + str(imgid) + ".png")
        s_result = result.split()

        threshold = s_result[7].split('~')
        min = threshold[0]
        max = threshold[1]
        
        s_result.append(s_result[8])
        s_result[7] = min
        s_result[8] = max

        print(s_result)

