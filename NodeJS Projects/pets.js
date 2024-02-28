let myPets =
{
    pet1: 
    {
        name: 'Fluffy',
        color: 'orange',
        type: 'cat',
    },
    pet2:
    {
        name: 'Stuffy',
        color: 'white',
        type: 'hamster'
    },
    pet3:
    {
        name: 'Bluffy',
        color: 'brown',
        type: 'dog',
    },
};
let count = 0;
for (x in myPets)
{
    count += 1;
}
myPets.number = count
console.log(`I have ${myPets.number} pets. Their names are ${myPets.pet1.name}, \
${myPets.pet2.name} and ${myPets.pet3.name}.`);
console.log(`${myPets.pet1.name} is an ${myPets.pet1.color} ${myPets.pet1.type}, 
${myPets.pet2.name} is a ${myPets.pet2.color} ${myPets.pet2.type} and 
${myPets.pet3.name} is a ${myPets.pet3.color} ${myPets.pet3.type} `);
