document.getElementById("show-popup").addEventListener("click",function(){
    document.getElementById("modal").classList.add("open")
})


document.getElementById("close-popupp").addEventListener("click",function(){
    document.getElementById("modal").classList.remove("open")
})


document.addEventListener("click", function(e)       
{
  if_id = e.target. id;
  the_class =e.target.className;
  if(the_class == "but-click")
  {
    if_id = document.getElementById(if_id);
    if(if_id.style.background == "#ffffff")
    {
      if_id.style.background = "#efefef";
    }
    else
    {
      var links = document.querySelectorAll(".but-click");
      links.forEach(link => {
        link.setAttribute("style", "background:#efefef");
      })
      if_id.style.background="#ffffff";
    }
  }
});

document.getElementById("but-click-2").addEventListener("click", function() {
  document.getElementById("show-register").style.display = "none";
});

document.getElementById("but-click-1").addEventListener("click", function() {
  document.getElementById("show-register").style.display = "inline-flex";
});

