document.querySelectorAll('.tab-button').forEach(button => {
    button.addEventListener('click', () => {
        const tabContentId = button.getAttribute('data-tab');

        // Remove active class from all buttons and tab contents
        document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));

        // Add active class to the clicked button and corresponding tab content
        button.classList.add('active');
        document.getElementById(tabContentId).classList.add('active');
    });
});
