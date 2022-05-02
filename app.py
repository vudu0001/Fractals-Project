from flask import Flask,Response,jsonify, render_template ,logging,request
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/getimage",methods=["POST","GET"])
def get_img_snowlow():
    finalres=""
    print(request)
    res = str(request)[str(request).find('?')+1:str(request).rfind("'")]
    print(res)
    if res=="snowlow":
        finalres = "Koch-Snowflake-LOW.png"
    elif res=="snowhigh":
        finalres = "Koch-Snowflake-HIGH.png"
    elif res=="pietlow":
        finalres = "Piet-Mondrian-LOW.png"
    elif res=="piethigh":
        finalres = "Piet-Mondrian-HIGH.png"
    elif res=="treelow":
        finalres = "Tree-Branch-Fractal-LOW.png"
    elif res=="treehigh":
        finalres = "Tree-Branch-Fractal-HIGH.png"

    return finalres



#run server
if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)
    
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
