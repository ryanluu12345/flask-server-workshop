from flask import Flask, render_template,redirect, url_for, request
import json

app = Flask(__name__)

@app.route("/")
def main():
    your_name = "Ryan Luu"
    #The name = your_name line can be deconstructed as:
    #"name" is the variable that will be accessed on the front end
    #"your_name" is the variable that is passed from the backend (look above)
    #You can pass a variety of data structures, not just strings
    return render_template("index.html",name = your_name)

@app.route("/handleName",methods = ["POST","GET"])
def handle_name():
    data = {}

    #Checks if the request is a post method
    #If it is a form submit, it will be a post because that is how we defined it on the front end
    if request.method == "POST":
        #Data from the form is typically processed here
        data = request.form #All the data from the form
        name = request.form["name"] #The specific name from the form
        print(data)
        print(name)
    return redirect(url_for("main")) #Redirects to the main route


if __name__ =="__main__":
    app.run(debug=True) #Take out in production
