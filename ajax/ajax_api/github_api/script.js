var cardDiv = document.querySelector(".container")
var username = "";

function getUsername(element) {
    console.log(element.value)
    username = element.value
}

function makeCard(data) {
    var card = `<div class="card"> 
                    <img src="${data.avatar_url}" alt="${data.login}">
                    <h3>Username: ${data.login}</h3>
                    <h3>${data.name} has ${data.followers} followers</h3>
                </div>`;
    return card;
}

async function getUserData() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch(`https://api.github.com/users/${username}`);
    // We then need to convert the data into JSON format.
    var userData = await response.json();
    console.log(userData);
    cardDiv.innerHTML = makeCard(userData) + cardDiv.innerHTML;
}
    

