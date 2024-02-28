const fs = require('fs');
const path = require('path');
if(process.argv[2] === undefined)
{
    console.log('Missing arguments\nCorrect Invocation: AsyncDir.js [folder]');
}
const folder = process.argv[2]
fs.readdir(__dirname + '/' + folder, (err) => 
{
    if (err)
    {
        fs.mkdir(__dirname + '/' + folder, (err) =>
        {
            if (err) throw err;
            console.log('Folder created');
        });
    }
    else
    {
        console.log(`The path to the folder: \n${__dirname + '/' + folder} `)
    }
});
