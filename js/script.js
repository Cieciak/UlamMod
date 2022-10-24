var current = 0
var files = []

async function get_directory(dir_name){
    const url = `https://api.github.com/repos/Cieciak/UlamMod/git/trees/main`
    const response = await fetch(url).then(response => response.json())
    const directory = response.tree.find(node => node.path  === dir_name)
    if (directory) {
        const response = await fetch(directory.url).then(resonse => resonse.json())
        const files = response.tree.map(node => node.path)
        return files
    }
}

function split_name(text){return text.split('.')[0]}

function prev(){
    // current = (current - 1) % files.length // Funni thing happen
    current = Math.max(0, current - 1)
    document.getElementById("output").innerHTML = split_name(files[current])
    load_svg(files[current])
}

function next(){
    current = Math.min(files.length - 1, current + 1)
    document.getElementById("output").innerHTML = split_name(files[current])
    load_svg(files[current])
}

function load_svg(path){
    document.getElementById("image").src = `./svg/${path}`
}

async function init(){
    files = await get_directory('svg')
    document.getElementById("output").innerHTML = split_name(files[current])
    load_svg(files[current])
}