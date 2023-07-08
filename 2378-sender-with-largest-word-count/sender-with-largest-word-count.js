/**
 * @param {string[]} messages
 * @param {string[]} senders
 * @return {string}
 */
var largestWordCount = function(messages, senders) {
    const totals = new Map();
    for (let i = 0; i < messages.length; i++) {
        const words = messages[i].split(" ").length;
        totals.set(senders[i], (totals.get(senders[i]) || 0) + words);
    }
    let bestName = "";
    let bestCount = -1;
    for (const [name, count] of totals) {
        if (count > bestCount || (count === bestCount && name > bestName)) {
            bestCount = count;
            bestName = name;
        }
    }
    return bestName;
};