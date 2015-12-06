var download_folder = process.argv[2];
var start = parseInt(process.argv[3]);
var end = parseInt(process.argv[4]);

var webdriverio = require('webdriverio');
var fs = require('webdriverio');
var options = {
    desiredCapabilities: {
        browserName: 'chrome',
        chromeOptions: {
            args: ['window-size=2880,1800'],
            prefs: { "download.default_directory": download_folder}
        }
    }
};
// "/Users/sameerlal/Documents/NBA_DB/brefcrawler/5man/second/"

player_page = webdriverio
    .remote(options)
    .init()

getLineupData(player_page,start)

function getLineupData(page,i){
    if(i==end){
        return 0;
    }   
    var url_string = 'http://www.basketball-reference.com/play-index/plus/lineup_finder.cgi?request=1&player_id=&match=single&lineup_type=3-man&output=per_poss&year_id=2015&is_playoffs=N&team_id=&opp_id=&game_num_min=0&game_num_max=99&game_month=&game_location=&game_result=&c1stat=&c1comp=ge&c1val=&c2stat=&c2comp=ge&c2val=&c3stat=&c3comp=ge&c3val=&c4stat=&c4comp=ge&c4val=&order_by=diff_pts';
    var url_string_new = "";
    if(i>0){
        url_string_new = url_string + "&order_by_asc=&offset="+i;
    } else {
        url_string_new = url_string;
    }
    player_page.url(url_string_new)
    .execute(function(a){   
        sr_download_data('stats');
        return a;
      },"This worked for "+i).then(function(ret) {
            console.log(ret.value);
            getLineupData(page,i+100);
    }); 
}
