const imageInput = document.getElementById('imageInput');
const widthSlider = document.getElementById('widthSlider');
const widthValue = document.getElementById('widthValue');
const modeSelect = document.getElementById('modeSelect');
const themeSelect = document.getElementById('themeSelect');
const bgColor = document.getElementById('bgColor');
const textColor = document.getElementById('textColor');
const equalizeCheckbox = document.getElementById('equalizeCheckbox');
const invertCheckbox = document.getElementById('invertCheckbox');
const supersampleCheckbox = document.getElementById('supersampleCheckbox');
const generateBtn = document.getElementById('generateBtn');
const sourceCanvas = document.getElementById('sourceCanvas');
const originalCanvas = document.getElementById('originalCanvas');
const outputCanvas = document.getElementById('outputCanvas');
const comparisonContainer = document.querySelector('.comparison-container');
const divider = document.querySelector('.divider');
const asciiText = document.getElementById('asciiText');
const copyBtn = document.getElementById('copyBtn');
const downloadBtn = document.getElementById('downloadBtn');

const sourceCtx = sourceCanvas.getContext('2d');
const originalCtx = originalCanvas.getContext('2d');
const outputCtx = outputCanvas.getContext('2d');

const RAMPS = {
    contrast: ' .:-=+*#%@',
    smooth: ' .,;:clodxkOKXNWM#@',
    minimal: ' .:#',
    detailed: ' .\'`^",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$',
    blocks: ' ░▒▓█'
};

const THEMES = {
    dark:     { bg: '#0d0d1a', text: '#e0e0e0' },
    terminal: { bg: '#0a0a0a', text: '#00ff00' },
    amber:    { bg: '#1a1200', text: '#ffb000' },
    matrix:   { bg: '#000000', text: '#00ff41' },
    light:    { bg: '#f5f5f5', text: '#1a1a1a' },
    custom:   null
};

const FONT_SIZE = 10;
const LINE_HEIGHT = 10;

let loadedImage = null;
let isDragging = false;

imageInput.addEventListener('change', handleImageUpload);
widthSlider.addEventListener('input', updateWidthDisplay);
themeSelect.addEventListener('change', applyTheme);
bgColor.addEventListener('input', switchToCustom);
textColor.addEventListener('input', switchToCustom);
generateBtn.addEventListener('click', generate);
copyBtn.addEventListener('click', copyToClipboard);
downloadBtn.addEventListener('click', downloadPng);

divider.addEventListener('mousedown', startDrag);
divider.addEventListener('touchstart', startDrag);
document.addEventListener('mousemove', drag);
document.addEventListener('touchmove', drag);
document.addEventListener('mouseup', stopDrag);
document.addEventListener('touchend', stopDrag);

function handleImageUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const img = new Image();
    img.onload = function() {
        loadedImage = img;
        generateBtn.disabled = false;
    };
    img.src = URL.createObjectURL(file);
}

function updateWidthDisplay() {
    widthValue.textContent = widthSlider.value;
}

function applyTheme() {
    const theme = THEMES[themeSelect.value];
    if (theme) {
        bgColor.value = theme.bg;
        textColor.value = theme.text;
    }
}

function switchToCustom() {
    themeSelect.value = 'custom';
}

function generate() {
    if (!loadedImage) return;

    const charWidth = parseInt(widthSlider.value);
    const charHeight = Math.floor(charWidth * (loadedImage.height / loadedImage.width) * 0.5);
    const sampleScale = supersampleCheckbox.checked ? 3 : 1;

    sourceCanvas.width = charWidth * sampleScale;
    sourceCanvas.height = charHeight * sampleScale;
    sourceCtx.drawImage(loadedImage, 0, 0, charWidth * sampleScale, charHeight * sampleScale);

    const imageData = sourceCtx.getImageData(0, 0, charWidth * sampleScale, charHeight * sampleScale);
    const pixels = imageData.data;

    if (equalizeCheckbox.checked) {
        equalizeHistogram(pixels);
    }

    const ascii = buildAsciiString(pixels, charWidth, charHeight, sampleScale);
    asciiText.value = ascii;

    const canvasWidth = charWidth * FONT_SIZE * 0.6;
    const canvasHeight = charHeight * LINE_HEIGHT;

    renderOriginalToCanvas(canvasWidth, canvasHeight);
    renderToCanvas(ascii, charWidth, charHeight, canvasWidth, canvasHeight);

    comparisonContainer.hidden = false;
    setDividerPosition(50);
    copyBtn.hidden = false;
    downloadBtn.hidden = false;
}

