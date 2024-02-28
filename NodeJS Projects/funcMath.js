const path = require('path');

//check for correct invocation
if (process.argv.length !== 4 ){
    console.log("Usage: " + path.basename(process.argv[1], '.js')
    + " [number]  [isEven|isPositive|squared] ");
    return;
}

let operation = {
    isEven: 
    function(numVal)
    {
        //TODO: isEven takes in a number value and returns
        // true if the number is even and false otherwise.
           if(numVal % 2 === 0)
           {
                return true;
           }
           else
           {
                return false;
           }
    },
            
    isPositive:
    //TODO: isPositive takes in a number value and returns 
    // true if the number is positive and false otherwise.
    function(numVal)
    {
        if (numVal > 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    },
    squared:
    //TODO: squared takes in a number value and returns the value of 
    // the number squared
    function(numVal)
    {
        return Math.pow(numVal, 2);
    }
};

let wrongOp = function(){
    return "Undefined operation";
 };
let mynumber = process.argv[2]; //TODO: Extract the number from the command line
let chosenOp = operation[process.argv[3]]; //TODO: Extract the operation from the command line

//TODO: Complete the if statement to check if the operation is valid then call the 
//operation on the number otherwise print an erro message
if (chosenOp === undefined)
{
    console.log(wrongOp());
}
else
{
    console.log(chosenOp(mynumber));
}
