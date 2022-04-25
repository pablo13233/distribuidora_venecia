
function newFunction() {
  var tablaProducto;
  var modalTitulo = $('.modal-title');
  window.onload = function () {

    //alert("Pagina cargada");
    $("#btnAdd").on("click", function () {
      modalTitulo.find('span').html('Crear producto');
      modalTitulo.find('i').removeClass().addClass('fas fa-plus');
      $('#action').val("crear");
      $('#form_producto')[0].reset();
      $('#descripcion').val("");
      $('#nombre').focus();

      $('#modalProducto').modal('show');
    });
    $('#datatable').DataTable();
    obtenerDatos();
  };
}

