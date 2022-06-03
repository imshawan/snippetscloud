/**
 * @author imshawan
 * @function removeDuplicates
 * @description Removes duplicates from an array of Objects
 * @param {array} array - Array of Objects
 * @param {string} key - Key to check for duplicates
 * @returns {Array}
 */

 function removeDuplicates (array, key) {
    let newArr = [];
    let uniqueElems = [];
    array.forEach(function (item) {
        if (!uniqueElems.includes(item[key])) {
            newArr.push(item);
            uniqueElems.push(item[key]);
        }
    })
    return newArr;
}