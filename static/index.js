function handleClick(btnName, colorIndex) {

	// Change btn color if selected/unselected
	pricesToDisplay[colorIndex] === 1 ? pricesToDisplay[colorIndex] = 0 : pricesToDisplay[colorIndex] = 1;
	let btnStyle = pricesToDisplay[colorIndex] === 1 ?
		{
			'background-color': colors[colorIndex],
			'color': 'white',
		} : {
			'background-color': 'white',
			'color': colors[colorIndex],
		}
	$(btnName).css(btnStyle);
	drawNewChart();
}

function getData(dataset, colors) {

	// Getting columns Date and Prices(Open, High, Low, Close) + Average
	let col_names = dataset.column_names.splice(0, 5);

	let data = {
		col_names,
		values: dataset.data,
		colors
	}
	return data;
}

function getChartData(data, pricesToDisplay) {
	// let data = getData({{dataset|tojson|safe}});
	let datasets = [];		// datasets for a chart
	let dataset = [];		// single dataset for one Price (Open, High etc.)
	let labels = [];		// date labels

	let dataSize = data.values.length;
	let colNum = data.col_names.length;

	for (let col = 0; col < colNum; col++) {
		// Calculate a dataset for selected prices
		if (pricesToDisplay[col - 1] === 1 || col === 0) {
			for (let row = dataSize - 1; row > -1; row--) {
				if (col === 0) labels.push(data.values[row][col]);
				else dataset.push(data.values[row][col]);
			}
			if (col !== 0) {
				datasets.push({
					data: dataset,
					label: data.col_names[col],
					borderColor: data.colors[col - 1],
					fill: false
				});
				dataset = [];
			}
		}
	}

	return {
		type: 'line',
		data: { labels, datasets },
		options: {
			elements: {
				point: { radius: 0 }
			},
			legend: {
				display: false
			}
		},

	}
}
