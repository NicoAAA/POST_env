/* 
SENA CBA CENTRO DE BIOTECNOLOGIA AGROPECUARIA
PROGRAMACION DE SOFTWARE

FICHA: 2877795
AUTOR: NICOLAS ANDRES ACOSTA HIGUERA
PROYECTO: POST (static/JS/script.js)
FECHA: 2024-08-01
VERSION: 4.5.6  
*/

/** 
 * @description Selecciona el primer elemento del documento con la clase 'next'.
 * @type {Element}
 */


let next = document.querySelector('.next');
let prev = document.querySelector('.prev');

next.addEventListener('click', function() {
    // Selecciona todos los elementos del DOM que tienen la clase 'item'.
    let items = document.querySelectorAll('.item');

    // Verifica si hay elementos en la lista
    if (items.length > 0) {
        // Mueve el primer elemento al final
        let firstItem = items[0]; // Toma el primer elemento
        document.querySelector('.slide').appendChild(firstItem); // Mueve el primer elemento al final
    }
});

prev.addEventListener('click', function() {
    // Selecciona todos los elementos del DOM que tienen la clase 'item'.
    let items = document.querySelectorAll('.item');

    // Verifica si hay elementos en la lista
    if (items.length > 0) {
        // Mueve el último elemento al inicio
        let lastItem = items[items.length - 1]; // Toma el último elemento
        document.querySelector('.slide').prepend(lastItem); // Mueve el último elemento al inicio
    }
});

