from flask import Flask, request, Response
import json


app = Flask(__name__)
my_string = (
    f"<h1 style='color:red;text-align:center'> My Header</h1>Lorem ipsum dolor sit amet consectetur adipiscing elit. Nulla fermentum commodo tortor sed sagittis.<br>"
    f"Mauris risus nunc, blandit et imperdiet et, dapibus vitae ante. In at velit in ante consequat ultricies<br>"
    f"id a dui. Nullam posuere venenatis mi id posuere. Sed pellentesque dictum nunc, vel condimentum arcu<br>"
    f"eleifend at. In hac habitasse platea dictumst. Nulla nec mi nisi. Nulla commodo ipsum sit amet porttitor<br>"
    f"consequat. Fusce posuere porta sodales. Maecenas sed est convallis risus dignissim hendrerit tristique<br>"
    f" felis.<br>")


@app.route("/")
def get_root():
    return "Hello World!"


# Example query: http://127.0.0.1:3000/getsum?name=Matias&age=32
@app.route("/getsum")
def get_sum():
    print(request.args)
    name = request.args.get("name")
    age = request.args.get("age")
    return f"{my_string}Morjesta vaan, {name}<br>Age: {age}"


# Example query: http://127.0.0.1:3000/multiply/5/5
# Example result in JSON: '{num: 5, result: 25}'
@app.route('/multiply/<num>/<multiplier>')
def multiply(num, multiplier):
    try:
        num = int(num)
        multiplier = int(multiplier)
    except ValueError:
        response_data = {'msg': "input is not a number", 'input_numbers': [num, multiplier]}
        statusnumber = 200
        response = Response(response=json.dumps(response_data), status=statusnumber, mimetype='application/json')
        return response
        
    if 0 < num < 100 and 0 < multiplier < 100:
        result = num * multiplier
        response_data = {'msg': 'Calculation done', 'input_numbers': [num, multiplier], 'result': result}
        statusnumber = 200
    else:
        # All this to match status code
        response_data = {'msg': "num out of bounds", 'input_numbers': [num, multiplier]}
        statusnumber = 400

    response = Response(response=json.dumps(response_data), status=statusnumber, mimetype='application/json')
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
