
// https://www.emailjs.com/docs/tutorial/creating-contact-form/

// init userID from emailjs
(function () {
    emailjs.init("user_TKf54NY2OBMKWEY7MGGO7");
})();

// bind form to emailjs
window.onload = function () {
    document.getElementById('contact-form').addEventListener('submit', function (event) {
        event.preventDefault();
        // generate a five digit number for the contact_number variable
        this.contact_number.value = Math.random() * 100000 | 0;
        // email service, template id from emailjs
        emailjs.sendForm('service_yesouwh', 'plantbased_earthling', this)
            .then(function () {
                console.log('SUCCESS!');
            }, function (error) {
                console.log('FAILED...', error);
            });
    });
}
