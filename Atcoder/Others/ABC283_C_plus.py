#ABC283-C 000ボタンを追加してみた
s = input()

ans = len(s)
ans -= (s.count("000")*2) #000ボタンの処理
s = s.replace("000", "") #000の削除
ans -=s.count("00") #00ボタンの処理

print(ans)