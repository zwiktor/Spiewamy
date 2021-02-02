var url = window.location.pathname.split('/')
const user_url = url[2]
var api_url = "http://127.0.0.1:8000/api/" + user_url
var btn_link = document.getElementById('link-songs')

function startSing () {

    const song_title = document.getElementById('song_title')
    const song_text = document.getElementById('song_text')

    setInterval(function () {
    fetch(api_url)
        .then(response => response.json())
        .then(data => {
            console.log(data.text)
            song_title.textContent = data.title
            //Tutaj trzeba zastosować funkcję edycji tekstu i wprowadzenie do diva we właściwym formacie

            song_text.innerHTML = data.text
        }).catch(function (error) {
            console.log(error)
    })
    }, 10000)


}

document.addEventListener('DOMContentLoaded', function() {
    startSing();
});



function converter_to_beautiful_text(text) {
    const text_converted = text.replaceAll('\r\n', '<br>')
    return(text_converted)
}


function increaseFontSize() {
    const song_text = document.getElementById('song_text')
    var fontSize = getComputedStyle(song_text).fontSize
    fontSize = fontSize.slice(0,2)
    fontSize = parseInt(fontSize)
    var newFontSize = fontSize + 1
    song_text.style.fontSize = '' + newFontSize + 'px'
}

function decreaseFontSize() {
    const song_text = document.getElementById('song_text')
    var fontSize = getComputedStyle(song_text).fontSize
    fontSize = fontSize.slice(0,2)
    fontSize = parseInt(fontSize)
    var newFontSize = fontSize - 1
    song_text.style.fontSize = '' + newFontSize + 'px'
}

btn_link.addEventListener("click", () => {
    var urlUserSongs = "http://127.0.0.1:8000/sing/" + user_url + "/songs"
    window.location.replace(urlUserSongs);
})

function sentToSingroom(user_url) {
    var urlUser = "http://127.0.0.1:8000/sing/" + (user_url)
    console.log(urlUser)
    window.location.replace(urlUser);
}