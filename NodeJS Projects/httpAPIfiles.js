const http = require('http');
const fs = require('fs');
const path = require('path');
const server = http.createServer(function(req, res) 
{
    const urlBase = path.basename(req.url);
    const urlExt = path.extname(req.url);
    if(urlExt != '.txt')
    {
        console.log('Wrong file extension')
    }
    else
    {
        const pwd = __dirname + '/' + urlBase
        fs.readFile(pwd, {encoding: 'utf-8'}, (err, content) => 
        {
            if (err)
            {
                console.log('File does not exist in local directory');
            }
            else
            {
                console.log(content);
            }
        });
    }
});
server.listen(3000, function()
{
    console.log('The server is listening on port 3000');
});
