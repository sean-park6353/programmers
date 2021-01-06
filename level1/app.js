const express = require('express')
const app = express()
app.listen(3000, () => { console.log(`3000번 포트에 접속 완료`) })
app.get('/', (req, res) => {
    res.send("안녕하세요")
})