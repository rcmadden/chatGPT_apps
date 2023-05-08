from flask import Flask, render_template, request

app = Flask(__name__)

def roman_to_int(roman):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman)):
        if i > 0 and roman_map[roman[i]] > roman_map[roman[i - 1]]:
            result += roman_map[roman[i]] - 2 * roman_map[roman[i - 1]]
        else:
            result += roman_map[roman[i]]
    return result

def int_to_roman(num):
    roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    for value, numeral in sorted(roman_map.items(), reverse=True):
        while num >= value:
            result += numeral
            num -= value
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert():
    try:
        value = request.form['value']
        if value.isdigit():
            return render_template('index.html', result=int_to_roman(int(value)), type='Number')
        else:
            return render_template('index.html', result=roman_to_int(value.upper()), type='Roman')
    except:
        return render_template('index.html', error='Invalid input!')

if __name__ == '__main__':
    app.run(debug=True)
