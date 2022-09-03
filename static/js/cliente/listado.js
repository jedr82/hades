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
            {"data":"gender"},
            {"data":"id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/product/edit/'+row.id+'" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="/product/delete/'+row.id+'" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            
        }
    });
}

$(function () {
    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        //$('form')[0].reset();
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('shown.bs.modal', function () {
        $('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Desea confirmar la creación de un nuevo cliente?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
            //getData();
        });
    });
});