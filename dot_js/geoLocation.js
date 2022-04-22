var getPosition = function (options) {
    return new Promise(function (resolve, reject) {
      navigator.geolocation.getCurrentPosition(resolve, reject, options);
    });
  }
  
  getPosition()
    .then((position) => {
      console.log(position);
    })
    .catch((err) => {
  
      console.error(err);
    });
  