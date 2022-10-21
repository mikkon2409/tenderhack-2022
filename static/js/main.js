function getRequest(){
  var xhr = new XMLHttpRequest();

  xhr.open('GET', 'http://127.0.0.1:5000/form-example', false);
  xhr.send();

  if (xhr.status != 200) {
    alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
  } else {
    alert( xhr.responseText ); // responseText -- текст ответа.
  }
}