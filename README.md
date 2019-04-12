## 「5. 子供の帰宅を確認! 玄関あいたら画像をSlack通知 」のサンプルコード

## Install

```
sudo apt-get install fswebcam
pip3 install pyserial
pip3 install timeout-decorator
```

## crontab -e

```
30 21 * * * /home/pi/welcome_back/cron_welcome_back.sh >> /home/pi/welcome_back/log/exec-log 2>&1
```



