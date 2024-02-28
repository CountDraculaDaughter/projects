//new API
const http = require('http');
const fs = require('fs');
const {URL} = require('url');
const server = http.createServer( (req, res) =>
{
    console.log(`req.url:${req.url}`);
    //Parsing the req.url using the new API Step 2
    const baseURL = 'http://' + req.headers.host + '/';
    /*const parsedurl = new URL(req.url, baseURL);
    console.log(parsedurl); */
    //Parsing the req.url using the new API Step 6
    const {pathname, searchParams} = new URL(req.url, baseURL);
    console.log(pathname);
    console.log(searchParams);
    //Step 8
    console.log(`text: ${searchParams.get('text')}\nquantity: ${searchParams.get('quantity')}\ncategory: ${searchParams.get('category')}\n`);
    //Converting the searchParams object to a native JS object
    let entries = searchParams.entries();
    const query = Object.fromEntries(entries);
    console.log(`text : ${query.text}\nquantity : ${query.quantity}\ncategory : ${query.category}`);
    res.end('Done');
});
server.listen(3002, () =>
{
    console.log('Server running on 3002');
});
