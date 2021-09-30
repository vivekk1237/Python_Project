from flask import Flask,render_template,url_for,redirect,flash,request
from flask_sqlalchemy import SQLAlchemy
import speech_recognition as sr
import pyttsx3
import datetime
from game import rockPaperScissor,guessingNumber,Snake

app=Flask(__name__,template_folder='template')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///LocoPy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False,primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30))
    fullname= db.Column(db.String(60))
    password = db.Column(db.String(80), nullable=False)
    repassword = db.Column(db.String(80), nullable=False)


    def __repr__(self) -> str:
        return f"{self.fullname} and {self.username}"

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/home/<username>")
def userhome(username):
    return render_template('userhome.html',user=username)


@app.route("/voiceerror")
def speech():
    initial()
    while True:
            
        r=sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            wishMe()
            speak("ok I am ready You can Speak now")
            audio = r.listen(source,phrase_time_limit=4)

        try:
            MyText=r.recognize_google(audio,language='en-in')
            string=str(MyText)
            if(string.count("login")>0):
                speak("ok got it")
                return redirect(url_for("login"))
            elif(string.count("learn")>0):
                speak("ok got it")
                return redirect(url_for("learn"))
            elif(string.count("play")>0):
                speak("ok got it")
                return redirect(url_for("play"))
            elif(string.count("why")>0):
                speak("ok got it")
                return redirect(url_for("why"))
            elif(string.count("about")>0):
                speak("ok got it")
                return redirect(url_for("about"))
            elif(string.count("home")>0):
                speak("ok got it")
                return redirect(url_for("home"))
            else:
                tell="I can't find any matching content"
                speak(tell)
                flash("I can't find any matching content")
                return render_template('home.html')
                
                

        except Exception as e:
            speak(e)
            flash("Some Error Occurred")
            return render_template('home.html')

def initial():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  
    return engine
def speak(audio):
    engine=initial()
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 

@app.route("/level1/<username>")
def level1(username):
    return render_template('Level1.html',user=username)

@app.route("/level2/<username>")
def level2(username):
    return render_template('Level2.html',user=username)

@app.route("/level3/<username>")
def level3(username):
    return render_template('Level3.html',user=username)

@app.route("/play")
def play():
    return render_template('play.html')

@app.route("/play/<username>")
def userplay(username):
    return render_template('userplay.html',user=username)

@app.route("/learn")
def learn():
    return render_template('learn.html')

@app.route("/learn/<username>")
def userlearn(username):
    return render_template('userlearn.html',user=username)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/about/<username>")
def userabout(username):
    return render_template('userabout.html',user=username)


@app.route("/why")
def why():
    return render_template('why.html')

@app.route("/why/<username>")
def userwhy(username):
    return render_template('userwhy.html',user=username)

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/forgotpassword")
def forgot():
    return render_template('forgot.html')

@app.route("/registration")
def register():
    return render_template('Reg.html')
@app.route("/home")
def logged():
    username=request.args.get('username')
    password=request.args.get('pass')
    if(username==''):
        if(password==''):
            user="*Username can't be empty"
            passw="*Password can't be empty"
            return render_template('login.html',username=user,password=passw)
        else:
            user="*Username can't be empty"
            return render_template('login.html',username=user,password="")
    else:
        if(password==''):
            passw="*Password can't be empty"
            return render_template('login.html',username="",password=passw)
        else:
            quer = User.query.filter_by(username=username,password=password)
            result=quer.first()
            if(result):
                return redirect(url_for('userhome',username=username))

            else:
                return render_template('login.html',found="*Username & Password doesn't match")

@app.route("/registered")
def registered():
    first=request.args.get("fname")
    last=request.args.get("lname")
    email=request.args.get("email")
    password=request.args.get("pass")
    confirm=request.args.get("confirm")
    check=request.args.get("checkbox")
    if(first==""):
        return render_template('Reg.html',first="*First Name can't be empty")
    elif(email==""):
        return render_template('Reg.html',email="*Email can't be empty")
    elif(password==""):
        return render_template('Reg.html',password="*Password can't be empty")
    elif(confirm==""):
        return render_template('Reg.html',confirm="*Confirm Password can't be empty")
    else:
        if(password==confirm):
            if(len(password)<6):
                return render_template('Reg.html',password="*Password must be atleast 6 characters")
            elif(check=="on"):
                data=User(username=email,firstname=first,lastname=last,fullname=first+" "+last,password=password,repassword=confirm)
                db.session.add(data)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                return render_template('Reg.html',checked="*Checkbox must be checked")
        else:
            return render_template('Reg.html',confirm="*Confirm Password and Password didn't match")

@app.route("/rockpaperscissor/<username>")
def rps(username):
    rockPaperScissor.rockPaperScissor()
    return redirect(url_for('level1',username=username))

@app.route("/forgot")
def updated():
    name=request.args.get("fullname")
    username=request.args.get("username")
    password=request.args.get("password")
    confirm=request.args.get("confirm")
    if(name==""):
        return render_template('forgot.html',name="*Name can't be empty")
    elif(username==""):
        return render_template('forgot.html',username="*Username can't be empty")
    elif(password==""):
        return render_template('forgot.html',password="*New Password can't be empty")
    elif(confirm==""):
        return render_template('forgot.html',confirm="*Confirm Password can't be empty")
    else:
        if(password==confirm):
            if(len(password)<6):
                return render_template('forgot.html',password="*New Password must be atleast 6 characters")
            else:
                quer = User.query.filter_by(username=username,fullname=name)
                missing=quer.first()
                if missing:
                    missing.password=password
                    missing.repassword=confirm
                    db.session.commit()
                    return redirect(url_for('login'))
                else:
                    return render_template('forgot.html',found="*Username & Fullname doesn't match")
        else:
            return render_template('forgot.html',confirm="*Confirm Password and Password didn't match")


@app.route("/numberguessing/<username>")
def guess(username):
    guessingNumber.guessing()
    return redirect(url_for('level1',username=username))

@app.route("/snake")
def snakegame():
    Snake.main()
    return redirect(url_for('level2'))


if __name__=='__main__':
    app.run(debug=True)