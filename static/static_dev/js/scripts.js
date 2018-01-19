$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);

    function basketupdating(product_id, numb, is_delete) {
        var data = {};
        data.product_id = product_id;
        data.nmb = numb;
        var csrf_token = $('#form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        var url = form.attr("action");

        console.log(data);
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                console.log("OK");
                console.log(data.product_total_numb);
                if (data.product_total_numb) {
                    $('#product_total_numb').text("(" + data.product_total_numb + ")");
                    console.log(data.products);
                    $('.basket-items ul').html("");
                    $.each(data.products, function (k, v) {
                        $('.basket-items ul').append('<li><h6>' + v.name + ', ' + v.numb + 'шт. ' + 'по ' + v.price_per_item + ' руб  ' +
                            '<a class="delete-item" href="">x</a>' +
                            '</h6></li>');
                    })
                }
            },
            error: function () {
                console.log("ERROR")
            }
        });
    }

    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123rus');
        var numb = $('#product_page_number').val();
        console.log(numb);
        var submite_btn = $('#product_submit_btn');
        var product_id = submite_btn.data("product_id");
        var product_name = submite_btn.data("product_name");
        var product_price = submite_btn.data("product_price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);

        basketupdating(product_id, numb, is_delete=false)

    });
    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })
});