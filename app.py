from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']

    year = request.form['year']

    return render_template(
        'successful.html',
        name=name,
        year=year
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)