var url = window.location.pathname.split('/')
var user_url = url[2]
var api_url = "http://192.168.0.17:8000/api/" + user_url

function startSing () {

    const song_title = document.getElementById('song_title')
    const song_text = document.getElementById('song_text')

    setInterval(function () {
    fetch(api_url)
        .then(response => response.json())
        .then(data => {
            song_title.textContent = data.title
            converted_text = converter_to_beautiful_text(data.text)
            //Tutaj trzeba zastosować funkcję edycji tekstu i wprowadzenie do diva we właściwym formacie

            song_text.innerHTML = converted_text
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