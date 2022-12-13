from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():    
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

if __name__ == '__main__':
    app.run(port=8080, debug=True)