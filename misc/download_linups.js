var webdriverio = require('webdriverio');
var fs = require('fs');
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

url_string = 'http://www.basketball-reference.com/play-index/plus/lineup_finder.cgi?request=1&player_id=&match=single&lineup_type=4-man&output=per_poss&year_id=2015&is_playoffs=N&team_id=&opp_id=&game_num_min=0&game_num_max=99&game_month=&game_location=&game_result=&c1stat=&c1comp=ge&c1val=&c2stat=&c2comp=ge&c2val=&c3stat=&c3comp=ge&c3val=&c4stat=&c4comp=ge&c4val=&order_by=diff_pts'

player_page.url(url_string)
    .execute(function(a){   
        sr_download_data('stats');
        return a;
      },"This worked1").then(function(ret) {
            console.log(ret.value);
            while(!fs.existsSync('play-index_plus_lineup_finder.cgi_stats.csv')){
            }
            fs.rename('play-index_plus_lineup_finder.cgi_stats.csv', 'helloworld'+i+'.csv', function(err) {
                  if ( err ) console.log('ERROR: ' + err);
            });
            console.log("renamed file1");
    }); 
url_string = 'http://www.basketball-reference.com/play-index/plus/lineup_finder.cgi?request=1&player_id=&match=single&lineup_type=4-man&output=per_poss&year_id=2015&is_playoffs=N&team_id=&opp_id=&game_num_min=0&game_num_max=99&game_month=&game_location=&game_result=&c1stat=&c1comp=ge&c1val=&c2stat=&c2comp=ge&c2val=&c3stat=&c3comp=ge&c3val=&c4stat=&c4comp=ge&c4val=&order_by=diff_pts'

for( i =0; i<200; i+100){
    if(i>0){
        url_string_new = url_string+'&order_by_asc=&offset='+i;
    } else {
        url_string_new = url_string;
    }
    player_page.url(url_string_new)
    .execute(function(a){   
        sr_download_data('stats');
        return a;
      },"This worked1").then(function(ret) {
            console.log(ret.value);
            while(!fs.existsSync('play-index_plus_lineup_finder.cgi_stats.csv')){
            }
            fs.rename('play-index_plus_lineup_finder.cgi_stats.csv', 'helloworld'+i+'.csv', function(err) {
                  if ( err ) console.log('ERROR: ' + err);
            });
            console.log("renamed file1");
    }); 
}
