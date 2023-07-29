const selectedValues = {};

function handleDropdownItemClick(item, dropdownList, input) {
  const selectedValue = item.textContent;
  input.value = selectedValue;
  selectedValues[input.id] = selectedValue;
  dropdownList.style.display = "none";
}

function populateDropdownList(dropdownList, values, input) {
  dropdownList.innerHTML = "";
  values.forEach((value) => {
    const item = document.createElement("div");
    item.classList.add("dropdown-item");
    item.textContent = value;
    item.addEventListener("click", () => {
      handleDropdownItemClick(item, dropdownList, input);
    });
    dropdownList.appendChild(item);
  });
}

// Fruit names for each dropdown
const names1 = ["Apple", "Banana", "Cherry", "Grape", "Orange", "Pear"];
const names2 = ["Lemon", "Mango", "Kiwi", "Pineapple", "Watermelon"];
const names3 = ["Strawberry", "Blueberry", "Raspberry", "Blackberry", "Cranberry"];
const names4 = ["Peach", "Plum", "Apricot", "Nectarine", "Fig"];
const names5a = ["Coconut", "Guava", "Papaya", "Lychee", "Dragon Fruit"];
const names5b = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const names5c = ["Apple", "Banana", "Cherry", "Grape", "Orange", "Pear"];
const names6 = ["Coconut", "Guava", "Papaya", "Lychee", "Dragon Fruit"];
const names7 = ["Coconut", "Guava", "Papaya", "Lychee", "Dragon Fruit"];
const names8 = ["Coconut", "Guava", "Papaya", "Lychee", "Dragon Fruit"];
const names9 = ["Coconut", "Guava", "Papaya", "Lychee", "Dragon Fruit"];
const names10 = ["Coconut", "Guava", "Papaya", "Lychee", "Dragon Fruit"];

// Function to handle the dropdown filtering
function handleDropdownFilter(event, dropdownList) {
  const filterValue = event.target.value.toLowerCase();
  const dropdownItems = dropdownList.querySelectorAll(".dropdown-item");

  let hasVisibleItems = false;

  dropdownItems.forEach((item) => {
      const itemText = item.textContent.toLowerCase();
      if (itemText.includes(filterValue)) {
          item.style.display = "block";
          hasVisibleItems = true;
      } else {
          item.style.display = "none";
      }
  });

  dropdownList.style.display = hasVisibleItems ? "block" : "none";
}

// Function to initialize each dropdown with values and event listeners
function initializeDropdown(inputId, listId, values, submitButtonId) {
  const dropdownList = document.getElementById(listId);
  const input = document.getElementById(inputId);
  const submitButton = document.getElementById(submitButtonId);

  populateDropdownList(dropdownList, values, input);

  input.addEventListener("focus", (event) => handleDropdownFilter(event, dropdownList));
  input.addEventListener("input", (event) => handleDropdownFilter(event, dropdownList));

  if(inputId !== "filterInput5a" && inputId !== "filterInput5b") {
    submitButton.addEventListener("click", () => {
      alert(`Selected Fruit: ${selectedValues[inputId]}`);
      // let allSelectedValues = "Selected Values:\n";
      // for (const key in selectedValues) {
      //   allSelectedValues += `${key}: ${selectedValues[key]}\n`;
      // }
      // alert(allSelectedValues);
    });
  }

  else {
    submitButton.addEventListener("click", () => {
      const input = document.getElementById("filterInput5c");
      selectedValues["filterInput5c"] = input.value;
      const teacher = selectedValues["filterInput5a"];
      const day = selectedValues["filterInput5b"];
      const time = selectedValues["filterInput5c"];

      if (teacher && day && time) {
        alert(`Teacher: ${teacher}\nDay: ${day}\nTime: ${time}`);
      }
      else {
        alert("Please select both a fruit and a flower.");
      }
      // let allSelectedValues = "Selected Values:\n";
      // for (const key in selectedValues) {
      //   allSelectedValues += `${key}: ${selectedValues[key]}\n`;
      // }
      // alert(allSelectedValues);
    });
  }

  document.addEventListener("click", (event) => {
    if (!event.target.matches(`#${inputId}, .dropdown-item`)) {
      dropdownList.style.display = "none";
    }
  });
}


// Call the function to initialize each dropdown
initializeDropdown("filterInput1", "dropdownList1", names1, "submitButton1");
initializeDropdown("filterInput2", "dropdownList2", names2, "submitButton2");
initializeDropdown("filterInput3", "dropdownList3", names3, "submitButton3");
initializeDropdown("filterInput4", "dropdownList4", names4, "submitButton4");
initializeDropdown("filterInput5a", "dropdownList5a", names5a, "submitButton5");
initializeDropdown("filterInput5b", "dropdownList5b", names5b, "submitButton5");
initializeDropdown("filterInput6", "dropdownList6", names6, "submitButton6");
initializeDropdown("filterInput7", "dropdownList7", names7, "submitButton7");
initializeDropdown("filterInput8", "dropdownList8", names8, "submitButton8");
initializeDropdown("filterInput9", "dropdownList9", names9, "submitButton9");
initializeDropdown("filterInput10", "dropdownList10", names10, "submitButton10");

// Rest of the code remains the same as before

function hideAllInputContainers(exceptContainer) {
  const allInputContainers = document.querySelectorAll(".dropdown-container");
  allInputContainers.forEach((container) => {
    if (container !== exceptContainer) {
      container.style.display = "none";
    }
  });
}

// Function to show the dropdown container when a button is clicked
function showInputContainer(inputContainer) {
  hideAllInputContainers(inputContainer);

  // Show the clicked input container
  inputContainer.style.display = "block";

  
}

// Add an event listener to each question button to show the respective input container
function addEventListenerToQuestionBtns() {
  const questionBtns = document.querySelectorAll(".set");
  questionBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const inputContainerId = btn.id.replace("-btn", "-input");
      const inputContainer = document.getElementById(inputContainerId);
      showInputContainer(inputContainer);
    });
  });
}


// Function to initialize the code on page load
function init() {
  addEventListenerToQuestionBtns();
}

// Call the init function on page load
window.onload = init;
