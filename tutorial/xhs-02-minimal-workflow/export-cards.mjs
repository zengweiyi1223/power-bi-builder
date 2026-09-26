import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';
import fs from 'node:fs/promises';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = path.dirname(fileURLToPath(import.meta.url));
const outputDir = path.join(root, 'jpg');
await fs.mkdir(outputDir, { recursive: true });
const oldImages = (await fs.readdir(outputDir, { withFileTypes: true }))
  .filter((entry) => entry.isFile() && /\.jpe?g$/i.test(entry.name));
await Promise.all(oldImages.map((entry) => fs.rm(path.join(outputDir, entry.name))));

const browser = await chromium.launch({ headless: true, executablePath: 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe' });
const page = await browser.newPage({ viewport: { width: 1140, height: 1500 }, deviceScaleFactor: 1 });
await page.goto(pathToFileURL(path.join(root, 'cards.html')).href, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
const cards = page.locator('.card');
for (let index = 0; index < await cards.count(); index += 1) {
  const card = cards.nth(index);
  const name = await card.getAttribute('data-name');
  await card.screenshot({ path: path.join(outputDir, `${name}.jpg`), type: 'jpeg', quality: 94 });
}
await browser.close();
console.log(`Exported ${await fs.readdir(outputDir).then((items) => items.length)} cards to ${outputDir}`);
