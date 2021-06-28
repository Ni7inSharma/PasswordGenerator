import random
import string
from flask import Flask,render_template,request
app = Flask(__name__)

def generator(lenght):
    password=""

    for i in range(lenght):
        gen = random.randrange(33,127)
        password= password+chr(gen)

      
    return password

        


@app.route('/' , methods=['GET', 'POST'])
def hello_world():
   p=""
   if request.method == "POST" :
      
      len=request.form.get("number")
      p=generator(int(len))

   return render_template("index.html", content=p)

if __name__ == '__main__':
   app.run(debug=True)
