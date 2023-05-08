from flask_frozen import Freezer
from roman_numerals_3 import app

freezer = Freezer(app)

app.config['FREEZER_DESTINATION'] = 'build'


@app.route('/freeze')
def freeze():
    freezer.freeze()
    return 'HTML files generated successfully!'

if __name__ == '__main__':
    freezer.run(debug=True)
