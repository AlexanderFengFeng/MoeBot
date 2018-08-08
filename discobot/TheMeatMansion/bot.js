var Discord = require('discord.io');
var logger = require('winston');
var auth = require('./auth.json');

// Configure logger settings
logger.remove(logger.transports.Console);
logger.add(new logger.transports.Console, {
  colorize: true
});
logger.level = 'debug';

// Initialize Discord Bot
var bot = new Discord.Client({
  token: auth.token,
  autorun: true
});

bot.on('ready', function (evt) {
  logger.info('Connected');
  logger.info('Logged in as: ');
  logger.info(bot.username + ' – (' + bot.id + ')');
});

bot.on('message', function (user, userID, channelID, message, evt) {
  if (message.substring(0, 1) == '!') {
    var args = message.substring(1).split(' ');
    var cmd = args[0];

    args = args.splice(1);
    switch(cmd) {
      case 'meat':
        var meats = require('./data/meat.json');
        var animals = ' ';
        for (i in meats['animals']) {
          if (i == meats['animals'].length-1) {
            animals += 'and ' + meats['animals'][i];
            break;
          }
          animals += meats['animals'][i] + ', ';
        }
        bot.sendMessage({
          to: channelID,
          message: 'The meats the mansion have are' + animals + '.'
        }
      );
      break;
    }
  }
});


