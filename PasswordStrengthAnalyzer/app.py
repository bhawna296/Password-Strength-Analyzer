from flask import Flask, render_template, request
from password_generator import generate_password
from password_checker import check_password, entropy
from database import *  

app = Flask(__name__)   

create_database()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():  
    
    password = request.form["password"]

    reused = password_exists(password)

    score, suggestions = check_password(password)
    entropy_value = entropy(password)

    if score >= 85:
        strength = "Very Strong"
    elif score >= 65:
        strength = "Strong"
    elif score >= 45:
        strength = "Medium"
    else:
        strength = "Weak"

    generated_password = generate_password()    

    if not reused:
        save_password(password)

    return render_template(
                           "result.html", 
                           password=password,
                           score=score, 
                           strength=strength,
                           suggestions=suggestions, 
                           reused=reused, 
                           generated_password=generated_password,
                           entropy=entropy_value
                           )

@app.route("/report")
def report():
    
    with open("report.txt", "w") as report_file:
        report_file.write("Password Analysis Report")

    return "Report Created"

if __name__ == "__main__":

    app.run(debug=True)




   