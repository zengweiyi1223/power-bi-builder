import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ headless: true, executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe' });
const page = await browser.newPage({ viewport: { width: 1140, height: 1500 } });
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
await page.goto(pathToFileURL(path.join(root, 'cards.html')).href, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
const cards = await page.locator('.card').evaluateAll((nodes) => nodes.map((card) => {
  const outer = card.getBoundingClientRect();
  const footer = card.querySelector('.footer').getBoundingClientRect();
  const content = [...card.children].filter((element) => !element.classList.contains('footer'));
  const last = content.reduce((current, element) => element.getBoundingClientRect().bottom > current.getBoundingClientRect().bottom ? element : current, content[0]).getBoundingClientRect();
  const overflowing = [...card.querySelectorAll('*')].filter((element) => {
    const style = getComputedStyle(element);
    if (style.display === 'none' || style.visibility === 'hidden') return false;
    const box = element.getBoundingClientRect();
    return box.left < outer.left - 1 || box.right > outer.right + 1 || box.top < outer.top - 1 || box.bottom > outer.bottom + 1;
  }).map((element) => `${element.tagName.toLowerCase()}.${element.className}`);
  return { name: card.dataset.name, page: card.querySelector('.author-meta span')?.textContent.trim(), footerGap: Number((footer.top - last.bottom).toFixed(1)), overflowing };
}));
const brokenImages = await page.evaluate(() => [...document.images].filter((img) => !img.complete || img.naturalWidth === 0).map((img) => img.getAttribute('src')));
await browser.close();
const jpgFiles = (await fs.readdir(path.join(root, 'jpg'))).filter((name) => /\.jpe?g$/i.test(name)).sort();
const expectedPages = cards.map((_, index) => `${String(index + 1).padStart(2, '0')} / ${String(cards.length).padStart(2, '0')}`);
const pageMismatch = cards.filter((card, index) => card.page !== expectedPages[index]);
const cardFailures = cards.filter((card) => card.overflowing.length || card.footerGap < 40);
const result = { errors, brokenImages, pageMismatch, cardFailures, jpgFiles };
console.log(JSON.stringify(result, null, 2));
if (errors.length || brokenImages.length || pageMismatch.length || cardFailures.length || jpgFiles.length !== cards.length) process.exitCode = 1;
