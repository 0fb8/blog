---
title: Twisted Pair Cable
date: 2026-03-11
---

# Twisted Pair Cable

ノイズキャンセリング機能を搭載したケーブル. 

有線 LAN の de facto standard である Ethernet での活用が有名. 

## mechanism

2本の配線を撚り合わせて 1 対とした上で, 送信側から 2 本の配線が互いに逆位相となるよう信号を送り, 受信側は 2 本の差分として信号を検出する. 外部ノイズがあっても, 理想的には 2 本の配線の両方に均等に作用し, 受信側の差分検出によってその影響がキャンセルされるから, 外部ノイズに対して堅牢である. 

## whether shielded

シールド加工の有無によって, さらに Unshielded Twisted Pair (UTP) と Shielded Twisted Pair (STP) に細分される. 一般家庭ではふつう前者の UTP が用いられる. 後者 STP は当然より高価であり, ノイズの多い工場や研究所といった特殊な環境で使われる. 

## category

対応する規格に応じて CAT5e や CAT6/6A といったカテゴリに分けられる. 数字が大きいほど高性能. 

## use in Ethernet

有線 LAN の de facto standard である Ethernet では, 8 本の銅線の 2 本ずつを対にした, 4 対の信号路から為る Twisted Pair Cable が使われる. その両端には 8P8C (RJ-45) と呼ばれる専用のコネクタを取り付ける. 

### Straight-Through vs Crossover

コネクタは機器側のポートに接続する. ポートには送信専用のものと受信専用のものがあり, その配置は機器の種類によって異なる. 
PC や router では MDI と呼ばれる配置が, switch や hub では MDI-X と呼ばれる配置が用いられている. 

同種の配置を持つ機器同士を繋げる際は, Crossover を使わないと, 送信用同士・受信用同士が繋がることになり, 意味を為さない. 
逆に異種の形式同士を繋げる際は, Straight-Through を使えばよい. （MDI と MDI-X がそのような関係を持っている. 当初は PC と hub を Straight-Through のケーブルで接続できるというメリットに期待して, このような 2 種類の配置形式という概念が考案されたのだろう. ）

結局従来は人間がポートを都度確認してケーブルを選ぶ必要があったが, 近年のポートは賢く, Auto MDI/MDI-X という技術によって相手ポートに応じた柔軟な切り替えを自動で行う. この機能は 1000BASE-T (Gigabit Ethernet) 以降の規格で必須要件となっており, 今後人間が Straight-Through か Crossover かを気にする場面は少なくなっていくであろう. 