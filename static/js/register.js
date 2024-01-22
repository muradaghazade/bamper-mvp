const slider = document.querySelector('.slider');
const slideButtons = document.querySelectorAll('.slide-button');

slideButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const targetSlideIndex = parseInt(button.getAttribute('data-slide-index')) - 1;
    const translateX = -targetSlideIndex * 400;
    slider.style.transform = `translateX(${translateX}px)`;
  });
});

function validateEmailorNumber() {
  var emailOrNumber = document.getElementById("emailornumber").value;
  var numberPattern = /^05[0-9]-[0-9]{3}-[0-9]{2}-[0-9]{2}$/;

  if (numberPattern.test(emailOrNumber)) {

      console.log("Numara formatı doğru!");
  } else {
      // Numara formatı hatalı, kullanıcıyı uyarabilir veya başka bir işlem yapabilirsiniz.
      console.log("Numara formatı hatalı!");
  }
}

let yesBtn = document.getElementById('yes-btn');

    
  yesBtn.addEventListener('click', function() {
        
        window.location.href = '../accounts/templates/log-in.html';
});

let noBtn =  document.getElementById('no-btn');
let notificationContainer = document.getElementById('notification-container')
noBtn.addEventListener('click', function() {
  notificationContainer.style.display = 'none';
})