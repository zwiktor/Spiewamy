function checkIfUserExist() {
    var inputUsername = document.getElementById('userInput').value
    var buttonValue = document.getElementById('checkUser')
    var urlUsers = "http://127.0.0.1:8000/api/all/users?format=json"
    var usernameList = []

    fetch(urlUsers)
        .then(response => response.json())
        .then(data => {
            for(var username of data) {
                usernameList.push(username.username)
            }
            var userExists = usernameList.includes(inputUsername)
            if(userExists != true) {
                alert("Niema takiego użytkownika")
                window.location.replace("http://127.0.0.1:8000");
            }

        }).catch(function (error) {
            console.log(error)
    })


}