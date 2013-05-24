DATE=`/bin/date +%Y-%m-%d-%H-%M`
echo "time is: $DATE"

python mockUserInterests.py
mv mock_user_interests.xls $DATE.xls
echo "interest report"  | /home/wendui/sendmail/sendmail.sh \
 yongkaixie@wendui.com "initial interest report: $DATE" /home/wendui/scripts/python/$DATE.xls


