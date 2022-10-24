
async function init(){
    const url = `https://api.github.com/repos/Cieciak/UlamMod/git/trees/main`
    const list = await fetch(url).then(res => res.json())
    const dir = list.tree.find(node => node.path === 'svg');
    document.getElementById("output").innerHTML = dir
}