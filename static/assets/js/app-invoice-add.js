"use strict";
!function() {
    var e = document.querySelectorAll(".invoice-item-price")
      , t = document.querySelectorAll(".invoice-item-qty")
      , n = document.querySelectorAll(".date-picker");
    e && e.forEach(function(e) {
        new Cleave(e,{
            delimiter: "",
            numeral: !0
        })
    }),
    t && t.forEach(function(e) {
        new Cleave(e,{
            delimiter: "",
            numeral: !0
        })
    }),
    n && n.forEach(function(e) {
        e.flatpickr({
            monthSelectorType: "static"
        })
    })
}(),
$(function() {
    var n, o, a, i, l, r, e = $(".btn-apply-changes"), t = $(".source-item"), c = {
        "App Design": "Designed UI kit & app pages.",
        "App Customization": "Customization & Bug Fixes.",
        "ABC Template": "Bootstrap 4 admin template.",
        "App Development": "Native App Development."
    };
    function p(e, t) {
        e.closest(".repeater-wrapper").find(t).text(e.val())
    }
    $(document).on("click", ".tax-select", function(e) {
        e.stopPropagation()
    }),
    e.length && $(document).on("click", ".btn-apply-changes", function(e) {
        var t = $(this);
        l = t.closest(".dropdown-menu").find("#taxInput1"),
        r = t.closest(".dropdown-menu").find("#taxInput2"),
        i = t.closest(".dropdown-menu").find("#discountInput"),
        o = t.closest(".repeater-wrapper").find(".tax-1"),
        a = t.closest(".repeater-wrapper").find(".tax-2"),
        n = $(".discount"),
        null !== l.val() && p(l, o),
        null !== r.val() && p(r, a),
        i.val().length && t.closest(".repeater-wrapper").find(n).text(i.val() + "%")
    }),
    t.length && (t.on("submit", function(e) {
        e.preventDefault()
    }),
    t.repeater({
        show: function() {
            $(this).slideDown(),
            [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]')).map(function(e) {
                return new bootstrap.Tooltip(e)
            })
        },
        hide: function(e) {
            $(this).slideUp()
        }
    })),
    $(document).on("change", ".item-details", function() {
        var e = $(this)
          , t = c[e.val()];
        e.next("textarea").length ? e.next("textarea").val(t) : e.after('<textarea class="form-control" rows="2">' + t + "</textarea>")
    })
});
