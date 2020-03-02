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
  window.location.href = "profile-KatoMori/index.html";
};

document.getElementById("square-button2").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "profile-kicu/index.html";
};

document.getElementById("square-button3").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "profile-MtF/index.html";
};

document.getElementById("square-button4").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "profile-mori/index.html";
};

document.getElementById("square-button5").onclick = function() {
  this.classList.toggle("blue");
  window.location.href = "profile-takahashi1130/index.html";
};

document.getElementById("square-button6").onclick = function() {
  this.classList.toggle("blue");

  window.location.href = "profile-Tora/index.html";
};
