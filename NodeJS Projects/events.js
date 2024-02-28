const events = require('events');
if (process.argv[2] === undefined || process.argv[3] === undefined)
{
    console.log('please follow the convention for this program: node events.js [word] [sentence]');
}
let word = process.argv[2];
let sentence = process.argv[3];
const event = new events.EventEmitter();
const eventHandler = (occurance, position) => 
{
    console.log(`There is ${occurance} copy at position ${position}`);
}
event.on('found',eventHandler);
function locateWord (w,s)
{
    counter = 0;
    for (let x = 0; x < s.length; x++)
    {
        if(s.substring(x,x+3) === 'the')
        {
            counter += 1;
            event.emit('found', counter, x);
        }
    }
    console.log(`'${w}' is found ${counter} times`);
}
locateWord(word, sentence);
