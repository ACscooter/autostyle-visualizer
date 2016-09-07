// js file for scripts
// Created 9/6/16

function renderLeftBar(url) {
    $.getJSON(url, function(data) {
        $("#scroll-display-left").empty()
        $.each(data["names"], function(index, value) {
            var p = $("<p><a></a></p>");
            $("#scroll-display-left").append(p)
            $("a", p).text(value);
            $("a", p).attr("href", "/" + value + "/");
        });
    })
}

function showAssignments() {
    $.getJSON("/assignments/", function(data) {
        $("#scroll-display-left").empty()
        $.each(data["names"], function(index, value) {
            var p = $("<p><a></a></p>");
            $("#scroll-display-left").append(p)
            $("a", p).text(value);
            $("a", p).attr("href", "#");
            $("a", p).click(function() {
                selectAssignment(value);
            });
        });
    });
}

function showStudents() {
    $.getJSON("/sids/", function(data) {
        $("#scroll-display-left").empty()
        $.each(data["names"], function(index, value) {
            var p = $("<p><a></a></p>");
            $("#scroll-display-left").append(p)
            $("a", p).text(value);
            $("a", p).attr("href", "#");
            $("a", p).click(function() {
                selectSid(value);
            });
        });
    });
}

function selectSid(sid) {
    $.getJSON("/" + sid + "/" + "submissions" + "/", function(data) {
        $("#scroll-display-right").empty()
        var h3 = $("<h3>" + "SID: " + sid + "</h3>");
        var hr = $("<hr>");
        $("#scroll-display-right").append(h3)
        $("#scroll-display-right").append(hr)
        $.each(data, function(func_name, array) {
            var h3 = $("<h3>" + func_name + "</h3>");
            var br = $("<br>");
            $("#scroll-display-right").append(br);
            $("#scroll-display-right").append(h3);
            $("#scroll-display-right").append(br);
            $.each(array, function(index, value) {
                var div = $("<div></div>");
                var br = $("<br>");
                $("#scroll-display-right").append(div);
                $("#scroll-display-right").append(br);
                $("#scroll-display-right").append(br);
                var p = $("<p> code: </p>");
                var h5 = $("<h5>" + value["timestamp"] + "</h5>");
                var p1 = $("<pre>" + value["code"] + "</pre>");
                var p2 = $("<p>" + "correct: " + value["correct"] + "</p>");
                var p3 = $("<p>" + "cluster: " + value["cluster"] + "</p>");
                var p5 = $("<p>" + "style score: " + value["style_score"] + "</p>");
                $(div).append(h5);
                $(div).append(p);
                $(div).append(p1);
                $(div).append(p2);
                $(div).append(p3);
                $(div).append(p5);
                $.each(value["hints"], function(index, value2) {
                    if (index == "skeleton") {
                        var p1 = $("<p> skeleton: </p>");
                        var p = $("<pre>" + value2 + "</pre>");
                        $(div).append(p1);
                        $(div).append(p);
                    } else {
                        var p = $("<p>" + index + ": " + value2 + "</p>");
                        $(div).append(p);
                    }
                });
                $("#scroll-display-right").append(br);
                $("#scroll-display-right").append(br);

            });
        });
    });
}

function selectAssignment(assignment) {
    $.getJSON("/" + assignment + "/", function(data) {
        $("#scroll-display-left").empty()
        $.each(data["submitters"], function(index, value) {
            var p = $("<p><a></a></p>");
            $("#scroll-display-left").append(p)
            $("a", p).text(value);
            $("a", p).attr("href", "#");
            $("a", p).click(function() {
                selectSidAssignment(value, assignment);
            });
        });
    });
}

function selectSidAssignment(sid, assignment) {
    console.log("/" + assignment + "/" + sid + "/");
    $.getJSON("/" + assignment + "/" + sid + "/", function(data) {
        $("#scroll-display-right").empty();
        var p1 = $("<h3>" + "Assignment: " + assignment + "</h3>");
        var p2 = $("<h3>" + "SID: " + sid + "</h3>");
        var hr = $("<hr>");
        var br = $("<br>");
        $("#scroll-display-right").append(p1);
        $("#scroll-display-right").append(p2);
        $("#scroll-display-right").append(hr)
        $("#scroll-display-right").append(br);
        $("#scroll-display-right").append(br);
        $.each(data["submissions"], function(index, value) {
            var div = $("<div></div>");
            var br = $("<br>");
            $("#scroll-display-right").append(div);
            $(div).append(br);
            var h4 = $("<h4>" + value["timestamp"] + "</h4>");
            str = JSON.stringify(value["code"]);
            console.log(value["code"]);
            var p = $("<p> code: </p>");
            var p1 = $("<pre>" + value["code"] + "</pre>");
            var p2 = $("<p>" + "correct: " + value["correct"] + "</p>");
            var p3 = $("<p>" + "cluster: " + value["cluster"] + "</p>");
            var p5 = $("<p>" + "style score: " + value["style_score"] + "</p>");
            $(div).append(h4);
            $(div).append(p);
            $(div).append(p1);
            $(div).append(p2);
            $(div).append(p3);
            $(div).append(p5);
            $.each(value["hints"], function(index, value2) {
                if (index == "skeleton") {
                    var p1 = $("<p> skeleton: </p>");
                    var p = $("<pre>" + value2 + "</pre>");
                    $(div).append(p1);
                    $(div).append(p);
                } else {
                    var p = $("<p>" + index + ": " + value2 + "</p>");
                    $(div).append(p);
                }
            });
            $(div).append(br);
        });
    });
}







