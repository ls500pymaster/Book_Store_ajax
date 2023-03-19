$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-author .modal-content").html("");
        $("#modal-author").modal("show");
      },
      success: function (data) {
        $("#modal-author .modal-content").html(data.html_form);
      }
    });
  };

  /* Save form */
  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $("#author-table tbody").html(data.html_author_list);
          $("#modal-author").modal("hide");
        }
        else {
          $("#modal-author .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create author
  $(".js-author-create-form").click(loadForm);
  //
  $("#modal-author").on("submit", ".js-author-create-form", saveForm);

  // Update author
  $("#author-table").on("click", ".js-update-author", loadForm);
  $("#modal-author").on("submit", ".js-author-update-form", saveForm);

  // Delete author
  $("#author-table").on("click", ".js-delete-author", loadForm);
  $("#modal-author").on("submit", ".js-author-delete-form", saveForm);

});