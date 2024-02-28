const path = require('path');
const fs = require('fs');
const dirPath = __dirname;
const folders = dirPath.split(path.sep);
for (x in folders)
{
    fs.writeFileSync('fileWrite.txt', folders[x] + '\n');
}
for (y in folders)
{
    fs.appendFileSync('fileAppend.txt', folders[y] + '\n');
}
let data = fs.readFileSync('fileAppend.txt', 'utf8');
let fullPath = data.replaceAll('\n', path.sep);
console.log(fullPath);
