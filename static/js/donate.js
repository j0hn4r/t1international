/* global StripeCheckout, $ */

$().ready(function() {
    "use strict";

    var donate_modal = $("#donate-modal");
    var donate_part1 = $("#donate-popup-1");
    var donate_part2 = $("#donate-popup-2");
    var paynow_button = $("#pay-now");
    var donation_complete_form = $("#donation-complete-form");
    var stripe_handler;
    var stripe_open;
    var stripe_load;

    var configure_stripe_handler = function(public_key) {
        stripe_handler = StripeCheckout.configure({
            key: public_key,
            token: function(token) {
                donation_complete_form.find("input[name='token']").val(token.id);
                donation_complete_form.find("input[name='email']").val(token.email);
                donation_complete_form.submit();
            }
        });
    };

    $("#donate-form").on("click", ".donate-button", function(event) {
        event.preventDefault();

        var url = $(this).data("url");
        var form_data = $(this).closest("form").serialize();

        var payment_request = $.ajax(url, {
            type: "POST",
            data: form_data,
            dataType: "json"
        });

        payment_request.done(function(data) {
            if (data.success === true) {
                donation_complete_form.attr("action", data.complete_url);
                donation_complete_form.find("input[name='obj']").val(data.id);
                donation_complete_form.find("input[name='secret_key']").val(data.secret_key);

                // Configure Stripe handler
                stripe_load.done(function() {
                    configure_stripe_handler(data.public_key);
                    stripe_open = data.stripe_open;

                    paynow_button.prop("disabled", false);
                });

                donate_part1.addClass("hidden");
                donate_part2.removeClass("hidden");
            } else if (data.success === false) {
                $("#donate-form").html(data.form);
            }
        });
    });

    donate_modal.on("show.bs.modal", function(event) {
        var target = $(event.relatedTarget);
        var amount = target.data("amount");

        if (amount !== undefined) {
            $("#id_amount").val(amount);
        }

        // Load Stripe as late as possible
        if (stripe_load === undefined) {
            stripe_load = $.ajax({
                url: "https://checkout.stripe.com/checkout.js",
                dataType: "script",
                cache: true
            });
        }

        // Reset any bits needed
        donate_part1.removeClass("hidden");
        donate_part2.addClass("hidden");
        paynow_button.prop("disabled", true);
    });

    paynow_button.on("click", function(event) {
        event.preventDefault();
        donate_modal.modal("hide");
        stripe_handler.open(stripe_open);
    });
});
