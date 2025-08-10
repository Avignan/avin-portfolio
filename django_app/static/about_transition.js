document.addEventListener('DOMContentLoaded', function() {
    const aboutTitle = document.getElementById('about-title');
    const aboutImg = document.querySelector('.about-img');
    const aboutDesc = document.querySelector('.about-desc');
    if (aboutTitle) {
        aboutTitle.classList.add('visible');
        typeWriter('about-title', 'About Me', true);
    }
    if (aboutImg) {
        aboutImg.classList.add('visible');
    }
    if (aboutDesc) {
        aboutDesc.classList.add('visible');
    }
});

// General typewriter effect for any element and text
function typeWriter(elementId, text, loop = false) {
    const el = document.getElementById(elementId);
    if (!el) return;
    let i = 0;
    let isDeleting = false;
    function typeWriterLoop() {
        if (!isDeleting && i <= text.length) {
            el.textContent = text.substring(0, i);
            i++;
            if (i > text.length) {
                if (loop) {
                    setTimeout(() => { isDeleting = true; typeWriterLoop(); }, 1200);
                }
            } else {
                setTimeout(typeWriterLoop, 120);
            }
        } else if (isDeleting && i >= 0) {
            el.textContent = text.substring(0, i);
            i--;
            if (i < 0) {
                isDeleting = false;
                setTimeout(typeWriterLoop, 600);
            } else {
                setTimeout(typeWriterLoop, 60);
            }
        } else if (!loop && i > text.length) {
            el.textContent = text;
        }
    }
    typeWriterLoop();
}
