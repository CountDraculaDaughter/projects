//old API
const http = require('http');
const fs = require('fs');
const url = require('url');
const server = http.createServer( (req, res) =>
{
    console.log(`req.url:${req.url}`);
    //Parsing the req.url using the old API Step 2
    /*const parsedurl = url.parse(req.url, true);
    console.log(parsedurl);*/
    //Parsing the req.url using the old API Step 6
    /*const {pathname, query} = url.parse(req.url, true);
    console.log(pathname);
    console.log(query);*/
    //Parsing the req.url using the old API Step 8
    console.log(`req.url:${req.url}`);
    const {pathname, query} = url.parse(req.url, true);
    console.log(pathname);
    console.log(query);
    console.log(`text : ${query.text}\nquantity : ${query.quantity}\ncategory : ${query.category}`);
    res.end('Done');
});
server.listen(3001,() =>
{
    console.log('Server running on 3001');
});
