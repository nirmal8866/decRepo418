/** @odoo-module **/

    import core from "@web/legacy/js/services/core";
    var QWeb = core.qweb;
    import ajax from "@web/legacy/js/core/ajax";
    console.log("---------------ajax-----------------",ajax)

    $('body').ready(function () {
        console.log("--------------this----",this)
            ajax.rpc('/screenshot/feedback/get', 'call', {}).then(function(screenshot_data){
                if(screenshot_data.enable){
                    $("<link/>", {
                        rel: "stylesheet",
                        type: "text/css",
                        href: "/geminate_screenshot_feedback_send_all/static/src/lib/feedback/feedback.css"
                     }).appendTo("head");
                     $.when(
                        $.getScript( "/geminate_screenshot_feedback_send_all/static/src/lib/es6-promise/es6-promise.auto.js" ),
                        $.getScript( "/geminate_screenshot_feedback_send_all/static/src/lib/feedback/feedback.js" ),
                        $.Deferred(function( deferred ){
                            $( deferred.resolve );
                        })
                    ).done(function(){
                        let description = $(QWeb.render('geminate_feedback_welcome', screenshot_data.detail));
                        let highlighter = $(QWeb.render('geminate_feedback_highlighter', screenshot_data.detail));
                        let overview = $(QWeb.render('geminate_feedback_overview', screenshot_data.detail));
                        let submitSuccess = $(QWeb.render('geminate_feedback_submit_success', screenshot_data.detail));
                        let submitError = $(QWeb.render('geminate_feedback_submit_error', screenshot_data.detail));
                        $('body').append('<div id="screenshot-feedback-btn" class="fa fa-comments-o"/>');
                        $.feedback({
                            ajaxURL: "/screenshot/feedback/set",
                            html2canvasURL: "/geminate_screenshot_feedback_send_all/static/src/lib/html2canvas/html2canvas.min.js",
                            feedbackButton: "#screenshot-feedback-btn",
                            initButtonText: "Send feedback",
                            postHTML: screenshot_data.post_html,
                            imageTimeout: screenshot_data.image_timeout,
                            tpl: {
                                description: description.html(),
                                highlighter: highlighter.html(),
                                overview:overview.html(),
                                submitSuccess:submitSuccess.html(),
                                submitError: submitError.html()
                            },
                            initialBox: screenshot_data.initial_box
                        });
                        
                    });
                }
            });    
    }); 
