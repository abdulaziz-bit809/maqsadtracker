#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""19. Maqsadlar Tracker"""
import json, os
class Goals:
    def __init__(self):
        self.file = "goals.json"
        self.data = json.load(open(self.file)) if os.path.exists(self.file) else []
    def save(self):
        json.dump(self.data, open(self.file,"w"), ensure_ascii=False, indent=2)
    def add(self, title, target, unit, deadline):
        self.data.append({"title":title,"target":target,"current":0,"unit":unit,"deadline":deadline}); self.save(); print("✅")
    def update(self, idx, val):
        self.data[idx]["current"] += val; self.save()
        g = self.data[idx]
        print(f"{g['title']}: {g['current']/g['target']*100:.1f}%")
    def show(self):
        for i,g in enumerate(self.data):
            print(f"{i}. {g['title']}: {g['current']}/{g['target']} {g['unit']}")
def main():
    g = Goals()
    while True:
        print("\n1.Qoshish 2.Progress 3.Royxat 4.Chiqish")
        c = input("> ")
        if c=="1": g.add(input("Maqsad: "), float(input("Target: ")), input("Birlik: "), input("Muddat: "))
        elif c=="2": g.show(); g.update(int(input("Index: ")), float(input("Qiymat: ")))
        elif c=="3": g.show()
        elif c=="4": break
if __name__ == "__main__": main()
