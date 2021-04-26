from flask import Flask 
app = Flask(__name__) 
 
@app.route("/") 
def hello(): 
    return "Hello World! my name is rajat sharma" 
 
if __name__ == "__main__": 
    app.run() 