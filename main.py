# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import random
import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route("/")
def eat_what():
    hm = random_how_much()
    return hm

def random_floor():
    floor = random.randint(1, 2) #在那层楼吃
    r = random.randint(1, 36)
    windows = 1
    if r < 24+1:
        windows = random_f_win1()
    else:
        windows = random_f_win2()
    return str(floor) + '层' + str(windows) + '窗口'

def random_f_win1():
    return random.randint(1, 24)

def random_f_win2():
    return random.randint(1, 12)

# 正态分布 (防止太多次吃到太便宜/太贵的食物)
def gaussian_distribution():
    result = np.random.uniform(100, 400, (1))[0]
    result = round(result/100) if result > 370 else int(result/100)
    return result

def random_how_much():
    js = {
        1 : "5块5 ~ 8块",   # 套餐1
        2: "8块5 ~ 12块5",  # 套餐2
        3: "13块 ~ 16块5",  # 套餐3
        4: "17块 ~ 20块",  # 套餐4
    }
    floor = random_floor()
    x = gaussian_distribution()
    tc = js[x]
    return floor + "   " + tc

if __name__ == '__main__':
    app.run(debug=False)
