
// This javascript file is based on this tutorial: 'How to Implement CRUD Using Ajax and Json'
// https://simpleisbetterthancomplex.com/tutorial/2016/11/15/how-to-implement-a-crud-using-ajax-and-json.html
// Some code was changed to correspond to Definitions app.


$(function () {

  /* Functions */

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-term .modal-content").html("");
        $("#modal-term").modal("show");
      },
      success: function (data) {
        $("#modal-term .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          $(".defi-software-app").html(data.html_term_list);
          $("#modal-term").modal("hide");
        }
        else {
          $("#modal-term .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  /* Binding */

  // Create term
  $(".js-create-term").click(loadForm);
  $('#modal-term').on("submit", ".js-term-create-form", saveForm);

  // Update term
  $("#term-table").on("click", ".js-update-term", loadForm);
  $("#modal-term").on("submit", ".js-term-update-form", saveForm);

  // Delete term
  $("#term-table").on("click", ".js-delete-term", loadForm);
  $("#modal-term").on("submit", ".js-term-delete-form", saveForm);

});
