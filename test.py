import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("텍스트에디트 + 버튼 예제")
        self.setGeometry(200, 200, 400, 300)  # 창 위치와 크기 설정

        # 메인 레이아웃 (수직)
        main_layout = QVBoxLayout()

        # 텍스트 에디트 (창 크기에 맞게 확장됨)
        self.text_edit = QTextEdit(self)
        main_layout.addWidget(self.text_edit)

        # 버튼들을 담을 레이아웃 (수평)
        button_layout = QHBoxLayout()

        # 메시지 버튼
        self.message_button = QPushButton("메시지 버튼", self)
        self.message_button.clicked.connect(self.on_button_click)
        button_layout.addWidget(self.message_button)

        # Clear 버튼
        self.clear_button = QPushButton("Clear", self)
        self.clear_button.clicked.connect(self.on_clear_button_click)
        button_layout.addWidget(self.clear_button)

        main_layout.addLayout(button_layout) # 버튼 레이아웃을 메인 레이아웃에 추가
        self.setLayout(main_layout)

    def on_button_click(self):
        # 버튼 클릭 시 "Button Clicked" 문구를 텍스트에디트에 추가
        self.text_edit.append("Button Clicked")

    def on_clear_button_click(self):
        # Clear 버튼 클릭 시 텍스트 에디터 내용 모두 지우기
        self.text_edit.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())