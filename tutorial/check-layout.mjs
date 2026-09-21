import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({
  headless: true,
  executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
});

const checks = [];
for (const width of [1440, 1024, 390]) {
  const page = await browser.newPage({ viewport: { width, height: 900 } });
  const errors = [];
  page.on('pageerror', (error) => errors.push(error.message));
  await page.goto(pathToFileURL(path.join(root, 'index.html')).href, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const result = await page.evaluate(() => ({
    scrollWidth: document.documentElement.scrollWidth,
    clientWidth: document.documentElement.clientWidth,
    brokenImages: [...document.images].filter((img) => !img.complete || img.naturalWidth === 0).map((img) => img.getAttribute('src')),
  }));
  checks.push({ page: 'index', width, errors, ...result });
  await page.close();
}

const cardPage = await browser.newPage({ viewport: { width: 1140, height: 1500 } });
await cardPage.goto(pathToFileURL(path.join(root, 'xhs', 'cards.html')).href, { waitUntil: 'load' });
await cardPage.evaluate(() => document.fonts.ready);
const cards = await cardPage.locator('.card').evaluateAll((nodes) => nodes.map((card) => {
  const outer = card.getBoundingClientRect();
  const overflowing = [...card.querySelectorAll('*')]
    .filter((element) => {
      const style = getComputedStyle(element);
      if (style.display === 'none' || style.visibility === 'hidden') return false;
      const box = element.getBoundingClientRect();
      return box.left < outer.left - 1 || box.right > outer.right + 1 || box.top < outer.top - 1 || box.bottom > outer.bottom + 1;
    })
    .map((element) => `${element.tagName.toLowerCase()}.${element.className}`);
  return { name: card.dataset.name, overflowing };
}));
const brokenCardImages = await cardPage.evaluate(() => [...document.images].filter((img) => !img.complete || img.naturalWidth === 0).map((img) => img.getAttribute('src')));
await browser.close();

const failures = checks.filter((check) => check.errors.length || check.scrollWidth > check.clientWidth || check.brokenImages.length);
const cardFailures = cards.filter((card) => card.overflowing.length);
console.log(JSON.stringify({ checks, brokenCardImages, cardFailures }, null, 2));
if (failures.length || brokenCardImages.length || cardFailures.length) process.exitCode = 1;
