from flask import Flask, request, render_template, redirect
app = Flask(__name__)

@app.route('/mypage/me', methods=['GET'])
def me():
   if request.method == 'GET':
       print("We received GET")
       return render_template("Wizytówka.html")

@app.route('/mypage/contact', methods=['GET','POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("Wizytówka_2.html")
   elif request.method == 'POST':
        print(request.form)
        return redirect("/message")