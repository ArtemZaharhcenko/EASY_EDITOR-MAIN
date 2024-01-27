from PyQt5.QtWidgets import (QApplication, QWidget, QListWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog)
import os
from imageProcessor import ImageProcessor


app = QApplication([])
window = QWidget()
window.setWindowTitle("Easy editior")
window.resize(600, 600)

main_line = QHBoxLayout()

line1 = QVBoxLayout()
btn_folder = QPushButton("folder")
list_widget = QListWidget()

line1.addWidget(btn_folder)
line1.addWidget(list_widget)

main_line.addLayout(line1, stretch=1)

line2 = QVBoxLayout()
image  =QLabel("image")

button_line = QHBoxLayout()
btn1 = QPushButton("B/W ")
btn2 = QPushButton("Left")
btn3 = QPushButton("mirror")
btn4 = QPushButton("Blur")
btn5 = QPushButton("sharp")
button_line.addWidget(btn1)
button_line.addWidget(btn2)
button_line.addWidget(btn3)
button_line.addWidget(btn4)
button_line.addWidget(btn5)

line2.addWidget(image)
line2.addLayout(button_line)

main_line.addLayout(line2, stretch=2)

window.setLayout(main_line)


def filter (files):
    img_files = []
    filters = ["png", "jpg", "jpeg", "gid"]
    
    for file in files:
        if file.split(".")[-1] == "png":
            img_files.append(file)

    return img_files        

workdir = ''
def showFolder():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    filenames = filter(os.listdir(workdir))

    list_widget.addItems(filenames)

btn_folder.clicked.connect(showFolder)

workImage = ImageProcessor(image)

def showChosenItem():
    filename = list_widget.currentItem().text()
    workImage.loadImage(filename, workdir)
    workImage.showImage(os.path.join(workdir, filename))

list_widget.currentRowChanged.connect(showChosenItem)

btn1.clicked.connect(workImage.do_bw)
btn2.clicked.connect(workImage.left)
btn3.clicked.connect(workImage.mirror)
btn4.clicked.connect(workImage.blur)
btn5.clicked.connect(workImage.sharp)

window.show()

app.exec_()