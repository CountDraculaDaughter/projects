//Declare Variables
const total_seconds = 397985;
let hours = 0;
let remaining_seconds = 0;
let minutes = 0;
let seconds = 0;
//Calculate the times
hours = Math.floor(total_seconds / 3600);
remaining_seconds = total_seconds % 3600;
minutes = Math.floor(remaining_seconds / 60);
seconds = remaining_seconds % 60;
console.log("Number of hours: " + hours);
console.log("Number of minutes: " + minutes);
console.log("Number of seconds: " + seconds);
