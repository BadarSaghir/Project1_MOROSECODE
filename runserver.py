from flask import Flask, render_template
from flask.globals import request
from src.morpho.str_to_mor import MoroseCode

app = Flask(__name__)
code = MoroseCode()

@app.route('/',methods=[ 'GET','POST'])
def index():
    if request.method == 'POST':
        data=request.form['editor1']
        pwd=request.form['pwd']
        if request.form['Radios']=='encode':
            code.initialize(pwd)
            crypt_=code.encrypt(data)
            return render_template('index.html', result=True, crypt=crypt_)
        elif request.form['Radios']=='decode':
            code.initialize(pwd)
            crypt_=code.decrypt(data)
            return render_template('index.html', result=True, crypt=crypt_)

        else:
            return 'An Error Occur'

    return render_template('index.html', result=False)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 