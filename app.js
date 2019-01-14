const express = require('express')
const app = express()
var firebase = require('firebase/app');
require('firebase/auth');
require('firebase/database');
const port = 3000

const config = {
    apiKey: "AIzaSyAOiCp52hQICyWj1JMa_AHVzBaPvGFgmtQ",
    authDomain: "memento-sr.firebaseapp.com",
    databaseURL: "https://memento-sr.firebaseio.com",
    projectId: "memento-sr",
    storageBucket: "memento-sr.appspot.com",
    messagingSenderId: "210424874611"
  };
  firebase.initializeApp(config);
  var database = firebase.database()

app.use(express.urlencoded())
app.get('/', (req, res) => res.send('Hello World!'))

app.listen(port, () => console.log(`Example app listening on port ${port}!`))

app.get("/url2", (req, res, next) => {
    res.json(["Tony","Lisa","Michael","Ginger","Food"]);
   });


   app.post('/url', function (req, res) {
    res.send('POST request to homepage');
    const name = req.body.name
    firebase.database().ref("name").set(name);
  });

