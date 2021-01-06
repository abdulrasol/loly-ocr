// action btn
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll(".fixed-action-btn");
  var instances = M.FloatingActionButton.init(elems, {
    direction: "top",
  });
});

// select
document.addEventListener("DOMContentLoaded", function () {
  var elems = document.querySelectorAll("select");
  var instances = M.FormSelect.init(elems, {});
});

// download file automaticlly
setTimeout((e) => {
  document.getElementById("download-file").click();
  setTimeout((e) => {
    window.location.href = window.location.origin;
  }, 1500);
}, 3000);
