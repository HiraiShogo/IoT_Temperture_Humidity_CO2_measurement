from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta, date
import pickle
import numpy as np
import math
from matplotlib import pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def task():
    with app.app_context():
        now_time = datetime.now()
        print("task実行", now_time)
        if now_time.hour == 1:
            create()
        else:
            update()
def pic_create():
    temperature60 = []
    humidity60 = []
    co60 = []
    with open('data60.pickle', 'rb') as f:
        data60 = pickle.load(f)
    for i in range(len(data60)):
        temperature60.append(data60[i][0])
        humidity60.append(data60[i][1])
        co60.append(data60[i][2])
    temperature60 = [x for x in temperature60 if math.isnan(x) == False]
    humidity60 = [x for x in humidity60 if math.isnan(x) == False]
    co60 = [x for x in co60 if math.isnan(x) == False]


    # 1. 室温グラフ生成
    plt.figure(dpi=100, figsize=(13, 2), facecolor='#F0F0F0')
    plt.plot(temperature60, label="室温")
    plt.subplots_adjust(left=0.03, right=0.998, bottom=0.01)
    plt.title('温度', fontname="MS Gothic")

    # 凡例の表示
    plt.grid()
    plt.tick_params(labelbottom=False)
    plt.tick_params(direction='in')

    # プロット表示(設定の反映)
    plt.savefig('./static/images/temperture60.png')


    # 2. 湿度グラフ生成
    plt.figure(dpi=100, figsize=(13, 2), facecolor='#F0F0F0')
    plt.plot(humidity60, label="湿度")
    plt.subplots_adjust(left=0.03, right=0.998, bottom=0.01)
    plt.title('湿度', fontname="MS Gothic")

    # 凡例の表示
    plt.grid()
    plt.tick_params(labelbottom=False)
    plt.tick_params(direction='in')

    # プロット表示(設定の反映)
    plt.savefig('./static/images/humidity60.png')


    # 3. CO2グラフ生成
    plt.figure(dpi=100, figsize=(13, 2), facecolor='#F0F0F0')
    plt.plot(co60, label="CO2")
    plt.subplots_adjust(left=0.03, right=0.998, bottom=0.01)
    plt.title('CO2', fontname="MS Gothic")

    # 凡例の表示
    plt.grid()
    plt.tick_params(labelbottom=False)
    plt.tick_params(direction='in')

    # プロット表示(設定の反映)
    plt.savefig('./static/images/co60.png')

sched = BackgroundScheduler(daemon=True)
sched.add_job(task,'interval',minutes=60) 
sched.start()

app = Flask(__name__, static_folder='./static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    temperature1,temperature2,temperature3,temperature4,temperature5,temperature6,temperature7,temperature8,temperature9,temperature10,\
    temperature11,temperature12,temperature13,temperature14,temperature15,temperature16,temperature17,temperature18,temperature19,temperature20,\
    temperature21,temperature22,temperature23,temperature24=\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False)

    humidity1,humidity2,humidity3,humidity4,humidity5,humidity6,humidity7,humidity8,humidity9,humidity10,\
    humidity11,humidity12,humidity13,humidity14,humidity15,humidity16,humidity17,humidity18,humidity19,humidity20,\
    humidity21,humidity22,humidity23,humidity24=\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False)

    co1,co2,co3,co4,co5,co6,co7,co8,co9,co10,co11,co12,co13,co14,co15,co16,co17,co18,co19,co20,co21,co22,co23,co24=\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),\
    db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False),db.Column(db.String(5), nullable=False)

@app.route("/")
def index():
    # 変数定義
    target_date = date.today() - timedelta(days=3)
    temperature60 = []
    humidity60 = []
    co60 = []

    # 過去60分のデータ読み込み
    with open('data60.pickle', 'rb') as f:
        data60 = pickle.load(f)
    # データ並び替え
    for i in range(len(data60)):
        temperature60.append(data60[i][0])
        humidity60.append(data60[i][1])
        co60.append(data60[i][2])
    # データを視覚化
    pic_create()

    # SQL操作―３日前からの1時間データを取得
    posts = Post.query.filter(Post.date >= target_date)

    return render_template('index.html',posts = posts, temperature60=temperature60, humidity60=humidity60, co60=co60)


