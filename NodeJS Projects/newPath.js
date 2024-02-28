const path = require('path');
const pathList = path.dirname(__filename).split(path.sep);
for (const x in pathList)
{
    console.log(pathList[x]);
}
let newPath = '/';
for (let y = 0; y < pathList.length; y++)
{
    newPath = path.join(newPath, pathList[y]);
}
console.log(newPath);
