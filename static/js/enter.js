// listener for adding key session and user choice
$(document).ready(function () {
  $("#key").val(getCookie("key"));
  if (getCookie("user") == 1) {
    $("#user1").attr("checked", true);
  }
  if (getCookie("user") == 2) {
    $("#user2").attr("checked", true);
  }

  $("#button_send_data").click(function () {
    setCookie("key", $("#key").val(), 1);
    setCookie("user", $("input[name='user']:checked").val(), 2);
  });
});