@app.route('/new')
def create():
    # GETメソッドの時の処理
    date_today = date.today()
    datetime_today = datetime.now()
    temperature60 = []
    humidity60 = []
    co60 = []
    with open('data60.pickle', 'rb') as f:
        data60 = pickle.load(f)
    for i in range(len(data60)):
        temperature60.append(data60[i][0])
        humidity60.append(data60[i][1])
        co60.append(data60[i][2])
    temperature60 = [x for x in temperature60 if math.isnan(x) == False]
    humidity60 = [x for x in humidity60 if math.isnan(x) == False]
    co60 = [x for x in co60 if math.isnan(x) == False]
    temperature1 = str(format(float(np.mean(temperature60)), '.2f'))
    humidity1 = str(format(float(np.mean(humidity60)), '.2f'))
    co1 = str(int(np.mean(co60)))
    temperature2=temperature3=temperature4=temperature5=temperature6=temperature7=temperature8=temperature9=temperature10=\
    temperature11=temperature12=temperature13=temperature14=temperature15=temperature16=temperature17=temperature18=temperature19=temperature20=\
    temperature21=temperature22=temperature23=temperature24="-"
    humidity2=humidity3=humidity4=humidity5=humidity6=humidity7=humidity8=humidity9=humidity10=\
    humidity11=humidity12=humidity13=humidity14=humidity15=humidity16=humidity17=humidity18=humidity19=humidity20=\
    humidity21=humidity22=humidity23=humidity24="-"
    co2=co3=co4=co5=co6=co7=co8=co9=co10=co11=co12=co13=co14=co15=co16=co17=co18=co19=co20=co21=co22=co23=co24="-"

    post = Post(date=date_today, datetime=datetime_today, temperature1=temperature1,temperature2=temperature2,temperature3=temperature3,temperature4=temperature4,temperature5=temperature5,\
                temperature6=temperature6,temperature7=temperature7,temperature8=temperature8,temperature9=temperature9,temperature10=temperature10,\
                temperature11=temperature11,temperature12=temperature12,temperature13=temperature13,temperature14=temperature14,temperature15=temperature15,\
                temperature16=temperature16,temperature17=temperature17,temperature18=temperature18,temperature19=temperature19,temperature20=temperature20,\
                temperature21=temperature21,temperature22=temperature22,temperature23=temperature23,temperature24=temperature24,\
                humidity1=humidity1, humidity2=humidity2, humidity3=humidity3, humidity4=humidity4, humidity5=humidity5,\
                humidity6=humidity6, humidity7=humidity7, humidity8=humidity8, humidity9=humidity9, humidity10=humidity10,\
                humidity11=humidity11,humidity12=humidity12,humidity13=humidity13,humidity14=humidity14,humidity15=humidity15,\
                humidity16=humidity16,humidity17=humidity17,humidity18=humidity18,humidity19=humidity19,humidity20=humidity20,\
                humidity21=humidity21,humidity22=humidity22,humidity23=humidity23,humidity24=humidity24,\
                co1=co1,co2=co2,co3=co3,co4=co4,co5=co5,co6=co6,co7=co7,co8=co8,co9=co9,co10=co10,\
                co11=co11,co12=co12,co13=co13,co14=co14,co15=co15,co16=co16,co17=co17,co18=co18,co19=co19,co20=co20,\
                co21=co21,co22=co22,co23=co23,co24=co24)
    # DBに値を送り保存する
    db.session.add(post)
    db.session.commit()
    return "1"


