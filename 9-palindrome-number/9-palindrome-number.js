/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let reverseNumber = Number(x.toString().split('').reverse().join(''))
    if (reverseNumber === x) {
        return true
    }
    
    return false
    
};