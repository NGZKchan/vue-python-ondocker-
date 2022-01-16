from flask import Flask                           
app = Flask(__name__)                             

@app.route('/api/')                                   
def hello_world():                                
    return "Hello World!"                         

@app.route('/ngzk/')                                   
def nkzk():                                
    return "NGZKchan"                         

if __name__ == '__main__':                        
    app.run(host="0.0.0.0", port=5000, debug=True)