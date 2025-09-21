$(document).ready(function() {
    $('#mobile_btn').on('click', function () {
        $('#mobile_menu').toggleClass('active');
        $('#mobile_btn').find('i').toggleClass('fa-x');
    });
})



// Carrossel 1 e 2 Landing


function initializeCarousel(trackId, prevBtnId, nextBtnId) {
    const track = document.getElementById(trackId);
    if (!track) return;

    const slides = Array.from(track.children);
    const nextButton = document.getElementById(nextBtnId);
    const prevButton = document.getElementById(prevBtnId);

    const initialIndexDesktop = Math.floor(slides.length / 2);
    let currentIndex = window.innerWidth <= 768 ? 0 : initialIndexDesktop;
    let isMobile = window.innerWidth <= 768;

    function updateSliderPosition() {
        if (slides.length === 0) return;

        const nowMobile = window.innerWidth <= 768;

        if (nowMobile && !isMobile) {
            currentIndex = 0;
        } else if (!nowMobile && isMobile) {
            currentIndex = initialIndexDesktop;
        }

        isMobile = nowMobile;

        const slideWidth = slides[0].getBoundingClientRect().width;
        const trackStyle = window.getComputedStyle(track);
        const gap = parseFloat(trackStyle.gap) || 40;

        const wrapperWidth = track.parentElement.getBoundingClientRect().width;
        const offset = (wrapperWidth / 2) - (slideWidth / 2);
        const newTransform = -currentIndex * (slideWidth + gap) + offset;

        track.style.transform = `translateX(${newTransform}px)`;

        slides.forEach((slide, index) => {
            slide.classList.toggle('active', index === currentIndex);
        });
    }

    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % slides.length;
        updateSliderPosition();
    });

    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        updateSliderPosition();
    });

    slides.forEach((slide, index) => {
        slide.addEventListener('click', () => {
            if (currentIndex !== index) {
                currentIndex = index;
                updateSliderPosition();
            }
        });
    });

    window.addEventListener('resize', updateSliderPosition);

    setTimeout(updateSliderPosition, 100);
}

document.addEventListener('DOMContentLoaded', function() {
    initializeCarousel('track-1', 'prev-btn-1', 'next-btn-1');
    initializeCarousel('track-2', 'prev-btn-2', 'next-btn-2');
});