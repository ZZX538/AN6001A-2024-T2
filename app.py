#
#Syn code spaces is very high risk, sometimes fail

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        a = request.form['options']
        print(a)
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()


