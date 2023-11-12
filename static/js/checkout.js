$(document).ready(function () {

    $('.paywithRazorpay').click(function (e) { 
        e.preventDefault();
        
        // Get form field values
        var fname     = $("[name='fname']").val();     
        var lname     = $("[name='lname']").val();
        var email     = $("[name='email']").val();
        var phone     = $("[name='phone']").val();
        var address   = $("[name='address']").val();
        var city      = $("[name='city']").val();
        var state     = $("[name='state']").val();
        var country   = $("[name='country']").val();
        var pincode   = $("[name='pincode']").val();
        var token     = $('input[name=csrfmiddlewaretoken]').val();

        // Check if any of the required fields are empty
        if (
            fname == "" ||
            lname == "" ||
            email == "" ||
            phone == "" ||
            address == "" ||
            city == "" ||
            state == "" ||
            country == "" ||
            pincode == ""
        ) {
            alertify.error("All fields are mandatory");
            return false;
        } 
        else {
            // Proceed with Razorpay payment
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                success: function (response) {
                    var options = {
                        "key": "rzp_test_rcizbxE9fAdTp9",
                        "amount" : response.cart_total_price * 100,
                        "name": "N K COLLECTIONS",
                        "description": "Thank you for the awesome purchase",
                        "handler": function (responseb) {
                            // Prepare data for the POST request
                             data = {
                                "fname" : fname,
                                "lname" : lname,
                                "email" : email,
                                "phone" : phone,
                                "address" : address,
                                "city" : city,
                                "state" : state,
                                "country" : country,
                                "pincode" : pincode,
                                "payment_mode": "Paid with Razorpay",
                                "payment_id" : responseb.razorpay_payment_id,
                                csrfmiddlewaretoken: token,
                            };

                            // Make a POST request to place the order
                            $.ajax({
                                method: "POST",
                                url: "/place-order",
                                data: data,
                                success: function (responsec) {
                                    swal("Hifi !", responsec.status, "success").then((value) => {
                                        window.location.href = '/';
                                    });
                                }
                            });
                        },
                        "prefill": {
                            "name": fname + " " + lname,
                            "email": email,
                            "contact": phone
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });
        }
    });
});
