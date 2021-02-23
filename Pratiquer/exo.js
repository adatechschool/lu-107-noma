
class Pet{
    constructor(name, greeting="Hello"){
        this.name = name;
        this.greeting = greeting;
    }

    say_hi(){
        return console.log(this.greeting+" I'm " + this.name +"!")
    }
}
mypet = new Pet('Misolito');
mypet.say_hi();


class Cat extends Pet {
    constructor(name){
        super(name,"Meow");
    };
    legs_count(){
        return console.log('My number of legs is 4')
    }
    
}
mycat = new Cat('Leon')
mycat.say_hi();
mycat.legs_count();

class Parrot extends Pet {
    constructor(name){
        super(name,"Squawk");
    };
    legs_count(){
        return console.log('My number of legs is 2')
    }
    
}
myparrot = new Parrot('Telma')
myparrot.say_hi();
myparrot.legs_count();

