from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config["DEBUG"] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
        
            <label>
            Rotate by:<input type="text" name = "rot" value="0"/> 
            </label><br>
            <textarea name="text">
            {0}    
            </textarea><br>
            <label>
            <input type="submit" value="Submit Query"/>
            </label>
        </form>
    </body>
    
</html>
"""

@app.route("/")

def index():
    return form.format(0)
@app.route("/", methods=['POST'])

def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    rot_int = int(rot)
    encrypt = rotate_string(text, rot_int)
    content = encrypt
    error = rot_int < 0
    
    return form.format(content)

app.run()