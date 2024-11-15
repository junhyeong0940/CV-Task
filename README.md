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

# Panorama 영상 어플리케이션

## 개발 목적
Panorama는 카메라를 통해 여러 장의 이미지를 수집하고 이를 자동으로 합성하여 파노라마 영상을 만드는 어플리케이션입니다. 사용자는 이미지를 수집하고, 이를 합성하여 하나의 파노라마 영상으로 만들 수 있습니다.

## 구체적 구현 내용
1. **영상 수집**: 카메라에서 여러 장의 이미지를 수집하여 파노라마 영상 제작에 사용합니다.
    ```python 
    ret, frame = self.cap.read()  # 카메라에서 프레임 읽기
    ```
2. **영상 보기**: 수집된 이미지를 화면에 표시합니다.
    ```python
    stack = np.hstack((stack, cv2.resize(self.imgs[i], dsize=(0, 0), fx=0.25, fy=0.25)))  # 이미지 수평 결합
    ```
3. **파노라마 봉합**: 수집된 이미지를 합성하여 하나의 파노라마 영상을 생성합니다.
    ```python
    status, self.img_stitched = stitcher.stitch(self.imgs)  # 이미지 봉합
    ```
4. **파일 저장**: 생성된 파노라마 이미지를 파일로 저장할 수 있습니다.
    ``` python
    cv2.imwrite(fname, self.img_stitched)  # 합성된 이미지를 파일로 저장
    ```
5. **프로그램 종료**: 어플리케이션을 종료할 수 있는 기능을 제공합니다.
    ```python
    self.cap.release()  # 카메라 해제
    ```
## 사용법
1. **영상 수집**:
   - "영상 수집" 버튼을 클릭하여 카메라로 이미지를 수집합니다.
   - 'c' 키를 눌러 이미지를 저장하고, 'q' 키를 눌러 영상 수집을 종료합니다.
   - 최소 2장의 이미지를 수집해야 합니다.
   
2. **영상 보기**:
   - "영상 보기" 버튼을 클릭하여 수집된 이미지를 화면에 나열하여 확인할 수 있습니다.

3. **파노라마 봉합**:
   - "봉합" 버튼을 클릭하여 수집된 이미지를 하나의 파노라마 영상으로 합성합니다.
   - 봉합이 성공하면 파노라마 영상을 화면에 표시합니다.

4. **파일 저장**:
   - "저장" 버튼을 클릭하여 봉합된 파노라마 이미지를 파일로 저장할 수 있습니다.
   - 파일 형식으로 JPG, PNG, BMP를 선택할 수 있습니다.

5. **프로그램 종료**:
   - "나가기" 버튼을 클릭하여 어플리케이션을 종료합니다.

## 개발 환경
- **Python**: 3.10
- **필요한 라이브러리**:
    - OpenCV =2.1.3
    - opencv-python = 4.10.0.84
    - Numpy = 2.1.3 
    - PyQt6 = 6.7.1
    - pyinstaller = 6.11.0
## 설치 및 실행 방법

### 1. 가상환경 생성 및 활성화
```bash
# 가상환경 생성
python -m venv ./.venv
# 가상환경 활성화 (Windows)
.venv\Scripts\Activate.ps1
