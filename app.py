from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_drowsiness', methods=['POST'])
def run_drowsiness():
    output = subprocess.check_output(["python", "drowsiness.py"])
    return render_template('output_window.html', output=output.decode())

if __name__ == '__main__':
    app.run(debug=True)