function equalizeHistogram(pixels) {
    const histogram = new Array(256).fill(0);
    const totalPixels = pixels.length / 4;

    for (let i = 0; i < pixels.length; i += 4) {
        const brightness = Math.floor(0.299 * pixels[i] + 0.587 * pixels[i + 1] + 0.114 * pixels[i + 2]);
        histogram[brightness]++;
    }

    const cdf = new Array(256);
    cdf[0] = histogram[0];
    for (let i = 1; i < 256; i++) {
        cdf[i] = cdf[i - 1] + histogram[i];
    }

    let cdfMin = 0;
    for (let i = 0; i < 256; i++) {
        if (cdf[i] > 0) {
            cdfMin = cdf[i];
            break;
        }
    }

    const lookup = new Array(256);
    for (let i = 0; i < 256; i++) {
        lookup[i] = Math.round(((cdf[i] - cdfMin) / (totalPixels - cdfMin)) * 255);
    }

    for (let i = 0; i < pixels.length; i += 4) {
        const brightness = Math.floor(0.299 * pixels[i] + 0.587 * pixels[i + 1] + 0.114 * pixels[i + 2]);
        const scale = brightness > 0 ? lookup[brightness] / brightness : 1;

        pixels[i] = Math.min(255, Math.floor(pixels[i] * scale));
        pixels[i + 1] = Math.min(255, Math.floor(pixels[i + 1] * scale));
        pixels[i + 2] = Math.min(255, Math.floor(pixels[i + 2] * scale));
    }
}

function buildAsciiString(pixels, width, height, sampleScale) {
    const invert = invertCheckbox.checked;
    const baseRamp = RAMPS[modeSelect.value];
    const ramp = invert ? baseRamp : baseRamp.split('').reverse().join('');
    const rampLength = ramp.length;
    const canvasWidth = width * sampleScale;

    let result = '';

    for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
            let brightness;

            if (sampleScale === 1) {
                const i = (y * canvasWidth + x) * 4;
                const r = pixels[i];
                const g = pixels[i + 1];
                const b = pixels[i + 2];
                brightness = 0.299 * r + 0.587 * g + 0.114 * b;
            } else {
                let totalBrightness = 0;
                for (let sy = 0; sy < sampleScale; sy++) {
                    for (let sx = 0; sx < sampleScale; sx++) {
                        const pixelX = x * sampleScale + sx;
                        const pixelY = y * sampleScale + sy;
                        const i = (pixelY * canvasWidth + pixelX) * 4;
                        const r = pixels[i];
                        const g = pixels[i + 1];
                        const b = pixels[i + 2];
                        totalBrightness += 0.299 * r + 0.587 * g + 0.114 * b;
                    }
                }
                brightness = totalBrightness / (sampleScale * sampleScale);
            }

            const charIndex = Math.floor((brightness / 255) * (rampLength - 1));
            result += ramp[charIndex];
        }
        result += '\n';
    }

    return result;
}

function renderOriginalToCanvas(width, height) {
    originalCanvas.width = width;
    originalCanvas.height = height;
    originalCtx.drawImage(loadedImage, 0, 0, width, height);
}

function renderToCanvas(ascii, charWidth, charHeight, canvasWidth, canvasHeight) {
    outputCanvas.width = canvasWidth;
    outputCanvas.height = canvasHeight;

    outputCtx.fillStyle = bgColor.value;
    outputCtx.fillRect(0, 0, canvasWidth, canvasHeight);

    outputCtx.fillStyle = textColor.value;
    outputCtx.font = `${FONT_SIZE}px "Courier New", monospace`;
    outputCtx.textBaseline = 'top';

    const lines = ascii.split('\n');
    for (let i = 0; i < lines.length; i++) {
        outputCtx.fillText(lines[i], 0, i * LINE_HEIGHT);
    }
}

function startDrag(event) {
    event.preventDefault();
    isDragging = true;
}

function drag(event) {
    if (!isDragging) return;

    const containerRect = comparisonContainer.getBoundingClientRect();
    const clientX = event.touches ? event.touches[0].clientX : event.clientX;
    const position = clientX - containerRect.left;
    const percentage = (position / containerRect.width) * 100;
    const clampedPercentage = Math.min(100, Math.max(0, percentage));

    setDividerPosition(clampedPercentage);
}

function stopDrag() {
    isDragging = false;
}

function setDividerPosition(percentage) {
    divider.style.left = percentage + '%';
    outputCanvas.style.clipPath = 'inset(0 0 0 ' + percentage + '%)';
}

function copyToClipboard() {
    navigator.clipboard.writeText(asciiText.value).then(function() {
        const originalText = copyBtn.textContent;
        copyBtn.textContent = 'Copied!';
        setTimeout(function() {
            copyBtn.textContent = originalText;
        }, 2000);
    });
}

function downloadPng() {
    const link = document.createElement('a');
    link.download = 'ascii-art.png';
    link.href = outputCanvas.toDataURL('image/png');
    link.click();
}