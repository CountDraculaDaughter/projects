let person = 
{
    name: 'Alice',
    age: 25,
    job: 'dentist',
    sport: 'tennis',
    hobby: ['cooking', 'photography'],
};
console.log(person);
person.gender = 'female'
person.age = 31;
person['age'];
for (x in person)
{
    console.log(x);
}
for (let y in person)
{
    if(person[y] === 'tennis')
    {
        delete person[y];
    }
} 
let personkey = Object.keys(person);
personkey.forEach(function(keys)
{
    console.log(keys, ':',person[keys]);
});
let personAttributes = Object.values(person);
for (x in personkey)
{
    console.log(personkey[x]);
    console.log(personAttributes[x]);
}
