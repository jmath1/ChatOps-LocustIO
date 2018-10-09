const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => res.send('Hello World!'))

app.get('/first-task', (req, res) => res.send("the first task is complete"))

app.get('/second-task', (req, res) => res.send("the second task is complete"))

app.get('/third-task', (req, res) => res.send("the third task is complete"))


app.listen(port, () => console.log(`Example app listening on port ${port}!`))
