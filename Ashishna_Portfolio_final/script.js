
window.onload=()=>setTimeout(()=>loader.style.display='none',1200);
const roles=['UI/UX Designer','Web Builder','Design Systems Enthusiast','Automation Learner','Zero2Dev Student'];
let i=0,j=0,d=false,t=document.getElementById('typing');
setInterval(()=>{let w=roles[i];t.textContent=w.slice(0,j);if(!d){j++;if(j>w.length)d=true}else{j--;if(j===0){d=false;i=(i+1)%roles.length}}},100);
themeToggle.onclick=()=>document.body.classList.toggle('light');
const cur=document.getElementById('cursor');
document.addEventListener('mousemove',e=>{cur.style.left=e.clientX+'px';cur.style.top=e.clientY+'px';document.documentElement.style.setProperty('--x',e.clientX+'px');document.documentElement.style.setProperty('--y',e.clientY+'px');});
document.addEventListener('keydown',e=>{if(e.ctrlKey&&e.key==='k'){e.preventDefault();alert('Command Palette')}});
const c=particles,ctx=c.getContext('2d');c.width=innerWidth;c.height=innerHeight;
let p=[...Array(100)].map(()=>({x:Math.random()*c.width,y:Math.random()*c.height,v:1+Math.random()*2}));
(function a(){ctx.clearRect(0,0,c.width,c.height);p.forEach(o=>{ctx.beginPath();ctx.arc(o.x,o.y,2,0,6.28);ctx.fillStyle='#8b5cf6';ctx.fill();o.y+=o.v;if(o.y>c.height)o.y=0});requestAnimationFrame(a)})();
window.addEventListener('scroll',()=>{
    const scrolled=
    (window.scrollY/
    (document.body.scrollHeight-window.innerHeight))*100;

    progressBar.style.width=scrolled+'%';
});
fetch("../projects.json")
    .then(response => response.json())
    .then(projects => {
        const container = document.getElementById("github-projects");

        projects.forEach(project => {
            container.innerHTML += `
                <div class="project-card">
                    <h3>${project.name}</h3>
                    <p>${project.description || "No description"}</p>
                    <a href="${project.url}" target="_blank">
                        View Repository
                    </a>
                </div>
            `;
        });
    });
   fetch("../projects.json")
    .then(response => response.json())
    .then(projects => {
        const container = document.getElementById("github-projects");

        projects.forEach(project => {
            container.innerHTML += `
                <div class="project-card">
                    <h3>${project.name}</h3>
                    <p>${project.description || "No description"}</p>
                    <a href="${project.url}" target="_blank">
                        View Repository
                    </a>
                </div>
            `;
        });
    }); 