const express = require("express");
const app = express();

app.listen(3000, function (req, res) {
  console.log("3000번 포트 실행");
});

app.get("/", function (req, res) {
  res.send("기본 페이지입니다.");
});
app.get("/idle", function (req, res) {
  res.send("여자 아이들 페이지 입니다.");
});

app.get("/miyeon", function (req, res) {
  res.send("미연 페이지 입니다.");
});
app.get("/minni", function (req, res) {
  res.send("민니 페이지 입니다.");
});
app.get("/sujin", function (req, res) {
  res.send("수진 페이지 입니다.");
});
app.get("/soyeon", function (req, res) {
  res.send("소연 페이지 입니다.");
});
app.get("/woogi", function (req, res) {
  res.send("우기 페이지 입니다.");
});
app.get("/soohwa", function (req, res) {
  res.send("수화 페이지 입니다.");
});
