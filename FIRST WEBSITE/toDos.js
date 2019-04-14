var listElement = document.querySelector("#app ul");
var inputElement = document.querySelector('#app input');
var buttonElement = document.querySelector('#app a');

var toDos = JSON.parse(localStorage.getItem('list_toDos')) || [];

function renderToDos() {

    listElement.innerHTML = '';

    for (todo of toDos) {
        var todoElement = document.createElement('li');
        var todoText = document.createTextNode(todo);

        var linkElement = document.createElement('a');
        linkElement.setAttribute('href', '#');

        var pos = toDos.indexOf(todo);
        linkElement.setAttribute('onclick', 'deleteToDo(' + pos + ')');

        var linkText = document.createTextNode('Excluir');

        linkElement.appendChild(linkText);

        todoElement.appendChild(todoText);
        todoElement.appendChild(linkElement);

        listElement.appendChild(todoElement);
    }
}

renderToDos();

function addToDo() {
    if (inputElement.value == "") {
        alert("Digite uma tarefa válida");
        return false;
    }
    var todoText = inputElement.value;

    toDos.unshift(todoText);
    inputElement.value = "";
    renderToDos();
    saveToStorage();
}
buttonElement.onclick = addToDo;

inputElement.addEventListener("keydown", function (event) {
    if (event.keyCode === 13) {
        addToDo();
    }
});

function deleteToDo(pos) {
    toDos.splice(pos, 1);
    renderToDos();
    saveToStorage();
}

function saveToStorage() {
    localStorage.setItem('list_toDos', JSON.stringify(toDos));
}