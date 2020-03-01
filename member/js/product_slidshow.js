jQuery(function($){
    $('.slider').each(function(){
		$(this).slick({
			autoplay:true,
			autoplaySpeed:5000,
			dots:false,
		});
	});
});


document.getElementById("square-button").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "../profile-KatoMori/html/index.html";
};

document.getElementById("square-button2").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "../profile-kicu/html/index.html";
};

document.getElementById("square-button3").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "../profile-MtF/html/index.html";
};

document.getElementById("square-button4").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "../profile-mori/html/index.html";
};

document.getElementById("square-button5").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "../profile-takahashi1130/html/index.html";
};

document.getElementById("square-button6").onclick = function() {
  this.classList.toggle("blue");
  
  window.location.href = "../profile-Tora/html/index.html";
};