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


document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('typewriter-title')) {
        typeWriter('typewriter-title', 'Welcome To My Portfolio', true);
    }
    if (document.getElementById('skills-typewriter-title')) {
        typeWriter('skills-typewriter-title', 'What Do I Bring In', true);
    }
    if (document.getElementById('certificate-title')) {
        typeWriter('certificate-title', 'Some Of My Achievements', true);
    }
    if (document.getElementById('projects-typewriter-title')) {
        typeWriter('projects-typewriter-title', 'Projects I Have Worked On', true);
    }
    if (document.getElementById('contact-title')) {
        typeWriter('contact-title', 'Get In Touch', true);
    }
});

// Contact form submission
document.getElementById("contact_form").addEventListener("submit", async function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("from_email").value;
    const message = document.getElementById("message").value;
  
    if (!name || !email || !message) {
      alert("One or more form fields are missing!");
      console.log(name, email, message);
      return;
    }

    const formData = {
      name: document.getElementById("name").value,
      email: document.getElementById("from_email").value,
      message: document.getElementById("message").value
    };

    console.log("Sending form data:", formData);

    try {
        console.log("Attempting to send request to FastAPI server...");
        const response = await fetch("http://fastapi:8001/contact", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    });
        
        console.log("Response status:", response.status);
        console.log("Response headers:", response.headers);

    const result = await response.json();
    if (!response.ok) {
        throw new Error(result.detail || "Something went wrong");
      }

        const msgEl = document.getElementById("responseMsg");
        msgEl.innerText = result.message;
        msgEl.className = "success show"; // green popup with show class
        msgEl.classList.remove("hidden");

        // Clear form fields after successful submission
        document.getElementById("name").value = "";
        document.getElementById("from_email").value = "";
        document.getElementById("message").value = "";

        // Auto-hide after 5 seconds with smooth fade-out
        setTimeout(() => {
            msgEl.classList.remove("show");
            // Wait for fade-out animation to complete before hiding
            setTimeout(() => {
                msgEl.classList.add("hidden");
            }, 800);
        }, 5000);

    } catch (err) {
        const msgEl = document.getElementById("responseMsg");

        if (err.message === "Wrong email address entered.") {
            msgEl.innerText = "Wrong email address entered.";
        } else {
            msgEl.innerText = "Failed to send message.";
        }
    
        msgEl.className = "error show"; // red popup with show class
        msgEl.classList.remove("hidden");
        // Auto-hide after 5 seconds with smooth fade-out
        setTimeout(() => {
            msgEl.classList.remove("show");
            // Wait for fade-out animation to complete before hiding
            setTimeout(() => {
                msgEl.classList.add("hidden");
            }, 800);
        }, 5000);
    }
  });