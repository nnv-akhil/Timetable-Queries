function fun(value) {
    console.log(value);
    var formData =new FormData();
    formData.append("q", value); 

    $.ajax({
        url: '/send_dept',
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function(response) {
           
        },
        error: function(error) {
            console.log("AJAX request failed:", error);
        }
        });
}