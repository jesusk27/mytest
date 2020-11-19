const pupperteer = require('pupperteer');
async function scrapeProduct(URL){
    const browser = await pupperteer.launch();
    const page = await browser.newPage();
    await page.goto(URL);
    
    const[el]= await page.$x('//*[@id="rc-loteria-real"]/div[1]/table/tbody/tr/td/table/tbody/tr/td[2]/div[2]');
    const src= await el.getProperty('src');
    const bolosTxt = await src.jsonvalue();
    
   console.log({bolosTxt});
    
    browser.close();
}

    scrapeProduct('https//www.lotoreal.com.do');
    
