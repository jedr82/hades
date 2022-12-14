var vents = {
    items: {
        cli: '',
        date_joined: '',
        subtotal: 0.00,
        iva: 0.00,
        total: 0.00,
        products : []
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.products, function (pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            subtotal += dict.subtotal;
        });

        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function (item) {
        this.items.products.push(item);
        this.list();
    },
    list: function () {
        this.calculate_invoice();
        $('#tblProducts').DataTable({
            searching: false,
            paging: false,
            responsive: true,
            autoWidth: false,
            destroy: true,
            deferRender: true,
            data: this.items.products,
            columns: [
                {'data':'id'},
                {'data':'name'},
                {'data':'cate.name'},
                {'data':'pvp'},
                {'data':'cant'},
                {'data':'subtotal'},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data,type,row) {
                        return '<a rel="remove" class="btn btn-danger  btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3, -1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data,type,row) {
                        return 'Gs '+parseFloat(data).toLocaleString();
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data,type,row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm" autocomplete="off" value="'+row.cant+'">';
                    }
                },
            ],
            initComplete: function (settings, json) {

            }
        });
    },
};



$(function () {
    $('.select2').select2({
        theme: 'bootstrap4',
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format('YYYY-MM-DD'),
        locale: 'es'
    });

    $('input[name="iva"]').TouchSpin({
        min: 0,
        max: 100,
        step: 0.01,
        decimals: 2,
        bootstat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function () {
        vents.calculate_invoice();
    }).val(0.1);

    //Search products
    /*$('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {

            }).always(function (data) {

            });
        },
        minLength: 3,
        select: function(event,ui) {
            event.preventDefault();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            vents.add(ui.item);
            console.log(vents.items);
            $(this).val('');
        }
    });*/

    $('select[name="searchP"]').select2({
        theme: 'bootstrap4',
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type. 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_products'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripci??n',
        minimumInputLength: 1,
    }).on('select2:select2', function (e) {
        var data = e.params.data;
        data.cant = 1;
        data.subtotal = 0.00;
        vents.add(data);
    });
});