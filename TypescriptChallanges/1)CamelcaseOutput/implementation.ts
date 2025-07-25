import * as readline from 'readline';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('Enter something: ', (answer: string) => {
  console.log(`You entered: ${answer}`);
  const inputAsArray : string[]  = answer.split(/[\s,-]+/)
  console.log(inputAsArray)
  let output = ''
  inputAsArray.forEach((value, index, array)=>{
    console.log(value)
    let temValue = value
    temValue = value.toLowerCase()
    output += value.charAt(0).toUpperCase() + temValue.slice(1)
  })
  console.log(output)
  rl.close();
});