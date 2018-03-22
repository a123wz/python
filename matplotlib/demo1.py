import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

#plt.figure定义一个图像窗口：编号为3；大小为(8, 5)
plt.figure(num=1, figsize=(8, 5),)
#画线 曲线的颜色属性(color)为红色;曲线的宽度(linewidth)为1.0；
#曲线的类型(linestyle)为虚线
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
#plt.show()

#使用plt.xlim设置x坐标轴范围：(-1, 2)； 
#使用plt.ylim设置y坐标轴范围：(-2, 3)； 
#使用plt.xlabel设置x坐标轴名称：’I am x’； 
#使用plt.ylabel设置y坐标轴名称：’I am y’；
print("plt.show")
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
#使用plt.yticks设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；
#对应刻度的名称为[‘really bad’,’bad’,’normal’,’good’, ‘really good’]
new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
new_ticks = [-2, -1.8, -1, 1.22, 3];
plt.yticks(new_ticks,[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
# 使用plt.gca获取当前坐标轴信息. 使用.spines设置边框：右侧边框；使用.set_color设置边框颜色：默认白色； 使用.spines设置边框：上边框；
# 使用.set_color设置边框颜色：默认白色；
ax = plt.gca()
ax.spines['right'].set_color('red')
ax.spines['top'].set_color('none')

#使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：bottom.（所有位置：top，bottom，both，default，none）
ax.xaxis.set_ticks_position('bottom')

#使用.spines设置边框：x轴；使用.set_position设置边框位置：y=0的位置；（位置所有属性：outward，axes，data）
ax.spines['bottom'].set_position(('data', 0))


plt.show()
