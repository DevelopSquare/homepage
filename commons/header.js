class Header extends HTMLElement {
    constructor() {
      super()
      this.innerHTML = `
        <link rel="stylesheet" href="../commons/style/header.css">
        <div class="header-area">
            <div class="header-left">
                <a href="./toppage.html">
                    <img src="../imgs/logo_transparent.png" class="header-logo"  onmousedown="return false;">
                </a>
            </div>
            <div class="header-right">
                <ul>
                    <li>
                        <a href="#about">ABOUT</a>
                    </li>
                    <li>
                        <a href="#member">MEMBER</a>
                    </li>
                    <li>
                        <a href="#products">PRODUCT</a>
                    </li>
                </ul>
            </div>
        </div>
      `;
    }
  }
  
  customElements.define("global-header", Header);