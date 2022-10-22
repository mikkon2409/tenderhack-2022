let rows = [];
function getRequest() {
  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'http://127.0.0.1:5000/query-example?text=' + document.getElementById('search').value, false);
  xhr.send();

  if (xhr.status != 200) {
    console.log(xhr.status + ': ' + xhr.statusText); // пример вывода: 404: Not Found
  } else {
    // let doc = JSON.parse(xhr.response)
    let table = document.getElementById("block")
    rows.forEach(element => {
      table.removeChild(element);
    })
    rows = [];
    for (let i = 0; i < 5; i++) {
      // Insert a row at the end of table
      var newRow = table.insertRow();
      rows.push(newRow);

      // Insert a cell at the end of the row
      var newCell = newRow.insertCell();

      // Append a text node to the cell
      var newText = document.createTextNode(xhr.responseText);
      newCell.appendChild(newText)
    }
  }
}
