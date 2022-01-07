/**
 * @author Shawan Mandal
 * @function timeSince
 * @description Returns a string based on the timestamp supplied as the function parameter. e.g. "6 hours ago"
 * @param {longInt} timestamp Date.now()
 * @returns string
 */
 function timeSince(timestamp) {
    let date = new Date(timestamp);
    const seconds = Math.floor((Date.now() - date.getTime()) / 1000);
    if (!seconds) return "Just now";
    if (seconds < 0) return "Undefined";

    const interval = intervals.find(i => i.seconds < seconds);
    const count = Math.floor(seconds / interval.seconds);
    return `${count} ${interval.label}${count !== 1 ? 's' : ''} ago`;
}

const intervals = [
    { label: 'year', seconds: 31536000 },
    { label: 'month', seconds: 2592000 },
    { label: 'day', seconds: 86400 },
    { label: 'hour', seconds: 3600 },
    { label: 'minute', seconds: 60 },
    { label: 'second', seconds: 1 }
  ];