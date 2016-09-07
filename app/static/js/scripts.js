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
            $("a", p).attr("href", "/" + value + "/" + "submissions" + "/");
        });
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
