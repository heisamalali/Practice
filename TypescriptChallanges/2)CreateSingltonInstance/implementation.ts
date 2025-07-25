class Singleton {
    private static instance:Singleton;

    private constructor() {
    }

    public static getInstance() : Singleton{
        if(!Singleton.instance){
            Singleton.instance = new Singleton()
        }
        return Singleton.instance
    }
}

const singletonA = Singleton.getInstance()
const  singletonB = Singleton.getInstance()

console.log(singletonA === singletonB)