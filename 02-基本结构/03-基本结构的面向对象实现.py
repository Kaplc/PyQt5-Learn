"""
1) 优势方便维护将控件分组, 需要的时候导入调用

"""
from PyQt5.Qt import *


# 自定义类继承QWindow
class Window(QWidget):

    # 初始化
    def __init__(self):
        # 调用父类的__init__完成初始化
        super().__init__()

        # 自己定义的要初始化的代码
        self.setWindowTitle('类创建窗口')
        self.resize(500, 500)

        # 初始化执行的方法
        self.setup_ui()

    def setup_ui(self):
        # 填入self继承继承自己显示在父窗口内
        label = QLabel(self)
        label.setText('通过init调用此方法成功')


import sys

app = QApplication(sys.argv)

# 创建自定义类实例
w = Window()
# 使用show()
w.show()

sys.exit(app.exec_())
