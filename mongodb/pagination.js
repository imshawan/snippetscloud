
/**
 * @author Shawan Mandal
 * @function getArticlesWithPagination
 * @description Pagination example with mongoose that takes page number and no. of documents per page as params and returns the response based on that
 * @param {Object} req 
 * @param {Object} res 
 * @param {Mongoose schema} ArticleSchema
 * @returns JSON object of articles
 */
    
async function getArticlesWithPagination (req, res, ArticleSchema) {
    const fieldsToBeSearchedFor = [
        "title",
        "category",
        "authorName",
        "cover_image",
        "date",
        "slug",
      ] // The fields can be anything. 
        // They can be changed accordingly based on the schema and searching by this technique will give
        // you only the fields mentioned in the array.
    var page = parseInt(req.query.page) || 0; // Page number
    var limit =  parseInt(req.query.limitPostsBy) || 9; // Articles per page
    ArticleSchema.find({}, fieldsToBeSearchedFor)
      .sort({ date: -1 }) // Either ascending or descending order (1 or -1)
      .skip(page * limit)
      .limit(limit)
      .exec((err, records) => {
        if (err) {
          return res.status(400).json(err.message);
        }
        ArticleSchema.countDocuments({})
        .exec((err, count) => {
          res.status(200).json({
            articles: [records][0],
            total_pages: err ? 0 : Math.floor(count / limit),
            current_page: page,
            total_documents: records.length,
          });
        })
      });
  }