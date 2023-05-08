from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    number = request.form['number']
    roman_numeral = ''

    # Convert the number to a Roman numeral
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_numeral += numeral
            number -= value

    return render_template('index.html', roman_numeral=roman_numeral)

if __name__ == '__main__':
    app.run()
