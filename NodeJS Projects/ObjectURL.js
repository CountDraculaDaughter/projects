const http = require('http');
const {URL} = require('url');
let data = 
{
    trimmedPath:
        function(urlPath)
        {
            return urlPath.replace(/^\/+|\/+$/g,'');
        },
    queryStringObject:
        function(entry)
        {
            return Object.fromEntries(entry);
        },
    method:
        function(reqs)
        {
            return reqs.method.toLowerCase();
        },
    headers:
        function(reqs)
        {
            return reqs.headers;
        }
};
const server = http.createServer(function(req,res){
    const baseURL = 'http://'+ req.headers.host + '/';
    const parsedUrl = new URL(req.url, baseURL);
    console.log('Parsed URL: ',parsedUrl);

    //get the untrimed path from the url
    const path = parsedUrl.pathname; 
    console.log('Path: ',path);

    //trimmed path
    let objectA = data.trimmedPath(path);
    //let trimmedPath = path.replace(/^\/+|\/+$/g,'');
    let trimmedPathString = JSON.stringify(objectA);
    console.log('Trimmed Path: ', trimmedPathString);

    //Get the query string as an object
    const urlquery= parsedUrl.searchParams
    let entries = urlquery.entries();
    let objectB = data.queryStringObject(entries);
    let queryStringObjectString = JSON.stringify(objectB);
    //const queryStringObject = Object.fromEntries(entries);
    console.log('Query String Object: ',queryStringObjectString);

    //Get the HTTP method
    //const method = req.method.toLowerCase();
    let objectC = data.method(req);
    let method = JSON.stringify(objectC);
    console.log('Method: ',method);

    //Get the headers as an object
    //var headers = req.headers;
    let objectD = data.headers(req);
    let headers = JSON.stringify(objectD);
    console.log('Headers: ',headers);

    //res.end('Hello World\n');
    res.end(`Parsed URL: ${parsedUrl}\nPath: ${path}\nTrimmed Path: ${trimmedPathString}\nQueried String: ${queryStringObjectString}\nMethods: ${method}\nHeaders: ${headers}`);
});
server.listen(8081);
