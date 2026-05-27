/* ═══════════════════════════════════════════════════════════════ */
/* GROW SALE PRODUCTS — Main JavaScript                          */
/* Premium Screen Printing Website                               */
/* Clean, smooth animations — no glitches                        */
/* ═══════════════════════════════════════════════════════════════ */

(function () {
    'use strict';

    /* ── Utility: DOM Ready ────────────────────────────────────── */
    function onReady(fn) {
        if (document.readyState !== 'loading') {
            fn();
        } else {
            document.addEventListener('DOMContentLoaded', fn);
        }
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 1. NAVBAR SCROLL EFFECT                                      */
    /* ══════════════════════════════════════════════════════════════ */
    function initNavbar() {
        const nav = document.getElementById('main-nav');
        if (!nav) return;

        let lastScroll = 0;
        let ticking = false;

        function updateNav() {
            const scrollY = window.scrollY;

            if (scrollY > 50) {
                nav.classList.add('nav-scrolled');
            } else {
                nav.classList.remove('nav-scrolled');
            }

            // Hide on scroll down, show on scroll up (only after 300px)
            if (scrollY > 300) {
                if (scrollY > lastScroll + 5) {
                    nav.style.transform = 'translateY(-100%)';
                } else if (scrollY < lastScroll - 5) {
                    nav.style.transform = 'translateY(0)';
                }
            } else {
                nav.style.transform = 'translateY(0)';
            }

            lastScroll = scrollY;
            ticking = false;
        }

        window.addEventListener('scroll', function () {
            if (!ticking) {
                requestAnimationFrame(updateNav);
                ticking = true;
            }
        }, { passive: true });
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 2. MOBILE MENU TOGGLE                                        */
    /* ══════════════════════════════════════════════════════════════ */
    function initMobileMenu() {
        const btn = document.getElementById('mobile-menu-btn');
        const menu = document.getElementById('mobile-menu');
        if (!btn || !menu) return;

        let isOpen = false;

        btn.addEventListener('click', function () {
            isOpen = !isOpen;

            if (isOpen) {
                menu.classList.remove('mobile-menu-closed');
                menu.classList.add('mobile-menu-open');
                btn.querySelector('.hamburger-lines').classList.add('hamburger-active');
                document.body.style.overflow = 'hidden';
            } else {
                menu.classList.add('mobile-menu-closed');
                menu.classList.remove('mobile-menu-open');
                btn.querySelector('.hamburger-lines').classList.remove('hamburger-active');
                document.body.style.overflow = '';
            }
        });

        // Close menu on nav link click
        menu.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                if (isOpen) {
                    isOpen = false;
                    menu.classList.add('mobile-menu-closed');
                    menu.classList.remove('mobile-menu-open');
                    btn.querySelector('.hamburger-lines').classList.remove('hamburger-active');
                    document.body.style.overflow = '';
                }
            });
        });

        // Close on escape
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && isOpen) {
                btn.click();
            }
        });
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 3. SMOOTH SCROLL FOR ANCHOR LINKS                            */
    /* ══════════════════════════════════════════════════════════════ */
    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
            anchor.addEventListener('click', function (e) {
                const targetId = this.getAttribute('href');
                if (targetId === '#') return;

                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    const navHeight = document.getElementById('main-nav')?.offsetHeight || 80;
                    const targetPos = target.getBoundingClientRect().top + window.scrollY - navHeight;

                    window.scrollTo({
                        top: targetPos,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 4. COUNTER ANIMATION (Stats Section)                         */
    /* ══════════════════════════════════════════════════════════════ */
    function initCounters() {
        const counters = document.querySelectorAll('.counter');
        if (counters.length === 0) return;

        function animateCounter(el) {
            const target = parseInt(el.getAttribute('data-target'), 10);
            if (isNaN(target)) return;

            const duration = 2200;
            const startTime = performance.now();

            function easeOutQuart(t) {
                return 1 - Math.pow(1 - t, 4);
            }

            function update(currentTime) {
                const elapsed = currentTime - startTime;
                const progress = Math.min(elapsed / duration, 1);
                const easedProgress = easeOutQuart(progress);
                const currentVal = Math.floor(target * easedProgress);

                el.textContent = currentVal.toLocaleString();

                if (progress < 1) {
                    requestAnimationFrame(update);
                } else {
                    el.textContent = target.toLocaleString();
                }
            }

            requestAnimationFrame(update);
        }

        if ('IntersectionObserver' in window) {
            const observer = new IntersectionObserver(function (entries) {
                entries.forEach(function (entry) {
                    if (entry.isIntersecting) {
                        animateCounter(entry.target);
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.3 });

            counters.forEach(function (counter) {
                observer.observe(counter);
            });
        } else {
            counters.forEach(animateCounter);
        }
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 5. TOAST AUTO-DISMISS                                        */
    /* ══════════════════════════════════════════════════════════════ */
    function initToasts() {
        const toasts = document.querySelectorAll('.toast-notification');
        if (toasts.length === 0) return;

        toasts.forEach(function (toast, index) {
            setTimeout(function () {
                toast.classList.add('toast-dismissing');
                toast.addEventListener('animationend', function () {
                    toast.remove();
                    const container = document.getElementById('toast-container');
                    if (container && container.children.length === 0) {
                        container.remove();
                    }
                });
            }, 5000 + index * 500);
        });
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 6. GSAP HERO ANIMATION (Squeegee Effect)                     */
    /* ══════════════════════════════════════════════════════════════ */
    function initHeroAnimation() {
        if (typeof gsap === 'undefined') return;

        const hero = document.getElementById('hero');
        if (!hero) return;

        if (typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);
        }

        // Set initial states
        gsap.set('#hero-badge', { opacity: 0, y: 20 });
        gsap.set('#hero-sub', { opacity: 0, y: 20 });
        gsap.set('#hero-ctas', { opacity: 0, y: 20 });
        gsap.set('#hero-float-stats', { opacity: 0, x: 40 });

        const tl = gsap.timeline({
            defaults: { ease: 'power3.out' },
            delay: 0.2
        });

        // Badge fades in
        tl.to('#hero-badge', {
            opacity: 1, y: 0, duration: 0.7
        }, 0.1);

        // Heading lines stagger slide up
        const heroLines = document.querySelectorAll('.hero-line > span');
        if (heroLines.length > 0) {
            gsap.set(heroLines, { y: '100%' });
            tl.to(heroLines, {
                y: '0%',
                duration: 0.9,
                stagger: 0.15,
                ease: 'power3.out'
            }, 0.2);
        }

        // Subheading
        tl.to('#hero-sub', {
            opacity: 1, y: 0, duration: 0.7
        }, 0.9);

        // CTA buttons
        tl.to('#hero-ctas', {
            opacity: 1, y: 0, duration: 0.6
        }, 1.1);

        // Floating stats (desktop)
        tl.to('#hero-float-stats', {
            opacity: 1, x: 0, duration: 0.8, ease: 'power2.out'
        }, 1.2);

        // Subtle parallax on scroll
        if (typeof ScrollTrigger !== 'undefined') {
            gsap.to('#hero .max-w-7xl', {
                scrollTrigger: {
                    trigger: '#hero',
                    start: 'top top',
                    end: 'bottom top',
                    scrub: 1.5
                },
                y: 80,
                opacity: 0.4
            });
        }
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 7. SCROLL-REVEAL — Smooth IntersectionObserver System         */
    /* Clean fade-up with no conflicts                              */
    /* ══════════════════════════════════════════════════════════════ */
    function initScrollReveal() {
        var revealElements = document.querySelectorAll(
            '.reveal, .reveal-left, .reveal-right, .reveal-scale, .cmyk-reveal'
        );

        if (revealElements.length === 0) return;

        if (!('IntersectionObserver' in window)) {
            revealElements.forEach(function (el) {
                el.classList.add('revealed');
            });
            return;
        }

        var observerOptions = {
            root: null,
            rootMargin: '0px 0px -50px 0px',
            threshold: 0.1
        };

        var revealObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    var el = entry.target;
                    el.classList.add('revealed');
                    revealObserver.unobserve(el);

                    // Clean up animation classes after transition completes
                    // to prevent conflicts with hover transforms
                    var cleanup = function () {
                        el.removeEventListener('transitionend', cleanup);
                        el.classList.remove(
                            'reveal', 'reveal-left', 'reveal-right',
                            'reveal-scale', 'cmyk-reveal', 'revealed'
                        );
                        // Remove delay classes
                        var classes = Array.from(el.classList);
                        classes.forEach(function (c) {
                            if (c.startsWith('delay-')) el.classList.remove(c);
                        });
                    };

                    // Wait for the longest animation to finish, then clean up
                    setTimeout(cleanup, 1200);
                }
            });
        }, observerOptions);

        revealElements.forEach(function (el) {
            revealObserver.observe(el);
        });
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 8. GSAP SCROLL ANIMATIONS — Stat cards stagger               */
    /* ══════════════════════════════════════════════════════════════ */
    function initScrollAnimations() {
        if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

        gsap.registerPlugin(ScrollTrigger);

        // Stat cards — fade up with stagger
        var statCards = gsap.utils.toArray('.stat-card');
        if (statCards.length > 0) {
            gsap.from(statCards, {
                scrollTrigger: {
                    trigger: statCards[0].parentElement,
                    start: 'top 80%',
                    toggleActions: 'play none none none'
                },
                y: 40,
                opacity: 0,
                duration: 0.7,
                stagger: 0.12,
                ease: 'power2.out'
            });
        }
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 9. FILE UPLOAD PREVIEW                                       */
    /* ══════════════════════════════════════════════════════════════ */
    function initFileUpload() {
        const dropZone = document.getElementById('file-drop-zone');
        if (!dropZone) return;

        const fileInput = dropZone.querySelector('input[type="file"]');
        const preview = document.getElementById('file-preview');
        const fileNameEl = document.getElementById('file-name');
        const fileSizeEl = document.getElementById('file-size');
        const removeBtn = document.getElementById('file-remove');

        if (!fileInput) return;

        ['dragenter', 'dragover'].forEach(function (eventName) {
            dropZone.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.add('file-drop-active');
            });
        });

        ['dragleave', 'drop'].forEach(function (eventName) {
            dropZone.addEventListener(eventName, function (e) {
                e.preventDefault();
                e.stopPropagation();
                dropZone.classList.remove('file-drop-active');
            });
        });

        fileInput.addEventListener('change', function () {
            if (this.files && this.files[0]) {
                showFilePreview(this.files[0]);
            }
        });

        function showFilePreview(file) {
            if (!preview || !fileNameEl || !fileSizeEl) return;

            fileNameEl.textContent = file.name;
            var sizeMB = (file.size / (1024 * 1024)).toFixed(2);
            fileSizeEl.textContent = sizeMB + ' MB';
            preview.classList.remove('hidden');
        }

        if (removeBtn) {
            removeBtn.addEventListener('click', function (e) {
                e.preventDefault();
                e.stopPropagation();
                fileInput.value = '';
                if (preview) preview.classList.add('hidden');
            });
        }
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 10. FORM ENHANCEMENTS                                        */
    /* ══════════════════════════════════════════════════════════════ */
    function initFormEnhancements() {
        document.querySelectorAll('.form-input').forEach(function (input) {
            input.addEventListener('focus', function () {
                this.closest('.form-group')?.classList.add('focused');
            });

            input.addEventListener('blur', function () {
                this.closest('.form-group')?.classList.remove('focused');
            });
        });

        var formEl = document.getElementById('quote-form');
        if (!formEl) return;

        formEl.querySelectorAll('input:not([type="file"]):not([type="hidden"]):not(.form-input)').forEach(function (input) {
            input.classList.add('form-input', 'w-full', 'px-4', 'py-3', 'rounded-xl', 'border-2', 'border-gray-200', 'bg-gray-50/50', 'text-gs-charcoal', 'placeholder-gray-300', 'transition-all', 'duration-300');
        });

        formEl.querySelectorAll('select:not(.form-input)').forEach(function (select) {
            select.classList.add('form-input', 'w-full', 'px-4', 'py-3', 'rounded-xl', 'border-2', 'border-gray-200', 'bg-gray-50/50', 'text-gs-charcoal', 'transition-all', 'duration-300');
        });

        formEl.querySelectorAll('textarea:not(.form-input)').forEach(function (textarea) {
            textarea.classList.add('form-input', 'w-full', 'px-4', 'py-3', 'rounded-xl', 'border-2', 'border-gray-200', 'bg-gray-50/50', 'text-gs-charcoal', 'placeholder-gray-300', 'transition-all', 'duration-300', 'resize-none');
        });
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* 11. SMOOTH PAGE ENTRANCE                                     */
    /* ══════════════════════════════════════════════════════════════ */
    function initPageEntrance() {
        // Fade in the body smoothly on load
        document.body.classList.add('page-loaded');
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* INITIALIZE EVERYTHING                                        */
    /* ══════════════════════════════════════════════════════════════ */
    onReady(function () {
        initPageEntrance();
        initNavbar();
        initMobileMenu();
        initSmoothScroll();
        initCounters();
        initToasts();
        initHeroAnimation();
        initScrollAnimations();
        initScrollReveal();
        initFileUpload();
        initFormEnhancements();
    });

})();
