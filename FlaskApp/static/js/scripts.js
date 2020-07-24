function toggleStuff() {
  'use strict';

  const submitButton = document.getElementById('submitButton');
  const uploadForm = document.getElementById('uploadForm');
  const loadingSection = document.getElementById('loadingSection');
  const instructionText = document.getElementById('instructionText');
  submitButton.addEventListener('click', toggleLoading);
  function toggleLoading() {
    console.log('test');
    if (uploadForm.checkValidity()) {
      uploadForm.classList.add('d-none');
      loadingSection.classList.remove('d-none');
      instructionText.innerHTML =
        'Processing your files. Please do not click the back button or refresh the page.';
    }
  }
}
toggleStuff();
