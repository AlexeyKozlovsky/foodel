function reveal() {
    var reveals = document.querySelectorAll(".client-info");

    for (var i = 0; i < reveals.length; i++) {
      var windowHeight = window.innerHeight;
      var elementTop = reveals[i].getBoundingClientRect().top;
      var elementVisible = 150;

      if (elementTop < windowHeight - elementVisible) {
        reveals[i].classList.add("active");
      } else {
        reveals[i].classList.remove("active");
      }
    }
  }

  const scrollable_element = document.querySelector(".clients-container");
  scrollable_element.addEventListener("scroll", reveal);

reveal();
