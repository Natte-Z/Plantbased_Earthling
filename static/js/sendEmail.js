// email Alert
function showEmailAlert(){
    emailAlert.style.display = "block";
     emailFail.style.display = "none";
}
function showEmailFail(){
     emailAlert.style.display = "none";
    emailFail.style.display = "block";
}

// https://www.emailjs.com/docs/tutorial/creating-contact-form/
// init userID from emailjs
(function () {
    emailjs.init("user_TKf54NY2OBMKWEY7MGGO7");
})();

// bind form to emailjs in window.onload
window.onload = function () {

// set variables
let emailAlert = document.getElementById("emailAlert");
let emailFail = document.getElementById("emailFail");

    document.getElementById('contact-form').addEventListener('submit', function (event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // email service, template id from emailjs
        emailjs.sendForm('service_yesouwh', 'plantbased_earthling', this)
            .then(function () {
                // console.log('SUCCESS!');
                showEmailAlert();
            }, function (error) {
                // console.log('FAILED...', error);
                showEmailFail()
            });
    });
}



