function shimeclick() {
    var shime = document.getElementById('shime');
    if (shime.innerHTML.trim() == 'Shime') {
        shime.innerHTML = 'Oye';
    } else if (shime.innerHTML.trim() == 'Oye'){
        shime.innerHTML =
            'Te adoro <span class="glyphicon glyphicon-heart"/>';
    } else {
        shime.innerHTML = 'Shime';
    }
}