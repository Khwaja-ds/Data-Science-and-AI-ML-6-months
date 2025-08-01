document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('roadmapForm');
    const generateBtn = document.getElementById('generateBtn');
    const btnText = document.querySelector('.btn-text');
    const loadingSpinner = document.querySelector('.loading-spinner');
    const resultsSection = document.getElementById('resultsSection');
    const copyBtn = document.getElementById('copyBtn');
    const newRoadmapBtn = document.getElementById('newRoadmapBtn');
    const resultField = document.getElementById('resultField');
    const resultGoal = document.getElementById('resultGoal');
    const roadmapText = document.getElementById('roadmapText');

    // Form submission handler
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const field = document.getElementById('careerField').value;
        const goal = document.getElementById('careerGoal').value;
        
        if (!field || !goal) {
            showNotification('Please fill in all fields', 'error');
            return;
        }
        
        // Show loading state
        setLoadingState(true);
        
        try {
            const response = await fetch('/generate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    field: field,
                    goal: goal
                })
            });
            
            const data = await response.json();
            
            if (response.ok && data.success) {
                // Display results
                displayResults(data);
                showNotification('Roadmap generated successfully!', 'success');
            } else {
                throw new Error(data.error || 'Failed to generate roadmap');
            }
        } catch (error) {
            console.error('Error:', error);
            showNotification(error.message || 'An error occurred while generating the roadmap', 'error');
        } finally {
            // Hide loading state
            setLoadingState(false);
        }
    });

    // Copy to clipboard functionality
    copyBtn.addEventListener('click', async function() {
        const roadmapContent = roadmapText.textContent;
        
        try {
            await navigator.clipboard.writeText(roadmapContent);
            
            // Visual feedback
            copyBtn.classList.add('copy-success');
            copyBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            
            setTimeout(() => {
                copyBtn.classList.remove('copy-success');
                copyBtn.innerHTML = '<i class="fas fa-copy"></i> Copy to Clipboard';
            }, 2000);
            
            showNotification('Roadmap copied to clipboard!', 'success');
        } catch (err) {
            console.error('Failed to copy: ', err);
            showNotification('Failed to copy to clipboard', 'error');
        }
    });

    // New roadmap button
    newRoadmapBtn.addEventListener('click', function() {
        // Hide results
        resultsSection.style.display = 'none';
        
        // Reset form
        form.reset();
        
        // Scroll to top
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        
        // Focus on first field
        document.getElementById('careerField').focus();
    });

    // Set loading state
    function setLoadingState(isLoading) {
        if (isLoading) {
            generateBtn.disabled = true;
            btnText.style.display = 'none';
            loadingSpinner.style.display = 'flex';
        } else {
            generateBtn.disabled = false;
            btnText.style.display = 'flex';
            loadingSpinner.style.display = 'none';
        }
    }

    // Display results
    function displayResults(data) {
        resultField.textContent = data.field;
        resultGoal.textContent = data.goal;
        roadmapText.textContent = data.roadmap;
        
        // Show results section
        resultsSection.style.display = 'block';
        
        // Scroll to results
        resultsSection.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }

    // Show notification
    function showNotification(message, type = 'info') {
        // Remove existing notifications
        const existingNotification = document.querySelector('.notification');
        if (existingNotification) {
            existingNotification.remove();
        }
        
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${type === 'success' ? 'check-circle' : type === 'error' ? 'exclamation-circle' : 'info-circle'}"></i>
                <span>${message}</span>
            </div>
            <button class="notification-close">
                <i class="fas fa-times"></i>
            </button>
        `;
        
        // Add styles
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#48bb78' : type === 'error' ? '#f56565' : '#4299e1'};
            color: white;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            z-index: 1000;
            max-width: 400px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 15px;
            animation: slideInRight 0.3s ease-out;
        `;
        
        // Add animation styles
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideInRight {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
            
            .notification-content {
                display: flex;
                align-items: center;
                gap: 10px;
                flex: 1;
            }
            
            .notification-close {
                background: none;
                border: none;
                color: white;
                cursor: pointer;
                padding: 0;
                font-size: 14px;
                opacity: 0.8;
                transition: opacity 0.2s;
            }
            
            .notification-close:hover {
                opacity: 1;
            }
        `;
        document.head.appendChild(style);
        
        // Add to page
        document.body.appendChild(notification);
        
        // Close button functionality
        const closeBtn = notification.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notification.remove();
        });
        
        // Auto remove after 5 seconds
        setTimeout(() => {
            if (notification.parentNode) {
                notification.remove();
            }
        }, 5000);
    }

    // Add smooth scrolling for better UX
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Add form validation feedback
    const inputs = form.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.hasAttribute('required') && !this.value.trim()) {
                this.style.borderColor = '#f56565';
            } else {
                this.style.borderColor = '#e2e8f0';
            }
        });
        
        input.addEventListener('input', function() {
            if (this.value.trim()) {
                this.style.borderColor = '#e2e8f0';
            }
        });
    });

    // Add keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Ctrl/Cmd + Enter to submit form
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            if (document.activeElement.tagName === 'TEXTAREA') {
                e.preventDefault();
                form.dispatchEvent(new Event('submit'));
            }
        }
        
        // Escape to close notifications
        if (e.key === 'Escape') {
            const notification = document.querySelector('.notification');
            if (notification) {
                notification.remove();
            }
        }
    });

    // Add focus management for better accessibility
    const focusableElements = 'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])';
    
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            const focusable = [...document.querySelectorAll(focusableElements)];
            const firstFocusable = focusable[0];
            const lastFocusable = focusable[focusable.length - 1];
            
            if (e.shiftKey) {
                if (document.activeElement === firstFocusable) {
                    lastFocusable.focus();
                    e.preventDefault();
                }
            } else {
                if (document.activeElement === lastFocusable) {
                    firstFocusable.focus();
                    e.preventDefault();
                }
            }
        }
    });
}); 