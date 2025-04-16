/**
 * Heart Mate - JavaScript for enhancing user experience
 */

document.addEventListener('DOMContentLoaded', function() {
    // Form validation 
    const form = document.getElementById('predictionForm');
    
    if (form) {
        form.addEventListener('submit', function(event) {
            // Get all required inputs
            const inputs = form.querySelectorAll('input[required], select[required]');
            let isValid = true;
            
            // Check each input
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('is-invalid');
                } else {
                    input.classList.remove('is-invalid');
                }
            });
            
            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
                
                // Show alert message
                const alertDiv = document.createElement('div');
                alertDiv.className = 'alert alert-danger alert-dismissible fade show mt-3';
                alertDiv.innerHTML = `
                    <strong>Error!</strong> Please fill out all required fields.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                `;
                
                // Insert at the top of the form
                form.prepend(alertDiv);
                
                // Scroll to the top of the form
                window.scrollTo({
                    top: form.offsetTop - 100,
                    behavior: 'smooth'
                });
            }
        });
        
        // Remove validation styling on input
        form.querySelectorAll('input, select').forEach(input => {
            input.addEventListener('input', function() {
                if (this.value.trim()) {
                    this.classList.remove('is-invalid');
                }
            });
        });
    }
    
    // Smooth scrolling for all anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert:not(.alert-dismissible)');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.remove('show');
            setTimeout(() => {
                alert.remove();
            }, 300);
        }, 5000);
    });
});