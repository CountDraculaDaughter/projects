console.log("\nPrinting in normal order\n");
for(let j = 0; j < 4; j++)
{
    console.log('The value is: ' + j );
}
console.log("\nPrinting in reverse order using setTimeout\n");
for (let i = 0; i < 4; i++) 
{
    /*set up a function here to call console.log() */
    /* put a value in msec using the value of i */ 
    let milliSeconds = i == 0 ? 5 : 4 / i;
    setTimeout(() => 
    {
        console.log('The value is: ' + i);
    }, milliSeconds);
}
