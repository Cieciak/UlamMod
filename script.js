var context    = null
var label      = null
var expression = 'n'

function range(size){
    return Array.from({length: size}, ())
}

async function init(){
    const canvas      = document.getElementById('canvas')
    context           = canvas.getContext('2d')
    context.fillStyle = '#7793F8'
    label             = document.getElementById('function')
    label.innerHTML   = 'f(n) = ' + expression
}

async function calculate(){
    expression = document.getElementById('expression').value
    label.innerHTML = 'f(n) = ' + expression

    for (const number in )

    const result = 1+1
}

