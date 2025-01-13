// Wait for the DOM to load before attaching event listeners
document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('addNoteModal');
    const openModalBtn = document.getElementById('open-modal-btn');
    const closeModalBtn = document.getElementById('close-modal-btn');
    const closeModalFooterBtn = document.getElementById('close-btn');

    // Function to show the modal
    function showModal() {
        modal.style.display = 'block';
    }

    // Function to hide the modal
    function hideModal() {
        modal.style.display = 'none';
    }

    // Attach event listeners
    if (openModalBtn) {
        openModalBtn.addEventListener('click', showModal);
    }

    if (closeModalBtn) {
        closeModalBtn.addEventListener('click', hideModal);
    }

    if (closeModalFooterBtn) {
        closeModalFooterBtn.addEventListener('click', hideModal);
    }
});
