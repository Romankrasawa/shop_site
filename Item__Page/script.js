const catalog = document.querySelector('.catalog__list');
const catalog__crossBtn = document.querySelector('.catalog__cross-btn');
const catalog__btn = document.querySelector('.header__catalog-btn');

catalog__btn.addEventListener('click', function() {
    catalog.classList.add('catalog__list-toggle-class');
});

catalog__crossBtn.addEventListener('click', function() {
    catalog.classList.remove('catalog__list-toggle-class');
})



const feedback__openBtn = document.querySelector('.user-feedback__btn');

feedback__openBtn.addEventListener('click', function() {
    const feedback__div = document.querySelector('.feedback-box');

    feedback__div.classList.remove('feedback-box-display');
})


const feedback__closeBtn = document.querySelector('.feedback__close-btn');

feedback__closeBtn.addEventListener('click', function() {
    const feedback__div = document.querySelector('.feedback-box');

    feedback__div.classList.add('feedback-box-display');
})
