const http = require('http');
const fs = require('fs');
const path = require('path');
const server = http.createServer(function(req, res) 
{
    let url = path.basename(req.url);
    folder = __dirname + '/' + url;
    fs.readdir(folder, (err) => 
    {
        if (err)
        {
            console.log('Folder does not exist on the server');
        }
        else
        {
            console.log(folder);
        }
    });
}
);
server.listen(3000, function() 
{
    console.log('The server is listening on port 3000');
}
);
