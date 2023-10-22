$(document).ready(function () {
    
    $('.increment-btn').click(function (e) { 
        e.preventDefault();
        
        var inc_val =$(this).closest('.product_data').find('.qty-input').val();
        var value =parseInt(inc_val,10);
        value = isNaN(value)? 0 : value;
        if(value < 6)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
});

$(document).ready(function () {
    
    $('.decrement-btn').click(function (e) { 
        e.preventDefault();
        
        var dec_val =$(this).closest('.product_data').find('.qty-input').val();
        var value =parseInt(dec_val,10);
        value = isNaN(value)? 0 : value;
        if(value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
});