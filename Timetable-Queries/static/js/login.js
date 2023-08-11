function login()
	{
		var ent_pwd = document.getElementById("pwd").value;
        var formData= new FormData();
        formData.append("q",ent_pwd); 
        console.log(ent_pwd);
        // crct_pwd=""
        $.ajax({
            url: '/check',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
               if(response === "fail")
               {
                document.getElementById("incorrect").style.display = "block";
               }
               else if(response === "pass") {
                var adminLink = document.getElementById("sample");
                adminLink.click();
               }
            },
            error: function(error) {
                console.log("AJAX request failed:", error);
            }
            });
        // console.log(pwd)
        // if(crct_pwd===ent_pwd){
        // window.location = render_template('admin.html'); }
		
	}

function check() {
   document.getElementById("forgot").style.display = "block";
}

// document.addEventListener("DOMContentLoaded", function() {
//     document.getElementById("sample").addEventListener("click", function(event) {
//         event.preventDefault(); // Prevent the default behavior of the link
//     });
// });
