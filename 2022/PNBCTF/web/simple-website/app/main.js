// made with express js!!!
const express = require("express"); 
const fs = require("fs");

const app = express();
const PORT = process.env.PORT;

app.use((req, res, next) => {
    if ([req.body, req.headers, req.query].some(
        (item) => item && JSON.stringify(item).includes("flag")
    )) {
        return res.send("try again!");
    }
    next();
});

app.get("/", (req, res) => {
    try {
        res.setHeader("Content-Type", "text/html");
        res.send(fs.readFileSync(req.query.file || "index.html").toString());

    }
    catch (err) {
        console.log(err);
        res.status(500).send("Internal server error");
    }
});
app.listen(PORT, () => console.log(`web/mysimplewebsite listening on port http://localhost:${PORT}`));