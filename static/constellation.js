$(document).ready(function(){
    $('#gallery').click(function(){
        window.location.href = '/starGallery';
    });

    $('#test').click(function(){
        window.location.href = '/test';
    });

    $('#surprise').click(function(){
        const pages = ['/learning/1', '/learning/2', '/learning/3', '/learning/4'];
        window.location.href = pages[Math.floor(Math.random() * pages.length)];
    });
});
