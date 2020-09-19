var webdriver = require('selenium-webdriver');
var browser = new webdriver.Builder().usingServer().withCapabilities({'browserName': 'chrome' }).build();
browser.get('https://google.com');
browser.findElement(webdriver.By.name('q')).sendKeys('Vasanthan Muthuvel');
