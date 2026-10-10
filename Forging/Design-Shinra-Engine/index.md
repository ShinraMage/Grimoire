---
layout: page/note/slides
title: 設計Shinra-Engine心路歷程
---

## 設計Shinra-Engine心路歷程


## Theory1: 真正的資產是「產生結果的能力」

一般人擁有結果（房子、車子、包包）。

有錢人擁有系統（工廠、廠房、公司）。

數位時代的工廠 = 能大量生成內容的系統。

## Theory2:真正的生產力來自消耗大量算力

中世紀：鋁比黃金貴，因為提煉難。

現代：鋁箔紙隨處可見，因為電解法。

AI 時代：寫程式變便宜，能消耗更多 Token 的人 = 更高階生產者。

卡達肖夫指數

## Theory3: 軟體將成為下一個流量入口

知識：教會 → 印刷 → 網路

影片：電影院 → DVD → YouTube → AI 生成

文章：部落格 → YouTuber → 軟體

當軟體製作成本趨近於零，軟體本身就是流量入口。

## 結論

根據以上三個理論

創造一個工廠系統，無限消耗token，生成軟體的人 是未來的資產持有者

## 限制

大量用AI生產，會快速累積大量技術債

AI會寫垃圾


## 解方

根據第一性原理：AI會寫垃圾

設計出 "限制爆炸範圍"


## 實驗1: 統一後端

概念：激進的GraphQL

產出：LC(Lattice-Cast)

原理：pg GIN idx on jsonb with RLS

| workspace_id | table_id | row | jsonb |
| --- | --- | --- | --- |
| 1 | 1 | 1 | `{"type":"user","name":"Alice","roles":["admin"]}` |
| 1 | 1 | 2 | `{"type":"order","id":101,"status":"paid"}` |
| 1 | 1 | 3 | `{"type":"product","sku":"KB01","tags":["usb","keyboard"]}` |
| 1 | 1 | 4 | `{"type":"log","level":"error","service":"api"}` |
| 1 | 3 | 1 | `{"type":"payment","amount":500,"status":"failed"}` |
| 1 | 3 | 2 | `{"type":"sensor","temp":27.4,"room":"A7"}` |
| 2 | 4 | 1 | `{"name":"Alice","roles":["admin"]}` |
| 2 | 4 | 2 | `{"order_id":101,"status":"paid"}` |
| 2 | 5 | 1 | `{"sku":"KB01","price":999}` |
| 2 | 6 | 1 | `{"level":"error","service":"api"}` |
| 2 | 7 | 1 | `{"device":"T01","temp":27.4}` |

pg做得比mongoDB好： 

<div class="embed_youtube" yt-title=" 为什么关系数据库的挑战者都没有好下场【让编程再次伟大#25】 " yt-url="IUUpxfa1SSw" yt-width="700">Loading content...</div>


## 嘗試1: 成果

好處：AI可以隨意揮灑前端

不只有我想到這solution:

開源系統「Medusa」
這是號稱開源的shopify，它採用的是Headless Commerce，也就是無頭式電商。

意思是他的前台跟後台是分開的，你的前台可以是html也可以是自己蓋的任何系統，後台提供api給你串接傳遞訂單數據。
前台可以非常自由的設計，可以是官網、可以是一頁式購物，也可以是任何天馬行空的做法，最後只要傳遞對的資料給後台就可以成立訂單。

## 結論1: 第一性原理

LC是基於以下第一性原理的產物
* AI會寫垃圾，所以需要限制爆炸半徑
* 任何想法重點在於實驗驗證速度，LC是快速迭代的方法論
* 客戶無法 Crystallize Domain Know-how，所以需要FDE

## LC湧現
LC可以做不同的前端app統一後台 再也不用寫BE
* 爬蟲後台，ex: 591租屋爬蟲用的閱覽器
* AHLC(Agentic-Hive+Lattice-Cast)，可以讓不同AI協作的框架 ex: codex as Queen,  hermes+deepseek as Bee
* 日歷復盤系統
* SEO文章生成器
* ....

## 實驗2: game engine:

我要能hot replacement

gametok終於開始嘗試


## 嘗試2-1: 自製DSL


## 嘗試2-2: SE in vsc

<video controls preload="metadata" style="max-width: 100%;">
  <source src="sh-vsc.mp4" type="video/mp4">
  您的瀏覽器不支援內嵌影片播放。
</video>

遇到問題:
* 開發困難 進度遲緩


## 嘗試2-3: SE in tui

已經有雛形


## 嘗試2-4 重構:

設計成MVC-like

* bundle.so(data.rs, buffer.rs)
* game.so(control)
* ecs.so(data pipeline)
* render.so(render pipeline)
* asset.so(model meterial)

遇到問題

## 嘗試2-5 MCDV:

rust ABI not stable

hecs not friendly to wasm

最終以wasm作為基礎 做了 MCDV

* contract.wit
* asset.wasm
* game.wasm
* data.wasm
* render.wasm

![MCDV：由 contract.wit 固定組件契約，並讓可替換的 wasm 組件構成管線](mcdv-pipeline.svg)
