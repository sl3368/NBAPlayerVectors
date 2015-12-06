var webdriverio = require('webdriverio');
var options = {
    desiredCapabilities: {
        browserName: 'chrome',
        chromeOptions: {
            args: ['window-size=2880,1800'],
            prefs: { "download.default_directory": "/Users/sameerlal/Documents/NBA_DB/brefcrawler"}
        }
    }
};
 
player_page = webdriverio
    .remote(options)
    .init()
    .url('http://www.basketball-reference.com/players/a/anthoca01/gamelog/2015/')
    .execute(function(a){   
        sr_download_data('pgl_advanced');
        return a;
      },"This worked").then(function(ret) {
            console.log(ret.value);
      }); 
