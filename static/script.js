function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}

// store last image (IMPORTANT FIX)
let lastImage = null;

function previewImage(event) {
  let file = event.target.files[0];
  if (!file) return;

  lastImage = file;

  let img = document.getElementById("preview");

  let reader = new FileReader();
  reader.onload = function () {
    img.src = reader.result;
    img.style.display = "block"; // ALWAYS KEEP IMAGE VISIBLE
  };

  reader.readAsDataURL(file);
}

function showLoader() {
  document.getElementById("loader").style.display = "block";
  return true;
}
