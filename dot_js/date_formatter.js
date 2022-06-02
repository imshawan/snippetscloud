/**
 * @date 26-05-2022
 * @author imshawan
 * @param {Object} data { timestamp: timestamp, datetime: Boolean} 
 * @returns Formatted DateTime
 */

 function dateFormatter (data = {}) {
    let date = new Date(data.timestamp)
    let time = date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true })
    return `${date.getDate()} ${date.toLocaleDateString(undefined, { month: "long" })}, ${date.getFullYear()} ${data.datetime ? `, ${time}` : ''}`
}