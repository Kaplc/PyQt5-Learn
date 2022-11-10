"""
1) 设置-编辑器-实时模板

2)
    $自定义名字$定义写代码的位置, 导入后光标自动移动到该位置


"""

# 输入qtt一键生成
# ----------------------------------------
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
# 设置窗口标题
window.setWindowTitle('标题')
# 设置样式
window.resize(500, 500)




# 窗口实例不会自动显示需要调用
window.show()
# sys.exit: 接收退出码检测是否正常退出
# app.exec_(): 返回相应退出码
sys.exit(app.exec_())
