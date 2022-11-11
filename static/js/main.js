let rows = [];
function getRequest() {
  var xhr = new XMLHttpRequest();

  xhr.open('POST', '/search', true);
  xhr.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
  xhr.send(document.getElementById('search').value);

  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      if (xhr.status != 200) {
        console.log(xhr.status + ': ' + xhr.statusText); // пример вывода: 404: Not Found
      } else {
        let doc = JSON.parse(xhr.response)
        console.log(doc)
        let table = document.getElementById("block");
        let body = document.getElementById("body");
        table.removeChild(body);
        body = table.createTBody()
        body.id = "body"
        table.appendChild(body)
        doc.forEach(element => {
          // Insert a row at the end of table
          var newRow = body.insertRow();
          rows.push(newRow);
    
          // Insert a cell at the end of the row
          var newCell = newRow.insertCell();
    
          // Append a text node to the cell
          var newText = document.createTextNode(element['']['1']);
          newCell.appendChild(newText)
        });
      }
  }
  };

  
}
