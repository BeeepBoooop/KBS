function getBotResponse() {
  var rawText = $("#textInput").val();
  var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  var ok = 0
  document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
  $.get("/get", { message: rawText }).done(function (data) {
    $.each(data, function (e, name) {
      b = name + ""
      a = b.split(",")
      val = Number(a[1])
      console.log(val);
      if (val >= 60) {
        $("#userInput").hide()
        var botHtml = '<p class="botText"><span>' + "Bạn có thể đã bị " + a[0] + ", khả năng bị là " + a[1] + "%" + '</span></p>';
        var dieuchi = '<a id= "dieuchi" href="/dieuchi?linkdc=' + a[0] + '">' + "bạn có thể xem đề xuất điều trị tại đây điều trị" + '</a>'
        $("#chatbox").append(botHtml);
        $("#chatbox").append(dieuchi);
        document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
        ok = 1
      }
    })
    if (ok == 0) {
      $.each(data, function (e, name) {
        console.log(typeof value);
        b = name + ""
        a = b.split(",")
        val = Number(a[1])
        var botHtml = '<p class="botText"><span>' + "có thể bạn đã bị bệnh " + a[0] + '. Khả năng bị bệnh là ' + a[1] + "%" + '</span></p>';
        $("#chatbox").append(botHtml);
        document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
      });
      $.get("/getPropose", { message: rawText }).done(function (data) {
        var botHtml = '<p class="botText"><span>' + "Bạn có còn các triệu chứng hay tiền sử: " + data + ", hoặc triệu chứng khác không? Nếu không hãy chat: không còn triệu chứng" + '</span></p>';
        $("#chatbox").append(botHtml);
        document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
      });
    }
  });
}
$("#textInput").keypress(function (e) {
  if (e.which == 13) {

    var textUser = document.getElementById("textInput").value
    if (textUser == "không còn triệu chứng") {
      $("#userInput").hide()
      var rawText = $("#textInput").val();
      var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
      $("#textInput").val("");
      $("#chatbox").append(userHtml);
      $.get("/getResult", { message: rawText }).done(function (data) {
        var botHtml = '<p class="botText"><span>' + data + '</span></p>';
        $("#chatbox").append(botHtml);
        document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
      });
    }
    else {
      getBotResponse();
    }
  }
});
$("#buttonInput").click(function () {

  var textUser = document.getElementById("textInput").value
  if (textUser == "không còn triệu chứng") {
    $("#userInput").hide()
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + '</span></p>';
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    $.get("/getResult", { message: rawText }).done(function (data) {
      var botHtml = '<p class="botText"><span>' + data + '</span></p>';
      $("#chatbox").append(botHtml);
      document.getElementById('userInput').scrollIntoView({ block: 'start', behavior: 'smooth' });
    });
  }
  else {
    getBotResponse();
  }
})