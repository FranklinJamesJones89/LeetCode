const twoSum = (nums, target) => {
	let previousValues = {};

	for (let i = 0; i < nums.length; i++) {
		let currentNumber = nums[i];
		let neededValue = target - currentNumber;
		let index2 = previousValues[neededValue]
		if (index2 != null) {
			return [index2, i]
		} else {
			previousValues[currentNumber] = i;
		}		
	}
}

twoSum([2, 7, 11, 15], 9)

