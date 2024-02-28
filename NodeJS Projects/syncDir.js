const fs = require('fs');
let folder = process.argv;
let list = fs.readdirSync(__dirname);
console.log(list);
for (let x = 2; x < folder.lenth; x++)
{
    let newDir = path.join(__dirname,folder[x]);
    fs.mkdirSync(newDir);
}
list = fs.readdirSync(__dirname);
console.log(list);
for (let y = 2; y < folder.lenth; y++)
{
    let delDir = path.join(__dirname,folder[x]);
    fs.rmdirSync(delDir);
}
list = fs.readdirSync(__dirname);
console.log(list);
