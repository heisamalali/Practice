// we only can return undefined in void functions and
// if we don't return void it will be returned as default
function printName(name:string):void{
    console.log(name.toUpperCase())
    return undefined
}

// function with never return will return nothing and the code will never reach the end
function printAnotherName(name:string):never{
    throw new Error(name)
}