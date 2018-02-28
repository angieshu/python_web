from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# @app.route('/temperature', methods=['POST'])
# def temperature():
# 	return render_template('temperature.html')

API_KEY = 'zC992yeEkw5VTye5PFJY'

@app.route('/EOD/', methods=['POST'])
@app.route('/EOD/<dataset_code>', methods=['POST'])
def info(dataset_code='APPL'):
	# database_code = request.form('name');
	r = requests.get('https://www.quandl.com/api/v3/datasets/EOD/' + dataset_code + '.json?api_key=' + API_KEY)
	json_obj = r.text
	# json_obj = r.json()

	# dataset = json_obj['dataset']
	# return render_template('index.html', dataset=dataset)
	return json_obj

@app.route('/')
def index():
	r = requests.get('https://www.quandl.com/api/v3/datasets.json?api_key=' + API_KEY + '&database_code=EOD&sort_by=id&per_page=1000&meta_data=true')
	# json_obj = r.text
	json_obj = r.json()

	datasets = json_obj['datasets']
	#
	# arr_names = []
	# for i in tmp:
	# 	arr_names.append(i['name'])

	# print arr_names
	# for i in json_obj.datasets:
	# 	arr_names.append(i.name)
	# return arr_names
	# print names
	# return json_obj
	return render_template('home.html', datasets=datasets)

if (__name__ == '__main__'):
	app.run(host='', port=7777, debug=True)