@app.route('/update')
def update():
    now_before30min = datetime.now() - timedelta(minutes=30)
    now_after30min = datetime.now() + timedelta(minutes=30)
    day_before30min = date(now_before30min.year, now_before30min.month, now_before30min.day)
    hour_after30min = int(now_after30min.hour)
    posts = Post.query.filter(Post.date == day_before30min).all()

    temperature1=temperature2=temperature3=temperature4=temperature5=temperature6=temperature7=temperature8=temperature9=temperature10=\
    temperature11=temperature12=temperature13=temperature14=temperature15=temperature16=temperature17=temperature18=temperature19=temperature20=\
    temperature21=temperature22=temperature23=temperature24=\
    humidity1=humidity2=humidity3=humidity4=humidity5=humidity6=humidity7=humidity8=humidity9=humidity10=\
    humidity11=humidity12=humidity13=humidity14=humidity15=humidity16=humidity17=humidity18=humidity19=humidity20=\
    humidity21=humidity22=humidity23=humidity24=\
    co1=co2=co3=co4=co5=co6=co7=co8=co9=co10=co11=co12=co13=co14=co15=co16=co17=co18=co19=co20=co21=co22=co23=co24=""

    temperature60 = []
    humidity60 = []
    co60 = []
    with open('data60.pickle', 'rb') as f:
        data60 = pickle.load(f)
    for i in range(len(data60)):
        temperature60.append(data60[i][0])
        humidity60.append(data60[i][1])
        co60.append(data60[i][2])
    temperature60 = [x for x in temperature60 if math.isnan(x) == False]
    humidity60 = [x for x in humidity60 if math.isnan(x) == False]
    co60 = [x for x in co60 if math.isnan(x) == False]
    temperature = str(format(float(np.mean(temperature60)), '.2f'))
    humidity = str(format(float(np.mean(humidity60)), '.2f'))
    co = str(int(np.mean(co60)))


    if hour_after30min==0:temperature24,humidity24,co24=temperature,humidity,co
    elif hour_after30min==23:temperature23,humidity23,co23=temperature,humidity,co
    elif hour_after30min==22:temperature22,humidity22,co22=temperature,humidity,co
    elif hour_after30min==21:temperature21,humidity21,co21=temperature,humidity,co
    elif hour_after30min==20:temperature20,humidity20,co20=temperature,humidity,co
    elif hour_after30min==19:temperature19,humidity19,co19=temperature,humidity,co
    elif hour_after30min==18:temperature18,humidity18,co18=temperature,humidity,co
    elif hour_after30min==17:temperature17,humidity17,co17=temperature,humidity,co
    elif hour_after30min==16:temperature16,humidity16,co16=temperature,humidity,co
    elif hour_after30min==15:temperature15,humidity15,co15=temperature,humidity,co
    elif hour_after30min==14:temperature14,humidity14,co14=temperature,humidity,co
    elif hour_after30min==13:temperature13,humidity13,co13=temperature,humidity,co
    elif hour_after30min==12:temperature12,humidity12,co12=temperature,humidity,co
    elif hour_after30min==11:temperature11,humidity11,co11=temperature,humidity,co
    elif hour_after30min==10:temperature10,humidity10,co10=temperature,humidity,co
    elif hour_after30min==9:temperature9,humidity9,co9=temperature,humidity,co
    elif hour_after30min==8:temperature8,humidity8,co8=temperature,humidity,co
    elif hour_after30min==7:temperature7,humidity7,co7=temperature,humidity,co
    elif hour_after30min==6:temperature6,humidity6,co6=temperature,humidity,co
    elif hour_after30min==5:temperature5,humidity5,co5=temperature,humidity,co
    elif hour_after30min==4:temperature4,humidity4,co4=temperature,humidity,co
    elif hour_after30min==3:temperature3,humidity3,co3=temperature,humidity,co
    elif hour_after30min==2:temperature2,humidity2,co2=temperature,humidity,co
    elif hour_after30min==1:temperature1,humidity1,co1=temperature,humidity,co

    for post in posts:
        if temperature24:post.temperature24=temperature24
        elif temperature23:post.temperature23=temperature23
        elif temperature22:post.temperature22=temperature22
        elif temperature21:post.temperature21=temperature21
        elif temperature20:post.temperature20=temperature20
        elif temperature19:post.temperature19=temperature19
        elif temperature18:post.temperature18=temperature18
        elif temperature17:post.temperature17=temperature17
        elif temperature16:post.temperature16=temperature16
        elif temperature15:post.temperature15=temperature15
        elif temperature14:post.temperature14=temperature14
        elif temperature13:post.temperature13=temperature13
        elif temperature12:post.temperature12=temperature12
        elif temperature11:post.temperature11=temperature11
        elif temperature10:post.temperature10=temperature10
        elif temperature9:post.temperature9=temperature9
        elif temperature8:post.temperature8=temperature8
        elif temperature7:post.temperature7=temperature7
        elif temperature6:post.temperature6=temperature6
        elif temperature5:post.temperature5=temperature5
        elif temperature4:post.temperature4=temperature4
        elif temperature3:post.temperature3=temperature3
        elif temperature2:post.temperature2=temperature2
        elif temperature1:post.temperature1=temperature1

        if humidity24:post.humidity24=humidity24
        elif humidity23:post.humidity23=humidity23
        elif humidity22:post.humidity22=humidity22
        elif humidity21:post.humidity21=humidity21
        elif humidity20:post.humidity20=humidity20
        elif humidity19:post.humidity19=humidity19
        elif humidity18:post.humidity18=humidity18
        elif humidity17:post.humidity17=humidity17
        elif humidity16:post.humidity16=humidity16
        elif humidity15:post.humidity15=humidity15
        elif humidity14:post.humidity14=humidity14
        elif humidity13:post.humidity13=humidity13
        elif humidity12:post.humidity12=humidity12
        elif humidity11:post.humidity11=humidity11
        elif humidity10:post.humidity10=humidity10
        elif humidity9:post.humidity9=humidity9
        elif humidity8:post.humidity8=humidity8
        elif humidity7:post.humidity7=humidity7
        elif humidity6:post.humidity6=humidity6
        elif humidity5:post.humidity5=humidity5
        elif humidity4:post.humidity4=humidity4
        elif humidity3:post.humidity3=humidity3
        elif humidity2:post.humidity2=humidity2
        elif humidity1:post.humidity1=humidity1

        if co24:post.co24=co24
        elif co23:post.co23=co23
        elif co22:post.co22=co22
        elif co21:post.co21=co21
        elif co20:post.co20=co20
        elif co19:post.co19=co19
        elif co18:post.co18=co18
        elif co17:post.co17=co17
        elif co16:post.co16=co16
        elif co15:post.co15=co15
        elif co14:post.co14=co14
        elif co13:post.co13=co13
        elif co12:post.co12=co12
        elif co11:post.co11=co11
        elif co10:post.co10=co10
        elif co9:post.co9=co9
        elif co8:post.co8=co8
        elif co7:post.co7=co7
        elif co6:post.co6=co6
        elif co5:post.co5=co5
        elif co4:post.co4=co4
        elif co3:post.co3=co3
        elif co2:post.co2=co2
        elif co1:post.co1=co1

    db.session.commit()
    return "1"



@app.route('/update_1min')
def update_1min():
    temperature=request.args.get("temperature")
    humidity=request.args.get("humidity")
    co=request.args.get("co")
    with open('data60.pickle', 'rb') as f:
        data60 = pickle.load(f)
    if len(data60)>=60:
        for i in range(len(data60)-59):
            data60.pop(0)
    data60.append([float(temperature), float(humidity), int(co)])

    with open('data60.pickle', 'wb') as f:
        pickle.dump(data60, f)
    return "success"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)