/**
 * 
 * @date 03-06-2022
 * @function slugify
 * @description slugifies a string in JavaScript using a separator and returns the slugified string
 * @param {string} str 
 * @param {string} separator 
 * @returns String
 */

function slugify(str, separator='-') {
    str = str.replace(/^\s+|\s+$/g, '');
    str = str.toLowerCase();

    var from = "ÁÄÂÀÃÅČÇĆĎÉĚËÈÊẼĔȆÍÌÎÏŇÑÓÖÒÔÕØŘŔŠŤÚŮÜÙÛÝŸŽáäâàãåčçćďéěëèêẽĕȇíìîïňñóöòôõøðřŕšťúůüùûýÿžþÞĐđßÆa·/_,:;";
    var to   = "AAAAAACCCDEEEEEEEEIIIINNOOOOOORRSTUUUUUYYZaaaaaacccdeeeeeeeeiiiinnooooooorrstuuuuuyyzbBDdBAa------";
    for (var i=0, l=from.length ; i<l ; i++) {
        str = str.replace(new RegExp(from.charAt(i), 'g'), to.charAt(i));
    }

    // Remove invalid chars, Collapse whitespace and replace by separator
    return str.replace(/[^a-z0-9 -]/g, '') .replace(/\s+/g, separator).replace(/-+/g, separator); 
}