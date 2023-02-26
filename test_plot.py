import numpy as np
import matplotlib.pyplot as plt

# 创建子图
fig, axs = plt.subplots(nrows=4, figsize=(8, 6))

# 绘制子图
x = np.linspace(0, 2*np.pi, 100)
axs[0].plot(x, np.sin(x))
axs[1].plot(x, np.cos(x))
axs[2].plot(x, np.tan(x))
axs[3].plot(x, np.exp(x))

# 添加标题
axs[0].set_title('Sine function')
axs[1].set_title('Cosine function')
axs[2].set_title('Tangent function')
axs[3].set_title('Exponential function')

# 设置 x 轴和 y 轴标签
fig.text(0.5, 0.04, 'X axis', ha='center')
fig.text(0.04, 0.5, 'Y axis', va='center', rotation='vertical')

plt.tight_layout()
plt.show()
