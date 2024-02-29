from flask import Flask,request,render_template,jsonify

app = Flask(__name__)

@app.route('/')
def hello_page():
    return render_template('index.html')


@app.route('/math',methods=['POST'])
def math_operations():
    if(request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops == 'add':
            r = num1 + num2
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'subtract':
            r = num1 - num2
            result = "The subraction of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'multiply':
            r = num1 * num2
            result = "The multipilcation of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'divide':
            r = num1 / num2
            result = "The division of " + str(num1) + " and " + str(num2) + " is " + str(r)
        if ops == 'mod':
            r = num1 % num2
            result = "The modulo of " + str(num1) + " and " + str(num2) + " is " + str(r)

        
        return render_template('results.html',result = result)


if __name__ == '__main__':
    app.run(debug=True)