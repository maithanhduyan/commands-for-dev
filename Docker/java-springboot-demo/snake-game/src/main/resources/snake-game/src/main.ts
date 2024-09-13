import './style.css'
import typescriptLogo from './typescript.svg'
import viteLogo from '/vite.svg'
import { setupCounter } from './counter.ts'

// document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
//   <div>
//     <a href="https://vitejs.dev" target="_blank">
//       <img src="${viteLogo}" class="logo" alt="Vite logo" />
//     </a>
//     <a href="https://www.typescriptlang.org/" target="_blank">
//       <img src="${typescriptLogo}" class="logo vanilla" alt="TypeScript logo" />
//     </a>
//     <h1>Vite + TypeScript</h1>
//     <div class="card">
//       <button id="counter" type="button"></button>
//     </div>
//     <p class="read-the-docs">
//       Click on the Vite and TypeScript logos to learn more
//     </p>
//   </div>
// `

// setupCounter(document.querySelector<HTMLButtonElement>('#counter')!)

import { Game } from './classes/Game';
import { Console } from './classes/Console';

document.addEventListener(
  'DOMContentLoaded',
  () => {
    const noscripts = document.getElementsByClassName('noscript');
    while (noscripts.length > 0) {
      noscripts[0].parentNode?.removeChild(noscripts[0]);
    }
    const game = new Game();
    game.initialize();
    Console.log('Game Ready!');
  },
  false
);
