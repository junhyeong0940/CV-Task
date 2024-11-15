import cv2 as cv
import numpy as np
from PyQt6.QtWidgets import *
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사진 특수 효과')
        self.setGeometry(200, 200, 800, 200)

        pictureButton = QPushButton('사진 읽기', self)
        embossButton = QPushButton('엠보싱', self)
        cartoonButton = QPushButton('카툰', self)
        sketchButton = QPushButton('연필 스케치', self)
        oilButton = QPushButton('유화', self)
        saveButton = QPushButton('저장하기', self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['엠보싱', '카툰', '연필 스케치(명암)', '연필 스케치(컬러)', '유화'])
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다!', self)

        pictureButton.setGeometry(10, 10, 100, 30)
        embossButton.setGeometry(110, 10, 100, 30)
        cartoonButton.setGeometry(210, 10, 100, 30)
        sketchButton.setGeometry(310, 10, 100, 30)
        oilButton.setGeometry(410, 10, 100, 30)
        saveButton.setGeometry(510, 10, 100, 30)
        self.pickCombo.setGeometry(510, 40, 110, 30)
        quitButton.setGeometry(620, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 170)

        pictureButton.clicked.connect(self.pictureOpenFunction)
        embossButton.clicked.connect(self.embossFunction)
        cartoonButton.clicked.connect(self.cartoonFunction)
        sketchButton.clicked.connect(self.sketchFunction)
        oilButton.clicked.connect(self.oilFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)

        self.img = None
        self.emboss = None
        self.cartoon = None
        self.sketch_gray = None
        self.sketch_color = None
        self.oil = None

    def pictureOpenFunction(self):
        fname = QFileDialog.getOpenFileName(self, '사진 읽기', './')
        self.img = cv.imread(fname[0])
        if self.img is None:
            sys.exit('파일을 찾을 수 없습니다.')

        cv.imshow('Painting', self.img)

    def embossFunction(self):
        femboss = np.array([[-1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
        gray = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)
        gray16 = np.int16(gray)
        self.emboss = np.uint8(np.clip(cv.filter2D(gray16, -1, femboss) + 128, 0, 255))
        cv.imshow('Emboss', self.emboss)

    def cartoonFunction(self):
        self.cartoon = cv.stylization(self.img, sigma_s=60, sigma_r=0.45)
        cv.imshow('Cartoon', self.cartoon)

    def sketchFunction(self):
        self.sketch_gray, self.sketch_color = cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
        cv.imshow('Pencil sketch (gray)', self.sketch_gray)
        cv.imshow('Pencil sketch (color)', self.sketch_color)

    def oilFunction(self):
        self.oil = cv.xphoto.oilPainting(self.img, 10, 1, cv.COLOR_BGR2Lab)
        cv.imshow('Oil painting', self.oil)

    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장', './')

        # 파일 이름이 제공되지 않은 경우
        if not fname[0]:  
            return

        # 확장자 확인 및 추가
        if not fname[0].lower().endswith(('.png', '.jpg', '.jpeg')):
            fname = (fname[0] + '.png',)

        i = self.pickCombo.currentIndex()
        if i == 0 and self.emboss is not None: 
            cv.imwrite(fname[0], self.emboss)
        elif i == 1 and self.cartoon is not None: 
            cv.imwrite(fname[0], self.cartoon)
        elif i == 2 and self.sketch_gray is not None: 
            cv.imwrite(fname[0], self.sketch_gray)
        elif i == 3 and self.sketch_color is not None: 
            cv.imwrite(fname[0], self.sketch_color)
        elif i == 4 and self.oil is not None: 
            cv.imwrite(fname[0], self.oil)
        else:
            QMessageBox.warning(self, '저장 오류', '선택한 효과가 없습니다.')


    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = SpecialEffect()
win.show()
app.exec()
