/* ============ DARK MODE ============ */
function toggleDarkMode() {
    var html = document.documentElement;
    var current = html.getAttribute('data-theme');
    var next = current === 'dark' ? 'light' : 'dark';
    html.setAttribute('data-theme', next);
    html.setAttribute('data-bs-theme', next); // Enable Bootstrap 5.3 native dark mode support
    localStorage.setItem('theme', next);

    var icon = document.querySelector('#themeToggle i');
    if (icon) {
        icon.className = next === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
    }
}

function loadTheme() {
    var saved = localStorage.getItem('theme');
    if (saved) {
        document.documentElement.setAttribute('data-theme', saved);
        document.documentElement.setAttribute('data-bs-theme', saved); // Enable Bootstrap 5.3 native dark mode support
        var icon = document.querySelector('#themeToggle i');
        if (icon) {
            icon.className = saved === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-stars-fill';
        }
    }
}

/* ============ NAVBAR SCROLL ============ */
function handleNavScroll() {
    var navbar = document.getElementById('mainNavbar');
    var fab = document.getElementById('fabTop');
    if (!navbar) return;

    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        if (fab) {
            if (window.scrollY > 300) {
                fab.classList.add('visible');
            } else {
                fab.classList.remove('visible');
            }
        }
    });
}

/* ============ TOAST AUTO-DISMISS ============ */
function autoCloseToasts() {
    var toasts = document.querySelectorAll('.toast.show');
    toasts.forEach(function(toast) {
        setTimeout(function() {
            toast.style.transition = 'opacity 0.4s, transform 0.4s';
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(100%)';
            setTimeout(function() { toast.remove(); }, 400);
        }, 4000);
    });
}

/* ============ QUIZ NAVIGATION ============ */
function initQuiz() {
    var form = document.getElementById('skinQuizForm');
    if (!form) return;

    var steps = form.querySelectorAll('.quiz-step');
    var prevBtn = document.getElementById('quizPrev');
    var nextBtn = document.getElementById('quizNext');
    var submitBtn = document.getElementById('quizSubmit');
    var progressBar = document.getElementById('quizProgressBar');
    var stepLabel = document.getElementById('quizStepLabel');
    var currentStep = 0;
    var totalSteps = steps.length;

    function showStep(idx) {
        steps.forEach(function(s) { s.classList.remove('active'); });
        steps[idx].classList.add('active');

        var pct = ((idx + 1) / totalSteps * 100);
        if (progressBar) progressBar.style.width = pct + '%';
        if (stepLabel) stepLabel.textContent = 'Question ' + (idx + 1) + ' of ' + totalSteps;

        if (prevBtn) prevBtn.style.display = idx === 0 ? 'none' : '';
        if (nextBtn) nextBtn.style.display = idx === totalSteps - 1 ? 'none' : '';
        if (submitBtn) submitBtn.style.display = idx === totalSteps - 1 ? '' : 'none';
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function() {
            var currentStepEl = steps[currentStep];
            var radios = currentStepEl.querySelectorAll('input[type="radio"]');
            if (radios.length > 0) {
                var checked = currentStepEl.querySelector('input[type="radio"]:checked');
                if (!checked) {
                    showToast('Please select an option before continuing.', 'warning');
                    return;
                }
            }
            if (currentStep < totalSteps - 1) {
                currentStep++;
                showStep(currentStep);
            }
        });
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function() {
            if (currentStep > 0) {
                currentStep--;
                showStep(currentStep);
            }
        });
    }

    showStep(0);
}

/* ============ RATING ============ */
function rateProduct(productId, rating) {
    var formData = new FormData();
    formData.append('rating', rating);

    fetch('/rate/' + productId, {
        method: 'POST',
        body: formData
    })
    .then(function(r) { return r.json(); })
    .then(function(data) {
        if (data.success) {
            showToast(data.message, 'success');

            var container = document.querySelector('[data-product-id="' + productId + '"]');
            if (container) {
                var stars = container.querySelectorAll('.rate-star');
                stars.forEach(function(star) {
                    var starRating = parseInt(star.getAttribute('data-rating'));
                    if (starRating <= rating) {
                        star.classList.remove('bi-star');
                        star.classList.add('bi-star-fill', 'active');
                    } else {
                        star.classList.remove('bi-star-fill', 'active');
                        star.classList.add('bi-star');
                    }
                });
            }
        }
    })
    .catch(function(err) {
        showToast('Please login to rate products.', 'warning');
    });
}

