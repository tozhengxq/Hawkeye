from flask import render_template,flash,redirect,session,url_for,request,g
from app import app,db,lm,oid
from .forms import LoginForm,NameForm,InceptionTableStructure
from .models import User
import inception


@app.route('/')
def statis():
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/rtquery',methods=['GET','POST'])
def rtquery():
    form = InceptionTableStructure()
    sqlresult = {}
    if request.method == "POST":
        sqlcode = request.form.get('sqlcode')
        sqlresult = inception.table_structure(sqlcode)
        return render_template('v_rtquery.html',sqlresult=sqlresult,abc=sqlcode)
    return render_template('v_rtquery.html')




