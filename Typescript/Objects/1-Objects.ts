// alwayes a type can be defined like this
type Person = {name:string,age:number | undefined}
function printInfo(person : Person){
    console.log(`Hi ${person.name} , your age is ${person.age}`)
}

printInfo({name:"Heisam",age:34})