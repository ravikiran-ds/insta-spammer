from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from messenger import send_msg


app=Flask(__name__)
app.config['SECRET_KEY']="ssss"

class InfoForm(FlaskForm):
    username=StringField("Enter Username")
    message=StringField('Enter Message')
    times=StringField('Times to Send')
    submit=SubmitField('Submit')
@app.route('/',methods=['GET','POST'])
def index():
    name=False
    msg=False
    times=False
    form=InfoForm()
    if form.validate_on_submit():
        name=form.username.data
        msg=form.message.data
        times=int(form.times.data)
        print(name,msg,times)
        send_msg(name,msg,times)
        form.username.data=''
        form.message.data=''
        form.times.data=''
    return render_template("form.html",form=form)

if __name__=='__main__':
    app.run(debug=True)
