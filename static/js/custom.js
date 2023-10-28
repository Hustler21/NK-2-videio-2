$(document).ready(function () {
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        
        var inc_val = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_val, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 6) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        
        var dec_val = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_val, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addToCartBtn').click(function (e) { 
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: "/addtocart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
            }
        });
    });

    $('.addToWishlist').click(function (e) { 
        e.preventDefault();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();

        $.ajax({
            type: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
            }
        });
    });

    $('.changeQuantity').click(function (e) { 
        e.preventDefault();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            type: "POST",
            url: "/update-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
            }
        });
    });

    $(document).on('click','.delete-wishlist-item', function (e) {
        e.preventDefault();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();

        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                console.log(response);
                alertify.success(response.status);
                $('.wishdata').load(location.href + " .wishdata"); // Added space before '.wishdata' to load the content correctly
            }
        });
    });

    

});
