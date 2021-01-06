// select
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll("select");
  var instances = M.FormSelect.init(elems, {});
});

// back button
document.getElementById("back-btn").onclick((e) => {
  history.back();
});

// download file automaticlly
/*
setTimeout((e) => {
  document.getElementById("download-file").click();
  setTimeout((e) => {
    window.location.href = window.location.origin;
  }, 1500);
}, 3000);
*/
