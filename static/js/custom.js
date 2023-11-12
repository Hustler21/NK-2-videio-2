$(document).ready(function(){
    $('.thumb a').click(function(e){
        e.preventDefault();
        $('.mainImage img').attr('src', $(this).attr("href"));
    })
})
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
                
                if (response.status) {
                    alertify.success(response.status);
                } else {
                    // Handle the case where there's an error message
                    alertify.error(response.status3);
                }
                
                
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
            success: function (responseb) {
                alertify.success(responseb.status);
                $('.wishdata').load(location.href + " .wishdata"); // Added space before '.wishdata' to load the content correctly
            }
        });
    });

    $(document).on('click','.delete-cart-item', function (e) {
        e.preventDefault();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        var product_id = $(this).closest('.product_data').find('.prod_id').val();

        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                
                alertify.success(response.status);
                $('.cartdata').load(location.href + " .cartdata"); // Added space before '.wishdata' to load the content correctly
            }
        });
    });

    

});
var chatButton = document.getElementById("startChatButton");
var isChatVisible = false



chatButton.addEventListener("click", function() {
    if (typeof Tawk_API !== 'undefined') {
        if (!isChatVisible) {
            Tawk_API.toggle();
        } else {
            Tawk_API.hideWidget();
        }
        isChatVisible = !isChatVisible;
    
    }
});
