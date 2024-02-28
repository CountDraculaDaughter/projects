const http = require('http');
const url = require('url');
var list = [];
const reqHandler = (req,res) =>
{
    switch(req.method)
    {
        case 'POST':
            let item = '';
            req.setEncoding('utf8');
            req.on('data', (chunk) =>
            {
                item += chunk;
            })
            req.on('end', () =>
            {
                list.push(item);
                res.end('Item added to list\n');
            })
        case 'GET':
            if(list.length === 0)
            {
                res.end('Your list is empty. Well Done!!');
            }
            else
            {
                let response = '';
                response = list.map((element, index) =>
                {
                    return `${index+1} ) ${element}`;
                }).join('\n');
                res.end(response)
            }
        case 'DELETE':
            let urlParse = url.parse(req.url, true).pathname;
            let index = url.slice(1);
            if(NaN(index))
            {
                res.end('Invalid index\n');
            }
            else
            {
                let i = parseInt(index, 10);
                i--;
                if(list.length <= i)
                {
                    res.end('Index does not exist in list\n');
                }
                else
                {
                    list.splice(i,1);
                    res.end('Item removed from list');
                }
            }
        case 'PUT':
            let putPath = url.parse(req.url, true).pathname;
            let putIndex = putPath.slice(1);
            if (isNaN(putIndex))
            {
                res.end('Invalid Index\n');
            }
            else
            {
                let i = parseInt(putIndex);
                i--;
                if (list.length <= i)
                {
                    res.end('Index does not exist in list\n');
                }
                else
                {
                    let newitem = '';
                    req.setEncoding('utf8');
                    req.on('data', (chunk) =>
                    {
                        newitem += chunk;
                    });
                    req.on('end',()=>
                    {
                        console.log('Updating the item in the list at index ',i,' with ', newitem);
                        list.splice(i, 1, newitem);
                        console.log('list after update: ', list);
                        res.end('Item updated in the list\n');
                    });
                }
            }
        break;
        default:
            console.log('Unsupported method');
            res.end('Unsupported method\n');
            break;
    }
}
