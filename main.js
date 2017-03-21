function main(){
var $skillset=$('.subheading');
$skillset.hide();
$('.skillset').fadeIn(1000);
$('.projects').hide();
$('.subheading-button').on('click',function(){
$(this).next().slideToggle(1000);
$(this).toggleClass('active');});
$('.subheading').on('click',function(){
$(this).slideToggle(1000);
$(this).toggleClass('active');
});




}

$(document).ready(main);