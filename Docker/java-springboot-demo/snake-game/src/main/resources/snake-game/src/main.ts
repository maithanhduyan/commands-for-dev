import './style.css'
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
