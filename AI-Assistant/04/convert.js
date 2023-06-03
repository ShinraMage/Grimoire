const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('file:///C:/Download/Github/Posetmage/StM4H4/AI-Assistant/04/hw4.html', {waitUntil: 'networkidle2'});
  await page.pdf({path: 'output.pdf', format: 'A4', printBackground: true});

  await browser.close();
})();
