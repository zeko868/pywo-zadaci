
from flask import Flask, render_template

app=Flask(__name__)

@app.route("/<greeting>")  #to je dekorator (ovaj konkretno govori da da se u root direktoriju pokrene (ispiše) "Hello world")
def template_test(greeting):
    return render_template('template.html', my_string=greeting)

@app.route("/")
def index():
    return render_template('index.html')
if __name__=='__main__':
    app.run(debug=True)