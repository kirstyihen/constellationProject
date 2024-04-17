$(document).ready(function(){
    $('#gallery').click(function(){
        window.location.href = '/starGallery';
    });

    $('#quiz').click(function(){
        window.location.href = '/quiz';
    });

    $('#quiz-button').click(function(){
        const id = 0;
        window.location.href = '/quiz/' + id;
    });

    $('#surprise').click(function(){
        const pages = ['/learning/1', '/learning/2', '/learning/3', '/learning/4'];
        window.location.href = pages[Math.floor(Math.random() * pages.length)];
    });
});
