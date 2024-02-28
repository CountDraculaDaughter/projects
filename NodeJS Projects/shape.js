let today = new Date();
let shape = 
{
    name: 'circle',
    radius: 3.16,
    area: 
    function()
    {
        return Math.PI * Math.pow(this.radius, 2);
    },
};
let capacity =
{
    name: 'cube',
    side: 10,
    volume: 
    function()
    {
        return Math.pow(this.side, 3);
    },
};
let pet = 
{
    type: 'cat',
    name: 'Fluffy',
    year: 2022,
    age: 
    function()
    {
        return today.getFullYear() - 2022
    },
};
console.log(`The ${shape.name} has an area of ${shape.area()}`);
console.log(`The ${capacity.name} has a volume of ${capacity.volume()}`);
console.log(`This year my ${pet.type} ${pet.name} is ${pet.age()} years old` );
