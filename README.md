# ardupilot-flightLog
ardupilot App course work

## 概要
飛行記録を自動的に行うアプリケーション
下記項目をcsvファイルに出力する
- FLIGHT DATE: フライト日
- FROM: 離陸場所
- TO: 着陸場所
- OFF TIME: フライト開始時刻（Arm）
- ON TIME: フライト終了時刻（Disarm）
- FLIGHT TIME: フライト時間

## 事前準備
requestsライブラリをインストール
'$pip install requests'

## アプリケーション実行手順
### 1. SITL起動
### 2. アプリケーション起動
'$python flight_log.py'
### 3. 任意にフライトさせる
### 4. フライトを終了すると自動的にログがcsvファイルに出力される
