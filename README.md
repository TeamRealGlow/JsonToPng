# face-parsing을 위한 데이터셋 제작기
##### 디렉터리 내의 png를 제외한 사진 파일을 jpg로 변환 및 json파일을 컬러맵으로 변환해 png 파일로 저장해주는 프로그램

디렉터리 구조
```
jsonToPng
├─ app.py
├─ json_to_png.py 
├─ make_jpg.py
└─ testsave
```
requirements.txt
```commandline
opencv-python
glob2
```


실행법

Window
```
python app.py imagedir saverdir
```
Linux
```
$ python3 app.py testimg testsave
```
ex
```
python app.py testimg testsave
```

```
$ python3 app.py testimg testsave
```

컬러맵 참조
```commandline
colormap = {
"skin" : (255, 0, 0),
"eye" : (255, 0, 255),
"brow" : (51, 255, 255),
"lip" : (255, 255, 0),
"mouth" : (0, 255, 0),
"nose" : (0, 153, 0),
"hair" : (60, 0, 255),
"ear" : (255, 204, 204)
}
```