from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def principal():
    return render_template ('index.html')

@app.route('/información')
def información():
    return render_template('información.html')

@app.route('/Servicios.html')
def Servicios():
    return render_template('Servicios.html')

if __name__== 'main':
    app.run(debug=True)