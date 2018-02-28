from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# @app.route('/temperature', methods=['POST'])
# def temperature():
# 	return render_template('temperature.html')

API_KEY = 'zC992yeEkw5VTye5PFJY'

@app.route('/:dataset_code')
def apple():
	r = requests.get('https://www.quandl.com/api/v3/datasets/EOD/AAPL.json?api_key=' + API_KEY)
	json_obj = r.json()

	column_names = json_obj['dataset']['column_names']
	return render_template('index.html', column_names=column_names)

@app.route('/')
def index():
	r = requests.get('https://www.quandl.com/api/v3/datasets.json?database_code=EOD&sort_by=id')
	json_obj = r.text
	# json_obj = r.json()

	# tmp = json_obj['datasets']
	#
	# arr_names = []
	# for i in tmp:
	# 	arr_names.append(i['name'])

	# print arr_names
	# for i in json_obj.datasets:
	# 	arr_names.append(i.name)
	# return arr_names
	# print names
	return json_obj
	# return render_template('home.html', arr=arr_names)

if (__name__ == '__main__'):
	app.run(host='', port=7777, debug=True)
