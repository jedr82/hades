var tblClient;

function getData() {
    tblClient = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchData'
            },
            dataSrc: ""
        },
        columns: [
            {"data":"id"},
            {"data":"names"},
            {"data":"surnames"},
            {"data":"dni"},
            {"data":"address"},
            {"data":"date_birthday"},
            {"data":"gender.name"},
            {"data":"id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat btnEdit"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" class="btn btn-danger btn-xs btn-flat btnDelete"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            
        }
    });
}

$(function () {
    modal_title = $('.modal-title');

    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        $('#formCliente')[0].reset();
        $('#myModalClient').modal('show');
    });

    $('#data tbody')
    .on('click', '.btnEdit', function () {
        modal_title.find('span').html('Edición de un cliente');
        modal_title.find('i').removeClass().addClass('fas fa-edit');
        var tr = tblClient.cell($(this).closest('td,li')).index();
        var data = tblClient.row(tr.row).data();

        console.log(data);
        $('input[name="action"]').val('edit');
        $('input[name="id"]').val(data.id);
        $('input[name="names"]').val(data.names);
        $('input[name="surnames"]').val(data.surnames);
        $('input[name="dni"]').val(data.dni);
        $('input[name="address"]').val(data.address);
        $('input[name="date_birthday"]').val(data.date_birthday);
        $('select[name="gender"]').val(data.gender.id);
        $('#myModalClient').modal('show');
    }).on('click', '.btnDelete', function () {
        var tr = tblClient.cell($(this).closest('td,li')).index();
        var data = tblClient.row(tr.row).data();
        var parameters = new FormData();
        parameters.append('action','delete');
        parameters.append('id', data.id);

        submit_with_ajax(window.location.pathname, 'Notificación', '¿Desea confirmar la eliminación de un nuevo cliente?', parameters, function () {
            tblClient.ajax.reload();
        });
    });

    $('.btnUpd').on('click', function () {
        tblClient.ajax.reload();
        //getData();
    });

    $('#myModalClient').on('shown.bs.modal', function () {
        //$('#formCliente')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData($('#formCliente')[0]);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Desea confirmar la creación de un nuevo cliente?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
            //getData();
        });
    });
});