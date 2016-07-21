/* global StripeCheckout, $ */

$().ready(function() {
    "use strict";

    var donate_modal = $("#donate-modal");
    var donate_dialog = $("#donate-dialog");
    var donate_form = $("#donate-form");
    var donate_currency = donate_form.data("currency");
    var donate_symbol = donate_form.data("symbol");
    var donate_amount = donate_form.find("input[name='amount']");
    var donation_complete_form = $("#donation-complete-form");
    var stripe_handler;
    var stripe_load;

    var stripe_open = {
        "name": "T1International",
        "image": donate_form.data("image"),
        "billingAddress": true,
        "shippingAddress": false
    };

    var configure_stripe_handler = function(public_key) {
        stripe_handler = StripeCheckout.configure({
            key: public_key,
            token: function(token) {
                // Submit the form to process the transaction on our server
                donation_complete_form.find("input[name='token']").val(token.id);
                donation_complete_form.find("input[name='email']").val(token.email);
                donation_complete_form.submit();
            }
        });
    };

    donate_modal.on("show.bs.modal", function(event) {
        var target = $(event.relatedTarget);
        var amount = target.data("amount");

        if (amount === undefined) {
            amount = 20;
        }

        $("#id_amount").val(amount);

        // Load Stripe as late as possible
        if (stripe_load === undefined) {
            stripe_load = $.ajax({
                url: "https://checkout.stripe.com/checkout.js",
                dataType: "script",
                cache: true
            });
            stripe_load.done(function() {
                var public_key = donate_form.data("stripe");
                configure_stripe_handler(public_key);
                donate_dialog.removeClass("hidden");
            });
        }
    });

    $("#donate-form").on("click", ".donate-onetime", function(event) {
        event.preventDefault();

        var complete_url = $(this).data("url");
        var donate_pounds = parseInt(donate_amount.val(), 10);
        var donate_pence = donate_pounds * 100;

        donation_complete_form.attr("action", complete_url);
        donation_complete_form.find("input[name='amount']").val(donate_pounds);

        // Setup a one time donation
        var donate_stripe_open = $.extend({}, stripe_open, {
             "description": "Donation - " + donate_symbol + donate_pounds,
             "amount": donate_pence,
             "currency": donate_currency
        });

        donate_modal.modal("hide");
        stripe_handler.open(donate_stripe_open);
    });

    $("#donate-form").on("click", ".donate-monthly", function(event) {
        event.preventDefault();

        var complete_url = $(this).data("url");
        var donate_pounds = parseInt(donate_amount.val(), 10);

        donation_complete_form.attr("action", complete_url);
        donation_complete_form.find("input[name='amount']").val(donate_pounds);

        // Setup a recurring monthly payment
        var donate_stripe_open = $.extend({}, stripe_open, {
             "description": donate_symbol + donate_pounds + " Monthly Donation",
             "panelLabel": "Subscribe"
        });

        donate_modal.modal("hide");
        stripe_handler.open(donate_stripe_open);
    });
});
