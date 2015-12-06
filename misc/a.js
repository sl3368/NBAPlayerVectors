
var client = require("webdriverio").remote({
    desiredCapabilities: {
        browserName: 'chrome',
        chromeOptions: {
            args: ['window-size=2880,1800'],
            prefs: { "download.default_directory": "/Users/sameerlal/Documents/NBA_DB/brefcrawler"}
        }
    }
})

client.init()
    .url('http://www.basketball-reference.com/players/a/anthoca01/gamelog/2015/');
