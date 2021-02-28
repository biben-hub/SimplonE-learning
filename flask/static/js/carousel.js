import Splide from '@splidejs/splide';


new Splide( '.splide' ).mount();

var elms = document.getElementsByClassName( 'splide' );
for ( var i = 0, len = elms.length; i < len; i++ ) {
	new Splide( elms[ i ] ).mount();
}