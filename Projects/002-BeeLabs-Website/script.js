"use strict";


/* =========================================
   BeeLabs Website JavaScript
========================================= */


document.addEventListener("DOMContentLoaded", () => {

    const header = document.querySelector(".site-header");
    const menuButton = document.getElementById("menuButton");
    const navLinksContainer = document.getElementById("navLinks");
    const navigationLinks = document.querySelectorAll(".nav-links a");
    const sections = document.querySelectorAll("main section[id]");
    const revealElements = document.querySelectorAll(".reveal");
    const skillBars = document.querySelectorAll(".skill-bar span");
    const currentYear = document.getElementById("currentYear");


    /* ---------- Current Year ---------- */

    if (currentYear) {
        currentYear.textContent = new Date().getFullYear();
    }


    /* ---------- Header Scroll Effect ---------- */

    const updateHeader = () => {
        if (!header) {
            return;
        }

        header.classList.toggle("scrolled", window.scrollY > 20);
    };

    updateHeader();

    window.addEventListener("scroll", updateHeader, {
        passive: true
    });


    /* ---------- Mobile Menu ---------- */

    const closeMenu = () => {
        if (!menuButton || !navLinksContainer) {
            return;
        }

        menuButton.classList.remove("open");
        navLinksContainer.classList.remove("open");

        menuButton.setAttribute("aria-expanded", "false");
        menuButton.setAttribute(
            "aria-label",
            "Open navigation menu"
        );
    };


    const openMenu = () => {
        if (!menuButton || !navLinksContainer) {
            return;
        }

        menuButton.classList.add("open");
        navLinksContainer.classList.add("open");

        menuButton.setAttribute("aria-expanded", "true");
        menuButton.setAttribute(
            "aria-label",
            "Close navigation menu"
        );
    };


    if (menuButton && navLinksContainer) {

        menuButton.addEventListener("click", () => {

            const menuIsOpen =
                navLinksContainer.classList.contains("open");

            if (menuIsOpen) {
                closeMenu();
            } else {
                openMenu();
            }

        });

    }


    navigationLinks.forEach((link) => {

        link.addEventListener("click", () => {
            closeMenu();
        });

    });


    document.addEventListener("click", (event) => {

        if (!menuButton || !navLinksContainer) {
            return;
        }

        const clickedInsideMenu =
            navLinksContainer.contains(event.target);

        const clickedMenuButton =
            menuButton.contains(event.target);

        if (!clickedInsideMenu && !clickedMenuButton) {
            closeMenu();
        }

    });


    window.addEventListener("resize", () => {

        if (window.innerWidth > 820) {
            closeMenu();
        }

    });


    /* ---------- Reveal Elements on Scroll ---------- */

    const revealObserver = new IntersectionObserver(
        (entries, observer) => {

            entries.forEach((entry) => {

                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add("visible");
                observer.unobserve(entry.target);

            });

        },
        {
            threshold: 0.14,
            rootMargin: "0px 0px -45px 0px"
        }
    );


    revealElements.forEach((element) => {
        revealObserver.observe(element);
    });


    /* ---------- Animate Skill Bars ---------- */

    const skillsSection = document.getElementById("skills");

    if (skillsSection) {

        const skillsObserver = new IntersectionObserver(
            (entries, observer) => {

                entries.forEach((entry) => {

                    if (!entry.isIntersecting) {
                        return;
                    }

                    skillBars.forEach((bar) => {

                        const finalWidth =
                            bar.getAttribute("style");

                        bar.style.width = "0";

                        window.requestAnimationFrame(() => {

                            window.setTimeout(() => {
                                bar.setAttribute(
                                    "style",
                                    finalWidth
                                );
                            }, 120);

                        });

                    });

                    observer.unobserve(entry.target);

                });

            },
            {
                threshold: 0.25
            }
        );

        skillsObserver.observe(skillsSection);

    }


    /* ---------- Highlight Active Navigation Link ---------- */

    const updateActiveNavigation = () => {

        let currentSectionId = "home";
        const scrollPosition = window.scrollY + 160;

        sections.forEach((section) => {

            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;

            const isInsideSection =
                scrollPosition >= sectionTop &&
                scrollPosition < sectionTop + sectionHeight;

            if (isInsideSection) {
                currentSectionId = section.id;
            }

        });


        navigationLinks.forEach((link) => {

            const linkTarget = link.getAttribute("href");

            link.classList.toggle(
                "active",
                linkTarget === `#${currentSectionId}`
            );

        });

    };


    updateActiveNavigation();

    window.addEventListener(
        "scroll",
        updateActiveNavigation,
        {
            passive: true
        }
    );


    /* ---------- Smooth Internal Links ---------- */

    const internalLinks =
        document.querySelectorAll('a[href^="#"]');


    internalLinks.forEach((link) => {

        link.addEventListener("click", (event) => {

            const targetId = link.getAttribute("href");

            if (!targetId || targetId === "#") {
                return;
            }

            const targetElement =
                document.querySelector(targetId);

            if (!targetElement) {
                return;
            }

            event.preventDefault();

            targetElement.scrollIntoView({
                behavior: "smooth",
                block: "start"
            });

        });

    });

});