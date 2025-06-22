
// JavaScript to create and color pixel grid
const container = document.getElementById('pixel-container');
const screenWidth = 1028;
const screenHeight = 720;

for (let y = 0; y < screenHeight; y++) {
    for (let x = 0; x < screenWidth; x++) {
        const pixel = document.createElement('div');
        pixel.style.width = '1px';
        pixel.style.height = '1px';
        pixel.style.float = 'left';
        pixel.style.backgroundColor = `rgb(${x % 256}, ${y % 256}, ${(x * y) % 256})`;
        container.appendChild(pixel);
    }
}
