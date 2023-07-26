const fruits = [
  "apple",
  "banana",
  "cherry",
  "mango",
  "orange",
  "pineapple",
  "strawberry",
  "watermelon"
  // Add more fruit names as needed
];

function query2(inputId, dropdownListId, submitButtonId) {
  const inputElement = document.getElementById(inputId);
  const dropdownListElement = document.getElementById(dropdownListId);
  const submitButton = document.getElementById(submitButtonId);

  // Function to filter and display relevant fruits
  function updateDropdownList() {
      const inputValue = inputElement.value.toLowerCase();
      const filteredFruits = fruits.filter(fruit =>
          fruit.toLowerCase().includes(inputValue)
      );

      // Clear the existing dropdown items
      dropdownListElement.innerHTML = "";

      // Add filtered fruits to the dropdown list
      filteredFruits.forEach(fruit => {
          const option = document.createElement("div");
          option.textContent = fruit;
          option.classList.add("dropdown-item");

          // Handle click on the dropdown item
          option.addEventListener("click", function () {
              // Display the selected fruit in the input field
              inputElement.value = fruit;

              // Show an alert message with the selected fruit
              alert("Selected Fruit: " + fruit);

              // Hide the dropdown after selection
              dropdownListElement.style.display = "none";
          });

          dropdownListElement.appendChild(option);
      });

      // Display the dropdown
      dropdownListElement.style.display = "block";
  }

  // Update the dropdown list when the input field value changes
  inputElement.addEventListener("input", updateDropdownList);

  // Handle the input field focus event
  inputElement.addEventListener("focus", function () {
      if (inputElement.value.trim() === "") {
          // Show the whole dropdown if there is no input
          updateDropdownList();
      }
  });

  // Hide the dropdown when the input field loses focus
  inputElement.addEventListener("blur", function () {
      dropdownListElement.style.display = "none";
  });

  // Handle the submit button click
  submitButton.addEventListener("click", function () {
      const teacherName = inputElement.value.trim();
      alert("Submitted Teacher Name: " + teacherName);
  });
}

// Call the function with the provided input element IDs
query2("filterInput2", "dropdownList2", "submitButton2");