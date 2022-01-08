
/**
 * 
 * @author Shawan Mandal
 * @function nestedIncrementCount
 * @description This function demonstrates how we can increment a value inside a nested mongodb document structure
 * @param {MongoDB Client} mongoClient
 * @param {Object} key => The keys to find the document for incrementing the count
 * @param {string} bookCategory => Category of the book for which the value should be incremented. (e.g physics || chemistry || botany)
 * @param {integer} value => Increment or decrement value. Pass 1 for increment and -1 for decrement
 * @param {Object} data => {userId, username} for registering the count information
 * @returns 
 */
async function nestedIncrementCount (mongoClient, key, bookCategory, value, data) {
    value = parseInt(value, 10);
    if (!key || isNaN(value)) {
        return null;
    }

    if (!await mongoClient.collection('collection_name').findOne(key, { 'booksCount': { $exists: false, $ne: null }})) {
        // If no property as booksCount, then add it
        await mongoClient.collection('collection_name').update(key, { $set:{ 'booksCount': [] } });
    }
    if (!await mongoClient.collection('collection_name').findOne({...key, 'booksCount': { $elemMatch: {'userId': data.userId} } })) {
        // If no record found for the current user, add a new one
        await mongoClient.collection('collection_name').update(key, { $push:{ 'booksCount': { ...data, 'count': [] } } });
    }
    if (!await mongoClient.collection('collection_name').findOne({...key, 
        'booksCount': { $elemMatch: {'userId':  data.userId, 'count': { $elemMatch: {'bookCategory': bookCategory} } } } })) { 
        // If record exists, but no property to hold increment count, add it
        await mongoClient.collection('collection_name').update({...key, 'booksCount': { $elemMatch: {'userId': data.userId} } }, 
        { $push: { 'booksCount.$.count': {
            'bookCategory': bookCategory,
            'totalCount': 0,
        } }})
    }
    await mongoClient.collection('collection_name').findOneAndUpdate(
      // Actual increment
        key,
        { $inc: {
            'booksCount.$[i].count.$[j].totalCount': value
        }},
        {arrayFilters: [ { 'i.userId': { $eq: data.userId } }, {'j.bookCategory': { $eq: bookCategory } } ]}
    )
}

// An example document for reference that visualizes the nested structure MongoDB document
let example = {
  // booksCount is an array on N number of elements
  booksCount: [
    {
      userId: Number, // Each individual user has a different Object that contains 
      // UserId, username, count (which is again an array that contains the actual counting data)
      username: String,
      count: [
      // count is an array on N number of elements
        {
          bookCategory: String,
          totalCount: Number // Increment must happen here
        },
        {
          bookCategory: String,
          totalCount: Number // Increment must happen here
        }
      ]
    },
    {
      userId: Number,
      username: String,
      count: [
        {
          bookCategory: String,
          totalCount: Number 
        },
        {
          bookCategory: String,
          totalCount: Number
        }
      ]
    }
  ]
}