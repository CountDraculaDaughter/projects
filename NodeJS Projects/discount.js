//Declare Function to generate random numbers
function getRandomPurchaseAmount(min1, max1) 
{
    return roundTo((Math.random() * (max1 - min1) + min), 2); 
}
//Declare function to round to what I want
function roundTo(n, digits) 
{
    if (digits === undefined) 
    {
      digits = 0;
    }
  
    var multiplicator = Math.pow(10, digits);
    n = parseFloat((n * multiplicator).toFixed(11));
    var test =(Math.round(n) / multiplicator);
    return +(test.toFixed(digits));
  }
//Declare Variables
const min = 100;
const max = 2000;
const purchase = getRandomPurchaseAmount(min, max);
let discount = 0;
//Let user know of purchase amount
console.log("The purchase amount came out to: $" + purchase);
//Discount code
if (purchase >= 1000) 
{
    discount = roundTo((0.2 * purchase),2);
}
else if (purchase >= 500 && purchase < 1000)
{
    discount = roundTo((0.1 * purchase),2);
}
else
{
    discount = 0;
}
//Print to user the discount amount
console.log('The discount amount is: $' + discount);
