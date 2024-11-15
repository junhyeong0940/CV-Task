# 24-2 컴퓨터 비전 과제

# 1. Panorama 영상 어플리케이션

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
#어플리케이션 실행
python vision_agent\Panorama.py
```

## 2. SpecialEffect 사진 특수 효과 어플리케이션

## 개발 목적
SpecialEffect는 사용자가 사진을 선택한 후, 다양한 필터 효과를 적용할 수 있는 어플리케이션입니다. 엠보싱, 카툰, 연필 스케치, 유화 등의 효과를 제공하여 사용자에게 창의적인 사진 편집 기능을 제공합니다.

## 구체적 구현 내용
- **사진 읽기:** 사용자가 원하는 사진 파일을 선택하고 불러옵니다.
  ```python
  self.img = cv2.imread(fname[0])  # 이미지 파일 읽기
  ```
- **엠보싱 효과** 사진에 엠보싱 필터를 적용하여 사진을 독특한 질감으로 변환합니다.
    ```python
    self.emboss = np.uint8(np.clip(cv2.filter2D(gray16, -1, femboss) + 128, 0, 255))  # 엠보싱 필터
    ```
- **카툰 효과** 사진을 카툰 스타일로 변환하여 독특한 분위기를 연출합니다.
    ```python
       self.cartoon = cv2.stylization(self.img, sigma_s=60, sigma_r=0.45)  # 카툰 효과
    ```    
- **유화 효과**
    ```python
   self.oil = cv2.xphoto.oilPainting(self.img, 10, 1, cv2.COLOR_BGR2Lab)  # 유화 효과
    ```
- **파일 저장**
    ```python
    cv2.imwrite(fname[0], self.cartoon)  # 사진 저장
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
pip install opencv-python = 2.1.3
pip install numpy = 2.1.3 
pip install PyQt6 = 6.7.1
pip install pyinstaller = 6.11.0
#어플리케이션 실행
python vision_agent\SpecialEffect.py
```
