/**
 * @function isHTML
 * @description Check if the supplied string is HTML
 * @param {String} str 
 * @returns Boolean
 */
function isHTML (str) {

    try {
        const fragment = document.createRange().createContextualFragment(str);
        fragment.querySelectorAll('*').forEach(el => el.parentNode.removeChild(el));
        return !(fragment.textContent || '').trim();
    } catch (error) {
        console.log(error);
       return false;
    }
};

/**
 * @function htmlToString
 * @description Converts HTML to string
 * @param {String} str 
 * @returns String
 */
function htmlToString (string="") {
   let data = string;
   data = data.replace(/\n/gi, "");
   data = data.replace(/<style([\s\S]*?)<\/style>/gi, "");
   data = data.replace(/<script([\s\S]*?)<\/script>/gi, "");
   data = data.replace(/<a.*?href="(.*?)[\?\"].*?>(.*?)<\/a.*?>/gi, " $2 $1 ");
   data = data.replace(/<\/div>/gi, "\n\n");
   data = data.replace(/<\/li>/gi, "\n");
   data = data.replace(/<li.*?>/gi, "  *  ");
   data = data.replace(/<\/ul>/gi, "\n\n");
   data = data.replace(/<\/p>/gi, "\n\n");
   data = data.replace(/<br\s*[\/]?>/gi, "\n");
   data = data.replace(/<[^>]+>/gi, "");
   data = data.replace(/^\s*/gim, "");
   data = data.replace(/ ,/gi, ",");
   data = data.replace(/ +/gi, " ");
   data = data.replace(/\n+/gi, "\n\n");
   return data;
 };