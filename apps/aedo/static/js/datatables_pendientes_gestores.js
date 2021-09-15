    let table = $('#datatables').DataTable({
        language: {
            "sProcessing":     "Procesando...",
            "sLengthMenu":     "Mostrar _MENU_ registros",
            "sZeroRecords":    "No se encontraron resultados",
            "sEmptyTable":     "No tiene entregas pendientes",
            "sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix":    "",
            "sSearch":         "",
            "sSearchPlaceholder": "Buscar...",
            "sUrl":            "",
            "sInfoThousands":  ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst":    "Primero",
                "sLast":     "Último",
                "sNext":     "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
        "ordering": false,
        "ajax": {
            "url": "/api/pending-deliveries/",
            "type": "GET",
            "beforeSend": function (request) {
                const $csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value;
                  request.setRequestHeader("X-CSRFToken", $csrf_token );
              },
            "dataSrc": ""
        },
        "columns": [

            {"data": "id", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "ID" );
                }
            },
            {"data": "company", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Cliente" );
                }
            },
            {"data": "package", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Paquete" );
                }
            },
            {"data": "origin_address", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Origen" );
                }
            },
            {"data": "destination_address", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Destino" );
                }
            },
            {"data": "reception_date", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Retirar" );
                }
            },
            {"data": "deliver_date", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Entregar" );
                }
            },
            {"data": "employee_amount", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Comision" );
                }
            },
            {"data": "pending", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Cobrar" );
                }
            },
            {"data": "state", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Estado" );
                }
            },
            {"data": "comment", createdCell: function (td, cellData, rowData, row, col) {
                    $(td).attr( "title", "Observaciones" );
                }
            },
            {"data": "action",render: function(data, type) {                     
                    return data;
                }
            }
        ]
    });

