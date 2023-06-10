function calculateIncome(){
	const amountElem = document.getElementById('amount');
	const monthsElem = document.getElementById('months');
	const rateElem = document.getElementById('rate');
	let amount;
	let months;
	let rate;
	try {
		amount = Number(amountElem.value);
		months = Number(monthsElem.value);
		rate = Number(rateElem.value);
	} catch (error) {
		alert(error);
		return;
	}
	if (amount < 0){
		alert('No se permite montos negativos.');
		return;
	}
	if (months < 0){
		alert('No se permite meses negativos.');
		return;
	}
	if (rate < 0 || rate > 100){
		alert('El rango de la tasa es de 0 a 100.');
		return;
	}
	let amountAccumulated = amount;
	let result = [];
	for (let month = 1; month <= months; month++) {
		let actualRate = amountAccumulated * rate / 100;
		let income = [month, amountAccumulated, actualRate, amountAccumulated + actualRate];
		amountAccumulated += actualRate
		result.push(income);
	}
	this.createTable(result);
}

function createTable(tableData) {
	let table = document.getElementById('table');
	let tableBody = document.getElementById('tbody');
	let tableHeaderRowCount = 1;
	let rowCount = table.rows.length;
	for (let i = tableHeaderRowCount; i < rowCount; i++) {
		table.deleteRow(tableHeaderRowCount);
	}
	tableData.forEach(function(rowData) {
	  let row = document.createElement('tr');
  
	  rowData.forEach(function(cellData) {
		let cell = document.createElement('td');
		cell.appendChild(document.createTextNode(cellData));
		row.appendChild(cell);
	  });
  
	  tableBody.appendChild(row);
	});
  
	table.appendChild(tableBody);
	document.body.appendChild(table);
}