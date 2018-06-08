
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
          this.increaseCardHeight(e, btn);
        });
      });

    }

  }


  /**
   *
   */
  increaseCardHeight(e, clickedButton) {

    const targetClasses = e.target.previousSibling.childNodes[3].children[1].classList;

    targetClasses.contains('small')
      ? this.increaseCard(targetClasses, clickedButton)
      : this.decreaseCard(targetClasses, clickedButton);

  }

  increaseCard(cardClasses, btn) {
    cardClasses.remove('small');
    btn.text = 'Close';
  }

  decreaseCard(cardClasses, btn) {
    cardClasses.add('small');
    btn.text = 'More';
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
