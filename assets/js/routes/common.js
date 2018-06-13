
class Common {
  constructor() {

    this.readMore = [].slice.call((document.querySelectorAll('.read-more')));
  }


  /**
   *
   */
  init() {
    console.log('common init');

    this.addEventListeners();
  }


  /**
   *
   */
  addEventListeners() {

    if (this.readMore) {

      this.readMore.forEach(btn => {
        btn.addEventListener('click', (e) => {
          this.changeCardHeight(e, btn);
        });
      });

    }

  }


  /**
   *
   */
  changeCardHeight(e, clickedButton) {

    const targetClasses = e.target.previousSibling.childNodes[3].children[1].classList;

    console.log(e);

    const screenScrolled = e.srcElement.offsetTop;

    targetClasses.contains('small')
      ? this.increaseCard(targetClasses, clickedButton, screenScrolled)
      : this.decreaseCard(targetClasses, clickedButton, screenScrolled);

  }

  increaseCard(cardClasses, btn, windowHeight) {
    cardClasses.remove('small');
    btn.text = 'Close';

    window.scroll(0, windowHeight);
  }

  decreaseCard(cardClasses, btn, windowHeight) {
    cardClasses.add('small');
    btn.text = 'More';

    window.scroll(0, windowHeight);
  }


  /**
   *
   */
  removeEventListeners() {

    if (this.readMore) {
      this.readMore.forEach(btn => {
        btn.removeEventListener('click', () => {});
      });
    }

  }


  /**
   *
   */
  finalize() {
    this.removeEventListeners();
  }
}

export default new Common();
