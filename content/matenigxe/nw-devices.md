---
title: Networking Devices
date: 2026-04-09
---

# Networking Devices

基礎的な Network 機器を自分なりにまとめておく.  
Wireless は一先ずこの記事では措いておくこととする. 

## L1 - Physical Layer -

### Cable

有線の場合, これが無いと始まらない.  
最も身近なのは, Twisted Pair Cable (いわゆる LAN Cable) だろう.  
また最近では, Optical Fiber Cable の重要性も増している.  


### Repeater

Cable だけだと距離を経るごとに信号が減衰してしまうから, 途中途中で増幅する必要がある.  
そういうわけで, 単に増幅するだけの機器がこの Repeater である.  
完全に物理層の機器であり, network の topology など考える上では無視できるだろう. 


### Repeater Hub (Hub, Dumb Hub)

正式名称を Repeater Hub という.  
hub という英単語の意味が分からなければ, 自転車の車輪の中心部を思い浮かべればよい.  
その名の通り, （repeater の機能も持ちつつ, ）配線の分岐や合流に使うことができる.  

単なる repeater と違って network の topology を形作るためのものである.  
とはいえこの機器は, どこかの port から入ってきた信号を他の全 port から出力するだけという, 非常にシンプルな代物であり, collision domain を分割するわけでもない.  
何も考えていないただの物理的な部品に過ぎないので,  L1 に位置づけられる.  

何も考えていないことを強調して, Dumb Hub (バカハブ)と呼ばれたりもする.  
この呼称は, 後述する Switching Hub と区別するための retronym という側面があるように思う. 


## L2 - Data Link Layer -

### Bridge

collision domain を分割するための機器.  
2 つの collision domain にまたがって, MAC address に基づいた制御を行う.  
機能的には, 次に示す Switch の完全下位互換であり, 最近では目にすることは少ない. 


### Switch (SW, Switching Hub, Hub, L2SW)

正式名称を Switching Hub と言う.  
Bridge と同じく collision domain を分割するための機器だが, 一般に Bridge より port 数が多く, また ASIC によるハードウェアレベルでの最適化・高速化も為されているため, Bridge の上位互換である.  
Collision domain を分割しているわけだから, 当然 L1 の Repeater Hub (Dumb Hub) の上位互換でもある.  

というか最近では, 今までに書いた Repeater, Hub, Bridge の全てが Switch に置き換えられつつあると思う.  
さらに, VLAN の制御など, より高度な仕事も担うようになってきており, 超重要な機器である.  

よく SW と略記される. 後述する L3SW と区別するための retronym として, L2SW と呼ばれたりもする.  
この SW のことを単に Hub と呼ぶ人もいるようである. 前述の Repeater Hub を見かけることが最近では殆どないからであろうが, Repeater Hub のことを Hub と呼ぶ人もいるから, 文脈に注意する必要があるだろう. 


## L3 - Network Layer -

### Router (RT) (original meaning)

複数の port によって broadcast domain を分割する機器.  
内部に Routing Table なる table を持っており, packet がやってくるたびに, その dst IP address を自 table で引いて next hop を決定する.  
Routing Table はエンジニアが手動で設定することもあるし, 隣接する他 RT とやり取りして動的に更新することもある.  

### L3 Switch (L3SW)

L3SW の主目的は, 前述の Router を企業 NW のような大規模な LAN 内部で使う際の代替としての存在である.  
port 数が多かったり hardware レベルで最適化されていたりと, そのような用途に特化しているのである.  


### Router (?)

Router には様々な付加的な機能が搭載されたものもある.  
例えば, 

- 複数の segment の境界として, FW 機能. 
- LAN と Internet の境界に置く場合の, NAT/NAPT 変換. 
- LAN 内部の IP 割り当ての統括者とする場合の, DHCP server 機能. 
- 家庭内での無線 LAN 実現のための, AP としての機能. 
- etc. 
  
この場合, もはや本来の Router としての仕事はほんの一部であり, 本来の Router とは別の何かと考えたほうが良いようにさえ思う.  
が, 元々の Router という名前は残り続け, このような機器も依然として Router と呼ばれるし, 私もそう呼んでいる. 　
