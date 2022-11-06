var current = 'n'
var ctx = null

const API_PATH = `http://129.151.213.44:8080/compute/`

async function get_primes(func){
    const url = API_PATH + func
    const response = await fetch(url).then(response => response.json())
    return response
}

async function send_func(){
    current = document.getElementById('user_func_input').value
    document.getElementById("output").innerHTML = current
    await draw_on_canvas(current, ctx)
}

function put_pixel(x, y, ctx){
    ctx.fillRect(x, y, 1, 1)
}

async function draw_on_canvas(func, ctx){
    const primes = await get_primes(func)
    ctx.fillStyle = '#FFFFFF'
    ctx.fillRect(0, 0, 300, 300)
    ctx.fillStyle = '#BD0000'
    for (const key in primes){
        var row = key.split(';')
        var x = parseInt(row[0])
        var y = parseInt(row[1])
        put_pixel(x + 150, y + 150, ctx)
    }
}

async function init(){
    var canvas = document.getElementById("display")
    ctx = canvas.getContext("2d")
    ctx.fillStyle = '#BD0000'
    document.getElementById("output").innerHTML = current
    draw_on_canvas(current, ctx)
}