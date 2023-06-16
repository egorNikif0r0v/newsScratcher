var XMLHttpRequest = require('xhr2')

let xhr = new XMLHttpRequest();
let url = "http://127.0.0.1:5000/ch_topic";
let data = JSON.stringify({topic: 'business/companies'});

xhr.open("POST", url, true);
xhr.setRequestHeader("Content-Type", "application/json");

xhr.onreadystatechange = function() {
    if(xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
    }
};
console.log(data)
xhr.send(data);