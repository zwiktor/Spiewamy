function checkIfUserExist() {
    var inputUsername = document.getElementById('userInput').value
    var buttonValue = document.getElementById('checkUser')
    var urlUsers = "http://127.0.0.1:8000/api/all/users?format=json"
    var urlUser = "http://127.0.0.1:8000/api/"+ inputUsername
    var usernameList = []

    fetch(urlUser)
    .then(response => response.json())
    .then(data => {
        if(data.id === "-1") {
            alert("Użytkownik nie śpiewa")
            window.location.replace("http://127.0.0.1:8000");
        }

    }).catch(function (error) {
        console.log(error)
    })

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