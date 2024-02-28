const http = require('http');
const path = require('path');
const fs = require('fs');
const server = http.createServer(function(req, res)
{
    const recievedString = req.url.replace('/','').trim();
    console.log(recievedString);
    const isFile = recievedString.includes('.')? true : false;
    if (isFile)
    {
        fs.readFile(recievedString, {encoding: 'utf8'}, (err, content) =>
        {
            if(err)
            {
                const reqData = `Request Data \nMethod: ${req.method} \nHost: ${req.headers.host} \nAgent: ${req.headers['user-agent']}\n`;
                fs.writeFile(recievedString, reqData, (err) => 
                {
                    if (err) throw err;
                    res.end('File Created');
                });
            }
            else
            {
                console.log(content);
                res.end(`File Content:\n${content}`);
            }
        });
    }
    else
    {
        fs.readdir(recievedString, (err) =>
        {
            if (err)
            {
                fs.mkdir(recievedString, (err) => 
                {
                    if (err) throw err;
                    res.end('directory created');
                });
            }
            else
            {
                let strContent = content.toString();
                res.end(`Directory Content:\n${strContent}`);
            }
        });
    }
});
server.listen(3000, function()
{
    console.log('The server is listening on port 3000');
});
