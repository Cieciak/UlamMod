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

function prev(){
    current = (current - 1) % files.length
    document.getElementById("output").innerHTML = files[current]
}

async function init(){
    files = await get_directory('svg')
        document.getElementById("output").innerHTML = files
    
    
}