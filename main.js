let editor;

/* ----- NAVIGATION BAR FUNCTION ----- */
function myMenuFunction() {
  var menuBtn = document.getElementById("myNavMenu");

  if (menuBtn.className === "nav-menu") {
    menuBtn.className += " responsive";
  } else {
    menuBtn.className = "nav-menu";
  }
}

/* ----- ADD SHADOW ON NAVIGATION BAR WHILE SCROLLING ----- */
window.onscroll = function () { headerShadow() };

function headerShadow() {
  const navHeader = document.getElementById("header");

  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {

    navHeader.style.boxShadow = "0 1px 6px rgba(0, 0, 0, 0.1)";
    navHeader.style.height = "70px";
    navHeader.style.lineHeight = "70px";

  } else {

    navHeader.style.boxShadow = "none";
    navHeader.style.height = "90px";
    navHeader.style.lineHeight = "90px";

  }
}


/* ----- TYPING EFFECT ----- */
var typingEffect = new Typed(".typedText", {
  strings: ["Software Engineer", "Curriculum Developer", "Technical Trainer"],
  loop: true,
  typeSpeed: 100,
  backSpeed: 80,
  backDelay: 2000
})


/* ----- ## -- SCROLL REVEAL ANIMATION -- ## ----- */
const sr = ScrollReveal({
  origin: 'top',
  distance: '80px',
  duration: 2000,
  reset: true
})

/* -- HOME -- */
sr.reveal('.featured-text-card', {})
sr.reveal('.featured-name', { delay: 100 })
sr.reveal('.featured-text-info', { delay: 200 })
sr.reveal('.featured-text-btn', { delay: 200 })
sr.reveal('.social_icons', { delay: 200 })
sr.reveal('.featured-image', { delay: 300 })


/* -- PROJECT BOX -- */
sr.reveal('.project-box', { interval: 200 })

/* -- HEADINGS -- */
sr.reveal('.top-header', {})

/* ----- ## -- SCROLL REVEAL LEFT_RIGHT ANIMATION -- ## ----- */

/* -- ABOUT INFO & CONTACT INFO -- */
const srLeft = ScrollReveal({
  origin: 'left',
  distance: '80px',
  duration: 2000,
  reset: true
})

srLeft.reveal('.about-info', { delay: 100 })
srLeft.reveal('.contact-info', { delay: 100 })

/* -- ABOUT SKILLS & FORM BOX -- */
const srRight = ScrollReveal({
  origin: 'right',
  distance: '80px',
  duration: 2000,
  reset: true
})

srRight.reveal('.skills-box', { delay: 100 })
srRight.reveal('.form-control', { delay: 100 })



/* ----- CHANGE ACTIVE LINK ----- */

const sections = document.querySelectorAll('section[id]')

function scrollActive() {
  const scrollY = window.scrollY;

  sections.forEach(current => {
    const sectionHeight = current.offsetHeight,
      sectionTop = current.offsetTop - 50,
      sectionId = current.getAttribute('id')

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {

      document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.add('active-link')

    } else {

      document.querySelector('.nav-menu a[href*=' + sectionId + ']').classList.remove('active-link')

    }
  })
}

window.addEventListener('scroll', scrollActive)

/* ----- Email Function Hire Button ----- */

function sendEmail() {
  window.location.href = "mailto:yosola@gmail.com";
}

// Data for the projects
const projects = [
  {
    title: "Next.JS Course with TechConMe",
    description: "Designed and taught a hands-on course on building dynamic web applications using Next.js, covering topics such as routing, authentication, and state management.",
    skills: ["Next.js", "React", "JavaScript", "Auth0", "FireBase"],
    link: "https://github.com/Yosolita1978/Conference-Landing?tab=readme-ov-file#nextjs-course-overview",
    youtubeLink: "https://www.youtube.com/playlist?list=PLH72tRyNBul4xwHGPuduuoUuQ1b2qz1Bc"
  },
  {
    title: "Social Media Avatar Creation Workshop with Stable Diffusion",
    description: "Led a workshop on creating personalized social media avatars using Stable Diffusion v1.5, covering image generation techniques, model tuning, and artistic enhancement.",
    skills: ["Stable Diffusion", "Machine Learning", "Image Generation", "Python"],
    link: "https://github.com/Yosolita1978/AiWorkshop",
    youtubeLink: "https://www.youtube.com/watch?v=szc4FA7nyBo"
  },
  {
    title: "Your First Express and React App with Vite",
    description: "Built a full-stack web application template using React for the frontend and Express for the backend, leveraging Vite for rapid development and database integration.",
    skills: ["React", "Express", "Vite", "Full-Stack Development", "Database Integration"],
    link: "https://github.com/Techtonica/Template2023ReactAndVite",
    youtubeLink: "https://youtu.be/Oj1L3BuIJuw"
  }
];

// Function to create project cards
function createProjectCards() {
  const grid = document.getElementById('projects-grid');

  projects.forEach(project => {
    const card = document.createElement('div');
    card.classList.add('card');

    const cardHeader = document.createElement('div');
    cardHeader.classList.add('card-header');

    const cardTitle = document.createElement('h3');
    cardTitle.classList.add('card-title');
    cardTitle.innerHTML = `${project.title}`;
    cardHeader.appendChild(cardTitle);

    const cardDescription = document.createElement('p');
    cardDescription.classList.add('card-description');
    cardDescription.textContent = project.description;
    cardHeader.appendChild(cardDescription);

    const cardContent = document.createElement('div');
    cardContent.classList.add('card-content');

    const skillWrapper = document.createElement('div');
    skillWrapper.classList.add('skill-wrapper');
    project.skills.forEach(skill => {
      const badge = document.createElement('span');
      badge.classList.add('badge');
      badge.textContent = skill;
      skillWrapper.appendChild(badge);
    });
    cardContent.appendChild(skillWrapper);

    if (project.link) {
      const link = document.createElement('a');
      link.classList.add('project-link');
      link.href = project.link;
      link.target = '_blank';
      link.innerHTML = `View Project on GitHub`;
      cardContent.appendChild(link);
    }

    if (project.youtubeLink) {
      const youtubeLink = document.createElement('a');
      youtubeLink.classList.add('project-link');
      youtubeLink.href = project.youtubeLink;
      youtubeLink.target = '_blank';
      youtubeLink.innerHTML = `Watch Project on YouTube`;
      cardContent.appendChild(youtubeLink);
    }

    card.appendChild(cardHeader);
    card.appendChild(cardContent);
    grid.appendChild(card);
  });
}

// Initialize the project cards
createProjectCards();
