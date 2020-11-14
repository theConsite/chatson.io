function encryption(mess, key) {
  return CryptoJS.AES.encrypt(mess, key);
}
function decryption(mess_ecrypted, key) {
  return CryptoJS.AES.decrypt(mess_ecrypted, key);
}
// load key from cookies
$("#key").text(getCookie("key_encryption"));

// new key for encryption
$("#send_key").click(function () {
  console.log("aaa");
  setCookie("key_encryption", $("#encrytp").val(), 2);
  $("#key").text(getCookie("key_encryption"));
});
// send and refresh chat
function send_and_refresh() {
  var jqxhr = $.getJSON("/chat_check", function () {})
    .done(function (data) {
      $("#chat_box").html("");
      $.each(data, function () {
        if (this.user == 1) {
          class_to = 'class="user2"';
        } else {
          class_to = 'class="user1"';
        }
        // console.log(decryption(this.mess, $("#key").text(CryptoJS.enc.Utf8)) )
        //  console.log(decryption(this.mess, $("#key").text()).toString(CryptoJS.enc.Utf8));
        // $("#chat_box").append("<p " + class_to + " > " + decryption(this.mess, $("#key").text()).toString(CryptoJS.enc.Utf8) + " </p>")
        if (this.mess == null) {
          console.log("null");
        } else {
          $("#chat_box").append(
            "<p " +
              class_to +
              " > " +
              decryption(this.mess, $("#key").text()).toString(
                CryptoJS.enc.Utf8
              ) +
              " </p>"
          );
        }
      });
    })
    .fail(function () {
      console.log("error");
    });

  setTimeout(send_and_refresh, 1000);
}
//   main form sending
$(document).ready(function () {
  $("form").submit(function () {
    var $input_mess = $(this).find("input[name=chat_mess]");
    var $input_encryption = $("#key").text();
    if (!$input_mess.val() || !$input_encryption) {
      alert("wypełnij oba pola");
    } else {
      // alert(encryption($input_mess.val(), $input_encryption).toString(),$input_encryption,$input_mess.val())
      $input_mess.val(
        encryption($input_mess.val(), $input_encryption).toString()
      );
    }
  });
  send_and_refresh();
});
