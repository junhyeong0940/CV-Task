# 24-2 컴퓨터 비전 과제
## 1. TrafficWeak - 교통약자 보호 어플리케이션

## 개발 목적
TrafficWeak는 교통약자를 보호하기 위한 어플리케이션입니다. 이 프로그램은 교통 표지판을 등록하고, 도로 영상을 불러와 표지판을 인식하여 운전자가 주의해야 할 사항을 알립니다.

## 구체적 구현 내용
- **표지판 등록:** 어린이, 노인, 장애인 표지판 모델을 등록합니다. 예를 들어, 표지판 이미지 파일을 불러와 저장하는 코드는 다음과 같습니다.
  ```python
  self.signFiles = [['vision_agent\\.venv\\child.png', '어린이'], ['vision_agent\\.venv\\elder.png', '노인'], ['vision_agent\\.venv\\disabled.png', '장애인']]
  ```
- **도로 영상 불러오기**
    ```python
    fname = QFileDialog.getOpenFileName(self, '파일 읽기', './')
    ```
- **표지판 인식**
    ```python
        sift = cv.SIFT_create() 

        KD = []  
        for img in self.signImgs:
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
            KD.append(sift.detectAndCompute(gray, None))  
    
        grayRoad = cv.cvtColor(self.roadImg, cv.COLOR_BGR2GRAY)  
        road_kp, road_des = sift.detectAndCompute(grayRoad, None)  
    ```    
- **결과 표시**
    ```python
    self.label.setText(self.signFiles[best][1] + ' 보호구역입니다. 30km로 서행하세요.')
    ```

## 개발 환경
- **python 3.10**
- **필요한 라이브러리**
    -OpenCV
    -Numpy
    -PyQt6

## 터미널 명령어
다음 명령어를 사용하여 개발 환경을 설정하고 어플리케이션을 실행할 수 있습니다.
```bash
# 가상환경 생성
python -m venv ./.venv
# 가상환경 활성화
.venv\Scripts\Activate.ps1
#필요한 라이브러리 설치
pip install opencv-python
pip install numpy
pip install PyQt6

#어플리케이션 실행
python vision_agent\TrafficWeak.py
```

## 2. SpecialEffect - 이미지 특수효과 적용 어플리케이션

## 개발 목적
SpecialEffect는 사용자가 이미지를 불러와 다양한 필터(엠보싱, 카툰, 연필 스케치, 유화)를 적용할 수 있는 프로그램입니다.적용한 필터 결과를 저장하여 활용할 수 있습니다.

## 구체적 구현 내용
- **사진 불러오기:** 로컬 파일에서 이미지를 선택하여 불러오는 기능입니다.
    ```python
    fname = QFileDialog.getOpenFileName(self, '사진 읽기', './')
self.img = cv.imread(fname[0])
if self.img is None:
    sys.exit('파일을 찾을 수 없습니다.')
    ```
- **엠보싱 필터:** 이미지에 엠보싱 효과를 적용하여 입체감을 부여하는 기능입니다.
    ```python 
    femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
    ```
- **카툰 필터:** 이미지를 카툰 스타일로 변환합니다.
    ```python
    self.cartoon = cv.stylization(self.img, sigma_s=60, sigma_r=0.45)
    ```
- **연필 스케치 필터:** 이미지를 연필로 그린 듯한 흑백 및 컬러 스케치 효과로 변환합니다.
    ```python
    self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
    ```
- **유화 필터:** 이미지를 유화 그림처럼 변환하는 기능입니다.
    ```python 
    self.oil = cv.xphoto.oilPainting(self.img, 10, 1, cv.COLOR_BGR2Lab)
    ```
- **이미지 저장:** 사용자가 선택한 필터로 변환한 이미지를 원하는 파일 이름과 경로에 저장할 수 있습니다.
    ```python 
    fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
    cv.imwrite(fname[0], self.emboss)
    ```

## 개발 환경
- **python 3.10**
- **필요한 라이브러리**
    -OpenCV
    -Numpy
    -PyQt6

## 터미널 명령어
다음 명령어를 사용하여 개발 환경을 설정하고 어플리케이션을 실행할 수 있습니다.
```bash
# 가상환경 생성
python -m venv ./.venv
# 가상환경 활성화
.venv\Scripts\Activate.ps1
#필요한 라이브러리 설치
pip install opencv-python
pip install numpy
pip install PyQt6
pip install opencv-contrib-python

#어플리케이션 실행
python vision_agent\SpecialEffect.py
