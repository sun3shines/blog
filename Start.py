# -*- coding: utf-8 -*-
# @Time    : 2017/8/1 14:50
# @File    : Start.py
"""
应用启动类
"""



from flask import Flask,render_template,flash,url_for,redirect,Blueprint
from flask_bootstrap import Bootstrap

from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_login import LoginManager,login_user,UserMixin,logout_user,login_required
from flask_sqlalchemy import SQLAlchemy
import sys
#解决flash的一个bug
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


app = Flask(__name__)

app.config.from_pyfile('application.cfg')

db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap(app)
moment=Moment(app)
login_manger=LoginManager()
login_manger.session_protection='strong'
login_manger.login_view='blog.login'
login_manger.init_app(app)

@login_manger.user_loader
def load_user(user_id):
    from Model import Users
    return Users.query.get(int(user_id))

"""
蓝图注册
"""
def init():
    from Views import blog
    app.register_blueprint(blueprint=blog,url_prefix='/blog')

@app.route('/')
def index():
    return redirect(url_for('blog.index'))

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0',port=6679,debug=True)


