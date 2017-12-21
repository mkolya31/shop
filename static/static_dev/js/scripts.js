$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log('123');
        var numb = $('#product_page_number').val();
        console.log(numb);
        var submite_btn = $('#product_submit_btn');
        var product_id = submite_btn.data("product_id");
        var product_name = submite_btn.data("product_name");
        var product_price = submite_btn.data("product_price");
        console.log(product_id);
        console.log(product_name);
        console.log(product_price);
    })
});