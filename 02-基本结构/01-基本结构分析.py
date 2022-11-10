"""
基本结构:

窗口实例
   ↓


"""

# 导包
# PyQt5.Qt里面集合了常用的方法方便调用
from PyQt5.Qt import *
import sys

# 创建实例对象
# sys.argv: 接收命令行启动是输入的参数
print(sys.argv)
app = QApplication(sys.argv)


# 再创建窗口实例
window = QWidget()
# 设置标题
window.setWindowTitle('窗口标题')
# 设置样式
window.resize(500, 500)
window.move(400, 200)

# 创建标签实例, 并继承父窗口window, 显示在父窗口内
# 不继承会单独创建新窗口
label = QLabel(window)
label.setText('标签文本')
label.move(200, 200)

# 窗口实例不会自动显示需要调用
window.show()


# sys.exit: 接收退出码检测是否正常退出
# app.exec_(): 返回相应退出码
sys.exit(app.exec_())



