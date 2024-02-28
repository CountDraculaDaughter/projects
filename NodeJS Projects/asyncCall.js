const fs = require('fs');
if (process.argv[2] == undefined || process.argv[3] == undefined)
{
    console.log('Missing arguments\nCorrect Invocation: AsyncCall.js [filename][Text]');
}
    const file = process.argv[2];
    const str = process.argv[3];
    let reverse = str.split(" ").reverse().join(" ") + '\n';
    fs.readFile(file,{encoding: 'utf-8'},(err) =>
    {
        if(err)
        {
            fs.writeFile(file,reverse,(err)=>
            {
                if (err) throw err;
                console.log('File is created.');
            });
        }
        else
        {
            fs.appendFile(file, reverse, (err) => 
            {
                if (err) throw err;
            });
        }
    });
