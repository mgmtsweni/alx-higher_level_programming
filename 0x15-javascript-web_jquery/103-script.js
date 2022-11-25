"use strict";
("INPUT#language_code").keypress(function (e) {
    let key = e.which;
    if(key == 13) {translate();}
});

const translate = () => {
    const url = "https://fourtonfish.com";
    const script = $("INPUT#language_code").val();

    $.get(`${url}/hellosalut/?lang=${script}`, (data) => {
        $("DIV#hello").html(data.hello);
    });
};
