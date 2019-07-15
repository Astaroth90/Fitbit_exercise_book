/*
	
*/

export default class Plan {
	
	constructor(){
		this.exList = require("Collections/list");	
	}
	
	function addExercise(Exercises ex) {
		this.exList.push(ex);
	}
}