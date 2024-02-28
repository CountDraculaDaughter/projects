//Dependencies
const http = require('http');
//Server Object that will respond with a string
const server = http.createServer(function(req, res) 
{
    //console.log(req.headers);
    console.log(req.url);
    //console.log(req.method);
    //console.log(req.protcol);
    res.end('Welcome to Hell \n');
}
);
//Server listens on port 3000
server.listen(3000, function() 
{
    console.log('The server is listening on port 3000');
}
);
