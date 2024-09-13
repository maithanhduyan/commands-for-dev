// src/classes/Console.ts
export class Console {
    static log(message: string) {
        const consoleElement = document.getElementById('console');
        if (consoleElement) {
            const p = document.createElement('p');
            p.style.wordWrap = 'break-word';
            p.innerHTML = message;
            consoleElement.appendChild(p);
            while (consoleElement.childNodes.length > 25) {
                consoleElement.removeChild(consoleElement.firstChild!);
            }
            consoleElement.scrollTop = consoleElement.scrollHeight;
        }
    }
}
