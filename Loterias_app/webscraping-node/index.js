const cheerio = require('cheerio');
const request = require('request-promise');

async function ws(){
    const response = await request('http//lotoreal.com.do');
    console.log(response);
}
ws();