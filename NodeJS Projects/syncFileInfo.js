const fs = require('fs');
const path = require('path');
if (process.argv.length < 3)
{
    console.log('Please follow the commands syntax: node syncFileInfo.js []');
}
let work_path = __dirname;
let found = false;
while (!found && work_path !== '/')
{
    let contents = fs.readdirSync(work_path);
    if (contents.includes(process.argv[2]))
    {
        found = true;
    }
    else
    {
        work_path.resolve(work_path, '../');
    }
}
if (found)
{
    let entry = path.join(work_path, process.argv[2]);
    let status = fs.statSync(entry);
    if (status.isDirectory())
    {
        console.log(`The folder ${process.argv[2]} exists in the path ${work_path} and was created at ${status.birthtime}`);
    }
    else
    {
        console.log(`The file ${process.argv[2]} exists in the path ${work_path} and was modified at ${status.mtime}`);
    }
}
else
{
    console.log(`The entry ${process.argv[2]} does not exist`);
}
