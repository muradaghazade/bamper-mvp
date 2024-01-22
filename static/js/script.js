var toggleButton = document.getElementById("toggleButton");
        var textContainer = document.getElementById("textContainer");
        var inputContainer = document.getElementById("inputContainer");
        var isOpen = false;

        toggleButton.addEventListener("click", function() {
            isOpen = !isOpen; 

            if (isOpen) {
                toggleButton.textContent = "İmtina";
                textContainer.classList.add("hidden");
                inputContainer.classList.remove("hidden");
            } else {
                toggleButton.textContent = "Filterlə daxil edin";
                textContainer.classList.remove("hidden");
                inputContainer.classList.add("hidden");
            }
        });

        function generateYears() {
            var currentYear = new Date().getFullYear();
            var selectElement = document.getElementById("yearSelect");
          
            for (var year = currentYear; year >= 1950; year--) {
              var option = document.createElement("option");
              option.value = year;
              option.text = year;
              selectElement.add(option);
            }
          }
    
          generateYears();