// REST

const usuario = {
    nome: "Diego",
    idade: 23,
    empresa: "Rocketseat"
};

const {nome, ...resto} = usuario;

console.log(nome);
console.log(resto);

// SPREAD

const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const arr3 = [ ...arr1, ...arr2];