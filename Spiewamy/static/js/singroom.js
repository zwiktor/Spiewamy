var url = window.location.pathname.split('/')
var user_url = url[2]
var api_url = "http://127.0.0.1:8000/api/" + user_url

function startSing () {

    const song_title = document.getElementById('song_title')
    const song_text = document.getElementById('song_text')

    setInterval(function () {
    fetch(api_url )
        .then(response => response.json())
        .then(data => {
            song_title.textContent = data.title
            song_text.textContent = data.text
        }).catch(function (error) {
            console.log(error)
    })
    }, 10000)


}

document.addEventListener('DOMContentLoaded', function() {
    startSing();
});
