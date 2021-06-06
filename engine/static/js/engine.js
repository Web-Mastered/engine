
function darkMode() {
    console.log('Currently in dark mode');
    $( "body" ).removeClass( "bg-light text-dark" );
    $( ".heading-container" ).removeClass( "bg-light text-dark" );
    $( ".content-container" ).removeClass( "bg-light text-dark" );
    $( ".heading-nav" ).removeClass( "navbar-light" );
    $( "body" ).addClass( "bg-dark text-light" );
    $( ".heading-container" ).addClass( "bg-dark text-light" );
    $( ".content-container" ).addClass( "bg-dark text-light" );
    $( ".heading-nav" ).addClass( "navbar-dark" );
}

function lightMode() {
    console.log('Currently in light mode');
    $( "body" ).removeClass( "bg-dark text-light" );
    $( ".heading-container" ).removeClass( "bg-dark text-light" );
    $( ".content-container" ).removeClass( "bg-dark text-light" );
    $( ".heading-nav" ).removeClass( "navbar-dark" );
    $( "body" ).addClass( "bg-light text-dark" );
    $( ".heading-container" ).addClass( "bg-light text-dark" );
    $( ".content-container" ).addClass( "bg-light text-dark" );
    $( ".heading-nav" ).addClass( "navbar-light" );
}

// Handle dark/light mode changes when user enters website
const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)");
if (prefersDarkScheme.matches) {
    darkMode();
} else {
    lightMode();
}

// Handle dark/light mode changes while user is on website
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', event => {
    if (event.matches) {
        darkMode();
  } else {
        lightMode();
    }
});