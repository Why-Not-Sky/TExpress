type="text/javascript">jQuery(document).ready(function () {
!function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    p = /^http:/.test(d.location) ? 'http' : 'https';
    if (!d.getElementById(id)) {
        js = d.createElement(s);
        js.id = id;
        js.src = p + '://platform.twitter.com/widgets.js';
        fjs.parentNode.insertBefore(js, fjs);

    }
}
(document, "script", "twitter-wjs");

$("#file-id3").fileinput({
	previewFileType: "image",
	browseClass: "btn btn-success",
	browseLabel: "Pick Image",
	browseIcon: '<i class="glyphicon glyphicon-picture"></i>',
	removeClass: "btn btn-danger",
	removeLabel: "Delete",
	removeIcon: '<i class="glyphicon glyphicon-trash"></i>',
	uploadClass: "btn btn-info",
	uploadLabel: "Upload",
	uploadIcon: '<i class="glyphicon glyphicon-upload"></i>',
    uploadUrl: "http://127.0.0.1:5001/",
    uploadAsync: false,
});

$("#file-id").fileinput({
    browseClass: "btn btn-success",
    removeClass: "btn btn-danger",
    uploadClass: "btn btn-info",
    uploadUrl: "http://127.0.0.1:5001/",
    uploadAsync: false,
    layoutTemplates: {
        main1:
        "<div class=\'input-group {class}\'>\n" +
        "   <div class=\'input-group-btn\'>\n" +
        "       {browse}\n" +
        "       {upload}\n" +
        "       {remove}\n" +
        "   </div>\n" +
        "   {caption}\n" +
        "</div>\n" +  "{preview}"
    }
});

$(function () {
    $("[data-toggle=\'tooltip\']").tooltip();
});;
$(function () {
    $("[data-toggle=\'popover\']").popover();
});
$('body').on('click', function (e) {
    //did not click a popover toggle or popover
    if ($(e.target).data('toggle') !== 'popover'
        && $(e.target).parents('.popover.in').length === 0) {
        $('[data-toggle="popover"]').popover('hide');
    }
});
setTimeout(function() {
    $('.kv-webtips').removeClass('kv-animated-bell').addClass('kv-animated-bell');
}, 3000);
});
