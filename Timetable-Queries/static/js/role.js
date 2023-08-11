function fun(value) {
    console.log(value);
    var formData =new FormData();
    formData.append("q", value); 

    $.ajax({
        url: '/send_role',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
            // console.log(response)
            // document.getElementById("my").href =response; 
        },
        error: function(error) {
            console.log("AJAX request failed:", error);
        }
        });
}