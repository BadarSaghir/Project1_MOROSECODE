from flask import Flask, render_template
from flask.globals import request
app = Flask(__name__)


@app.route('/',methods=[ 'GET','POST'])
def index():
    if request.method == 'POST':
        if request.form['Radios']=='encode':
            return 'encoded'
        elif request.form['Radios']=='decode':
            return 'decoded'
    return request.form['editor1']
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 