let array = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'];
array.push('Thursday', 'Friday');
console.log(array);
array.splice(0,2);
console.log(array);
let sample = "";
for (let x = 0; x < array.length; x++)
{
    sample += x+1  + ') ' + array[x] + '\n';
}
console.log(sample);
array.splice(2,1);
let output = "";
for (let x = 0; x < array.length; x++)
{
    output += x+1  + ') ' + array[x] + '\n';
}
console.log(output);
