#$command =  "bot"
#$Command
#cd C:\bot1\bot\ ; git fetch origin master ; git add . ; git commit -m %time% ; git push origin master ; heroku login ; git fetch heroku master ; git push heroku master
Invoke-Expression cd C:\bot1\bot\ ; git fetch origin master ; git add . ; git commit -m %time% ; git push origin master ; heroku login ; git fetch heroku master ; git push heroku master