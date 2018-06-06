
class HomePage {
  constructor() {

    this.overlay = document.querySelector('.overlay');

    document.addEventListener('DOMContentLoaded', () => {
      this.animateOverlay();
    });
  }

  init() {
    console.log('homepage init');

  }

  animateOverlay() {
    setTimeout(() => {
      this.overlay.classList.remove('hidden');
    }, 1000);
  }
}

export default new HomePage();
