from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    print('Received data:', data)

    if 'number' not in data:
        return jsonify({'error': 'Number is required'}), 400

    try:
        number = int(data['number'])
    except ValueError:
        return jsonify({'error': 'Invalid number'}), 400

    result = calculate_factorial(number)
    print('Result:', result)
	
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
