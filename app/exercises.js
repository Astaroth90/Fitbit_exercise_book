export default class Exercise {

    /*var name;
    var repeat;
    var weight;
    var sets;
    */
    constructor(name,repeat,weight, sets){
        this.name = name;
        this.repeat = repeat;
        this.weight = weight;
        this.sets = sets;
    }

    get Name(){
        return this.name;
    }
	
	get Repeat() {
		return this.repeat;
	}
	
	get Weight() {
		return this.weight;
	}
	
	get Sets() {
		return this.sets;
	}
}