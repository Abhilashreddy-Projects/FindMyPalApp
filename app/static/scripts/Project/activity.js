var currentUrl = window.location.href;

var url = currentUrl.split('?');
var user_id = url[1].split('=');

var uid = user_id[1];


// Initialize Firebase
var config = {
    apiKey: "AIzaSyD8_nEsadS4xowGxBSAzipb5r1uqRiu6V4",
    authDomain: "dev-findmypal.firebaseapp.com",
    databaseURL: "https://dev-findmypal.firebaseio.com",
    projectId: "dev-findmypal",
    storageBucket: "dev-findmypal.appspot.com",
    messagingSenderId: "116241201934"
};

firebase.initializeApp(config);
