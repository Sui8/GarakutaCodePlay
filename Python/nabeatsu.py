count = int(input("繰り返し回数を入力してください: "))

print("(･`ー･´)「3の倍数と3がつく数字でアホになります」")

for i in range(1, count+1):
    if i % 3 == 0 or "3" in str(i):
        print(f"( ᐛ )    「{i}」")

    else:
        print(f"(･`ー･´) 「{i}」")

print("(ﾟ∀ﾟ)ﾍｰｲ!")
