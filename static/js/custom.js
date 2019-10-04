(function() {
  'use strict';
  window.addEventListener('load', function() {
    // Get the forms we want to add validation styles to
    var forms = document.getElementsByClassName('needs-validation');
    // Loop over them and prevent submission
    var validation = Array.prototype.filter.call(forms, function(form) {
      form.addEventListener('submit', function(event) {
        if (form.checkValidity() === false) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add('was-validated');
      }, false);
    });
  }, false);
})();


var message = document.getElementById("message-container");

setTimeout(function(){
   message.style.display = "none";
}, 3000);


function showUpdateForm(toggle)
{
    if(toggle==1)
        {
        document.getElementById("updateForm").style.display="block";
        document.getElementById("profileInformation").style.display="none";
        }
    else
        {
        document.getElementById("updateForm").style.display="none";
        document.getElementById("profileInformation").style.display="block";
        }
}