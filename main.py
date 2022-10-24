# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import random
from opts import *
from flask_cors import CORS
from flask import Flask, render_template, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False  # 返回中文
CORS(app, resources=r'/*')

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["1000 per day", "60 per minute"]
)

@app.route("/")
@limiter.limit("0.1/second", override_defaults=False)
def eat_what():
    hm = random_how_much()
    dict = {}
    dict["data"] = hm
    return jsonify(dict)

@app.route("/eatwhat")
def eat_html():
    return render_template("index.html")

def random_floor():
    floor = random.randint(1, 25)
    if floor < 16:
        floor = 1
        windows, food  = random_f_win1()
    else:
        floor = 2
        windows, food = random_f_win2()
    return str(floor) + '层' + str(windows) + '窗口\n' + food

def random_f_win1():
    ra = random.sample(list(floor1), 1)
    key = ra[0]
    values = floor1[key]
    value = getsomeone(values)
    return key, value

def random_f_win2():
    ra = random.sample(list(floor2), 1)
    key = ra[0]
    values = floor2[key]
    value = getsomeone(values)
    return key, value

def random_drink():
    x = random.randint(1, 100)
    js = {
        1: "矿泉水",  # 套餐1
        2: "维它",  # 套餐2
        3: "可乐",  # 套餐3
    }
    if x <= 60:
        return js[1]
    elif x < 90 and x > 60:
        return js[2]
    else:
        return js[3]

def random_how_much():
    js = {
        1: "",   # 套餐1
        2: "",  # 套餐2
        3: "",  # 套餐3
        4: "外卖",  # 套餐4
        5: "聚餐",  # 套餐5
    }
    floor = random_floor()
    x = random.randint(1, 33)
    if x < 30:
        drink = random_drink()
        tc = js[int(x/10) + 1]
        return floor + "\n" + tc + "\n" + drink
    elif x >=30 and x <=32:
        tc = js[4]
        return tc
    else:
        tc = js[5]
        return tc

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="5000",debug=False)
