

axios.get('https://api.github.com/users/grabowski74')
    .then(function(response) {
        console.log(response.data.login);
    })
    .catch(function(error) {
        console.warn(error);
    });