import random

# 0=qoya, 1=qogʻoz, 2=qaychi
map_ = {'qoya':0, 'qogʻoz':1, 'qaychi':2}
inv = {v:k for k,v in map_.items()}
ps = cs = 0

print("Kim birinchi 5 ochko to‘plasa — g‘olib.")

for _ in range(1000):            # yetarli urinish chegarasi
    if ps==5 or cs==5: break

    p = input("Tanlang: ").strip().lower()
    if p not in map_:
        print("Noto‘g‘ri!\n"); continue

    c = random.randint(0,2)
    print("Kompyuter:", inv[c])

    d = (map_[p] - c) % 3
    if   d==0: print("Durrang!\n")
    elif d==1: print("Siz yutdingiz!\n"); ps+=1
    else:      print("Kompyuter yutdi!\n"); cs+=1

    print(f"Siz {ps} — Kompyuter {cs}\n")

print("🎉 Siz yutdingiz!" if ps==5 else "😞 Kompyuter yutdi.")