/* ============ TOAST UTILITY ============ */
function showToast(message, type) {
    type = type || 'info';
    var bgClass = type === 'success' ? 'bg-success' : type === 'danger' ? 'bg-danger' : type === 'warning' ? 'bg-warning text-dark' : 'bg-info';
    var icon = type === 'success' ? 'check-circle' : type === 'danger' ? 'exclamation-triangle' : type === 'warning' ? 'exclamation-triangle' : 'info-circle';

    var container = document.querySelector('.toast-container');
    if (!container) {
        container = document.createElement('div');
        container.className = 'toast-container position-fixed top-0 end-0 p-3';
        container.style.zIndex = '9999';
        container.style.marginTop = '80px';
        document.body.appendChild(container);
    }

    var toast = document.createElement('div');
    toast.className = 'toast show align-items-center text-white ' + bgClass + ' border-0 mb-2';
    toast.setAttribute('role', 'alert');
    toast.innerHTML = '<div class="d-flex"><div class="toast-body"><i class="bi bi-' + icon + ' me-2"></i>' + message + '</div><button type="button" class="btn-close btn-close-white me-2 m-auto" onclick="this.closest(\'.toast\').remove()"></button></div>';

    container.appendChild(toast);

    setTimeout(function() {
        toast.style.transition = 'opacity 0.4s, transform 0.4s';
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(100%)';
        setTimeout(function() { toast.remove(); }, 400);
    }, 4000);
}

/* ============ STAR HOVER ============ */
function initStarHovers() {
    document.querySelectorAll('.star-rating-input').forEach(function(container) {
        var stars = container.querySelectorAll('.rate-star');
        stars.forEach(function(star) {
            star.addEventListener('mouseenter', function() {
                var rating = parseInt(this.getAttribute('data-rating'));
                stars.forEach(function(s) {
                    var r = parseInt(s.getAttribute('data-rating'));
                    if (r <= rating) {
                        s.classList.add('bi-star-fill');
                        s.classList.remove('bi-star');
                    } else {
                        s.classList.remove('bi-star-fill');
                        s.classList.add('bi-star');
                    }
                });
            });
        });

        container.addEventListener('mouseleave', function() {
            stars.forEach(function(s) {
                if (!s.classList.contains('active')) {
                    s.classList.remove('bi-star-fill');
                    s.classList.add('bi-star');
                }
            });
        });
    });
}

/* ============ SMOOTH SCROLL LINKS ============ */
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            var targetId = this.getAttribute('href');
            if (targetId === '#') return;
            var target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });

                var navCollapse = document.querySelector('.navbar-collapse.show');
                if (navCollapse) {
                    var bsCollapse = bootstrap.Collapse.getInstance(navCollapse);
                    if (bsCollapse) bsCollapse.hide();
                }
            }
        });
    });
}

/* ============ REMINDERS (LOCAL STORAGE) ============ */
function initReminders() {
    var savedReminders = JSON.parse(localStorage.getItem('skincare_reminders') || '{}');

    if (savedReminders.morning_enabled) {
        checkReminderTime(savedReminders.morning_time || '07:00', 'Morning skincare routine! Time to cleanse, tone, serum, moisturize, and sunscreen.');
    }
    if (savedReminders.night_enabled) {
        checkReminderTime(savedReminders.night_time || '21:00', 'Night skincare routine! Time for your PM routine.');
    }
}

function checkReminderTime(timeStr, message) {
    var now = new Date();
    var parts = timeStr.split(':');
    var targetHour = parseInt(parts[0]);
    var targetMin = parseInt(parts[1]);

    if (now.getHours() === targetHour && now.getMinutes() === targetMin) {
        if (Notification.permission === 'granted') {
            new Notification('GlowGuide Reminder', { body: message });
        } else {
            showToast(message, 'info');
        }
    }
}

function saveReminders(morningTime, nightTime, morningEnabled, nightEnabled) {
    localStorage.setItem('skincare_reminders', JSON.stringify({
        morning_time: morningTime,
        night_time: nightTime,
        morning_enabled: morningEnabled,
        night_enabled: nightEnabled
    }));
    showToast('Reminders saved!', 'success');
}

/* ============ BUDGET SLIDER ============ */
function initBudgetSlider() {
    var slider = document.getElementById('budgetSlider');
    var label = document.getElementById('budgetLabel');
    if (slider && label) {
        slider.addEventListener('input', function() {
            var val = parseInt(this.value);
            if (val <= 500) label.textContent = 'Budget (Under ₹500)';
            else if (val <= 1000) label.textContent = 'Mid-Range (₹500-₹1000)';
            else label.textContent = 'Premium (₹1000+)';
        });
    }
}

/* ============ ANIMATION OBSERVER ============ */
function initAnimations() {
    if (!window.IntersectionObserver) return;

    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.glass-card, .product-card, .myth-card, .stat-card').forEach(function(el) {
        observer.observe(el);
    });
}

/* ============ INIT ============ */
document.addEventListener('DOMContentLoaded', function() {
    loadTheme();
    handleNavScroll();
    autoCloseToasts();
    initStarHovers();
    initSmoothScroll();
    initBudgetSlider();
    initAnimations();
    initReminders();
});
