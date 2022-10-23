class Footer extends HTMLElement {
    constructor() {
      super()
      this.innerHTML = `
        <link rel="stylesheet" href="../commons/style/footer.css">
        <div class="footer">
            <a href="https://twitter.com/DevelopSquare">
                <img src="../imgs/twittericon.png" alt="twitter_icon" class="icon">
            </a>
        </div>
      `;
    }
  }
  
  customElements.define("global-footer", Footer);