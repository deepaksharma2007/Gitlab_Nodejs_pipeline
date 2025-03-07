const express = require("express")

const app = express ()

function lw(req, res){
res.send ("welcome to deepak home")
console. log("client connected on page data .... ")
}

app.get("/data", lw )
app.listen(3000)
