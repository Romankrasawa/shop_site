const catalog = document.querySelector('.catalog__list');
const catalog__crossBtn = document.querySelector('.catalog__cross-btn');
const catalog__btn = document.querySelector('.header__catalog-btn');

catalog__btn.addEventListener('click', function() {
    catalog.classList.add('catalog__list-toggle-class');
});

catalog__crossBtn.addEventListener('click', function() {
    catalog.classList.remove('catalog__list-toggle-class');
})