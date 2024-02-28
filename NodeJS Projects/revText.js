function reverseText(text)
{
    return text.split(" ").reverse().join(" ")
}
let testText = 'This is a test String'
let testText2 = 'This is a second String';
console.log(`Original Text:\n${testText} \n${testText2}`);
console.log(`Reversed Text:\n${reverseText(testText)} \n${reverseText(testText2)}`);
