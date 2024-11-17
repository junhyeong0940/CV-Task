import os
import sys
import numpy as np
import cv2
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QComboBox,
    QFileDialog, QMessageBox
)


class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("사진 특수 효과")
        self.setGeometry(200, 200, 800, 200)

        # 버튼 생성
        pictureButton = QPushButton("사진 읽기", self)
        embossButton = QPushButton("엠보싱", self)
        cartoonButton = QPushButton("카툰", self)
        sketchButton = QPushButton("연필 스케치", self)
        oilButton = QPushButton("유화", self)
        saveButton = QPushButton("저장하기", self)
        quitButton = QPushButton("나가기", self)

        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(["엠보싱", "카툰", "연필 스케치(명암)", "연필 스케치(컬러)", "유화"])

        self.label = QLabel("환영합니다!", self)

        # 버튼 위치 설정
        pictureButton.setGeometry(10, 10, 100, 30)
        embossButton.setGeometry(110, 10, 100, 30)
        cartoonButton.setGeometry(210, 10, 100, 30)
        sketchButton.setGeometry(310, 10, 100, 30)
        oilButton.setGeometry(410, 10, 100, 30)
        saveButton.setGeometry(510, 10, 100, 30)
        quitButton.setGeometry(620, 10, 100, 30)
        self.pickCombo.setGeometry(510, 40, 110, 30)
        self.label.setGeometry(10, 40, 500, 170)

        # 버튼 이벤트 연결
        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction)
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchButton.clicked.connect(self.sketchFunction)
        oilButton.clicked.connect(self.oilFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

    def pictureOpenFunction(self):
        # 파일 선택
        fname = QFileDialog.getOpenFileName(self, "사진 읽기", "./", "Images (*.png *.jpg *.jpeg *.bmp)")
        if not fname[0]:  # 파일이 선택되지 않았을 경우
            QMessageBox.warning(self, "경고", "파일이 선택되지 않았습니다!")
            return

        # 경로 확인
        print("선택된 파일 경로:", fname[0])

        # 한글 경로 처리
        try:
            file_path = os.path.abspath(fname[0])
            self.img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
            if self.img is None:
                QMessageBox.critical(self, "오류", "이미지를 불러오지 못했습니다! 유효한 파일인지 확인하세요.")
                return

            # 이미지 출력
            cv2.imshow("Painting", self.img)
        except Exception as e:
            QMessageBox.critical(self, "오류", f"파일을 처리하는 중 오류가 발생했습니다: {str(e)}")

    def embossFunction(self):
        if not hasattr(self, 'img'):
            QMessageBox.warning(self, "경고", "이미지를 먼저 열어주세요!")
            return

        # 엠보싱 필터 적용
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv2.filter2D(gray16, -1, femboss) + 128, 0, 255))
        cv2.imshow("Emboss", self.emboss)

    def cartoonFunction(self):
        if not hasattr(self, 'img'):
            QMessageBox.warning(self, "경고", "이미지를 먼저 열어주세요!")
            return

        # 카툰 효과 적용
        self.cartoon = cv2.stylization(self.img, sigma_s=60, sigma_r=0.45)
        cv2.imshow("Cartoon", self.cartoon)

    def sketchFunction(self):
        if not hasattr(self, 'img'):
            QMessageBox.warning(self, "경고", "이미지를 먼저 열어주세요!")
            return

        # 연필 스케치 효과 적용
        self.sketch_gray, self.sketch_color = cv2.pencilSketch(
            self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02
        )
        cv2.imshow("Pencil sketch(gray)", self.sketch_gray)
        cv2.imshow("Pencil sketch(color)", self.sketch_color)

    def oilFunction(self):
        if not hasattr(self, 'img'):
            QMessageBox.warning(self, "경고", "이미지를 먼저 열어주세요!")
            return

        # 유화 효과 적용
        self.oil = cv2.xphoto.oilPainting(self.img, 10, 1, cv2.COLOR_BGR2Lab)
        cv2.imshow("Oil painting", self.oil)

    def saveFunction(self):
        if not hasattr(self, 'img'):
            QMessageBox.warning(self, "경고", "이미지를 먼저 열어주세요!")
            return

        # 파일 저장
        fname = QFileDialog.getSaveFileName(self, "파일 저장", "./", "Images (*.png *.jpg *.jpeg *.bmp)")
        if not fname[0]:  # 저장 경로가 선택되지 않았을 경우
            QMessageBox.warning(self, "경고", "저장 경로가 선택되지 않았습니다!")
            return

        # 현재 선택된 효과 저장
        i = self.pickCombo.currentIndex()
        if i == 0 and hasattr(self, 'emboss'):
            cv2.imwrite(fname[0], self.emboss)
        elif i == 1 and hasattr(self, 'cartoon'):
            cv2.imwrite(fname[0], self.cartoon)
        elif i == 2 and hasattr(self, 'sketch_gray'):
            cv2.imwrite(fname[0], self.sketch_gray)
        elif i == 3 and hasattr(self, 'sketch_color'):
            cv2.imwrite(fname[0], self.sketch_color)
        elif i == 4 and hasattr(self, 'oil'):
            cv2.imwrite(fname[0], self.oil)
        else:
            QMessageBox.warning(self, "경고", "해당 효과가 적용되지 않았습니다!")

    def quitFunction(self):
        cv2.destroyAllWindows()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SpecialEffect()
    win.show()
    app.exec()
