#!node

const fizzBuzz = (nums) => {
	for (i = 0; i < nums; i++) {
		if (i % 15 == 0) {
			console.log('fizzbuzz')
		}
		else if (i % 3 == 0) {
			console.log('fizz')
		} 
		else if (i % 5 == 0) {
			console.log('buzz')
		} 
		else {
			console.log(i)
		}
	}
};

fizzBuzz(100)
