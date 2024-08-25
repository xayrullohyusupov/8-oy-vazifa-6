// JavaScript kodlari, masalan, yangiliklar slayd-show yoki obuna formasi validatsiyasi
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.newsletter-form');
    form.addEventListener('submit', function(event) {
        const email = form.querySelector('input[name="email"]').value;
        if (!email) {
            alert('Iltimos, email manzilini kiriting.');
            event.preventDefault();
        }
    });
});
