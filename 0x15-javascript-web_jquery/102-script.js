"use strict";
$("INPUT#btn_translate").click(() => {
    const url = "https://fourtonfish.com";
    const script = $("INPUT#language_code").val();

    $.get(`${url}/hellosalut/?lang=${script}`, (data) => {
      $("DIV#hello").html(data.hello);
    });
  });
  