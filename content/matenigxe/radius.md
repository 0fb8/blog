---
title: RADIUS
date: 2026-04-09
---

# RADIUS

**RADIUS** とは, **C/S による一元的な AAA 管理**を実現する, L7 protocol である.  
RADIUS packet は header 部分と可変長の Attribute-Value Pair (AVP) 部分からなるのだが, RADIUS 最大の特徴は, この AVP 部をエンジニアが柔軟に設計できることと, それに伴う拡張性・汎用性の高さだろう.  
実際, （名称が Remote Authentication Dial-In User Service の acronym であることから分かるように, ）元々 RADIUS とは電話回線での利用を想定して開発されたものなのだが, 現在は LAN の認証 protocol である IEEE 802.1X での利用のほうが有名なくらいである.  


## AAA

AAA とは, network security で必要な機能を Authentication, Authorization, Accounting の 3 要素に分けて考えるモデル・フレームワークである.   

**Authentication (AuthN)**: 本当にその人自身なのか（他人のなりすましではないか）検証する. 日本語では認証.  
**Authorization (AuthZ)**: その人が何をできるかという, 権限の制御. 日本語では認可.  
**Accounting**: その人がいつ何をしたかなど記録する. 日本語では何故か「課金」と訳されることもあるが, 別に金銭的なやり取りと直接の関係がある概念ではないため, 少なくとも頭の中では, accounting という英語のまま理解するほうが良いだろう.  

なお RADIUS は, AAA という考え方が出てくる前に開発されたものであり, protocol レベルで 3 要素を切り分けてサポートしているわけではない. 後述の RADIUS Code を見れば分かるが, RADIUS が提供する主なサービスは「Access」なるものと「Accounting」であり, このうち前者は, AAA でいう AuthN と AuthZ がごっちゃになったものである.  


## RADIUS packet

RADIUS packet の構造はシンプルである.  

0. Code (1 byte): packet の種類を表す.  
    - `Access-Request` (1): client からの認証要求
    - `Access-Accept` (2): server からの許可
    - `Access-Reject` (3): server からの拒否
    - `Accounting-Request` (4)
    - `Accounting-Response` (5)
    - etc.
1. Identifier (1 byte): request と response を対応させるための ID.  
2. Length (2 bytes): packet 全体の長さ  
3. Authenticator (16 bytes): RADIUS 自身の security に関連する.   
4. Attribute-Value Pairs (variable-length)  
   

## RadSec

オリジナルの RADIUS は UDP 1812, 1813 port 上で動く.  
RADIUS 自身の security を確保するために, Authenticator field や AVP の一部を活用した工夫も為されてきた. 
ところが, 詳細は割愛するが, どうもそれだけでは不十分な場面もあったようだ.  
計算資源も充実してきた現代においては, RADIUS をまるごと TLS で包んでしまう **RadSec** が, より安全な選択肢として注目・期待されている.  

