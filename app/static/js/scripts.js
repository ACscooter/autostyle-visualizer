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
            $("a", p).attr("href", "/" + value + "/");
            $("a", p).attr("onclick", "showAssignmentSubmissions(" + value + ")")
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
            // $("a", p).attr("href", "/" + value + "/" + "submissions" + "/");
            $("a", p).attr("href", "#");
            $("a", p).click(function() {
                tester(value);
            });
        });
    });
}

function tester(sid) {
    $.getJSON("/" + sid + "/" + "submissions" + "/", function(data) {
        // $("#scroll-display-right").empty()
        // $.each(data["names"], function(index, value) {
        //     var p = $("<p><a></a></p>");
        //     $("#scroll-display-left").append(p)
        //     $("a", p).text(value);
        //     // $("a", p).attr("href", "/" + value + "/" + "submissions" + "/");
        //     $("a", p).attr("href", "#");
        //     $("a", p).click("showStudents()");
        // });
        $("#scroll-display-right").empty();
        // console.log(JSON.parse(data));
        // console.log(JSON.stringify(data, undefined, 2));
        // var stringified = JSON.stringify(data, undefined, 2);
        // var objectified = $.parseJSON(stringified);
        // console.log(objectified);
        // var str = Json.stringify(objectified["Add Up"]["code"], undefined, 2);
        // var p = $("<p>" + str + "</p>");
        // $("#scroll-display-right").append(p)

        // $("p", p).text(data["Add Up"]["code"]);
    });
}

function showAssignmentSubmissions(assignment) {
    $.getJSON(link, function(data) {
        console.log(data)
        // $.each(data, function(index, value) {
        // 	var p = $("<p><a></a></p>");

        // 	$("#scroll-display-right").append(p)

        // 	$("a", p).text(value);
        // });
        $("scroll-display-right").append(data);
    });
}
