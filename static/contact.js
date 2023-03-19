$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-contact .modal-content").html("");
        $("#modal-contact").modal("show");
      },
      success: function (data) {
        $("#modal-contact .modal-content").html(data.html_form);
      }
    });
  };

  // Create author
  $(".js-contact-create-form").click(loadForm);
  //
  $("#modal-contact").on("submit", ".js-contact-create-form", saveForm);

  // Update author
  // $("#author-table").on("click", ".js-update-author", loadForm);
  // $("#modal-author").on("submit", ".js-author-update-form", saveForm);
  //
  // // Delete author
  // $("#author-table").on("click", ".js-delete-author", loadForm);
  // $("#modal-author").on("submit", ".js-author-delete-form", saveForm);

});