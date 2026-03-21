# EAF 2026 Trade Journal

這是 EAF Investment Competition 2026 的個人交易日誌與分析工具，由我（John）負責管理 30% 流動倉位（trade 部分）。

**重要聲明**：本 repo 僅用於記錄、分析、生成報告與 rationale，**絕不自動執行交易**。所有下單均手動在 IBKR TWS 平台完成，符合比賽規則（僅交易 HK 和 US 市場）。

## 專案目的
- 系統化記錄每筆 trade 的 rationale、風險管理、執行過程、盈虧與反思。
- 輔助撰寫中期報告（4月3日截止）和最終 presentation。
- 與隊友協作：70% portfolio 由其他兩位負責，30% trade 由我管理。

## 目錄結構
- trades/ → 每筆交易一個 .md 文件，使用 template_trade.md 作為模版
- analysis/ → Python 腳本（風險計算、每日匯報等）
- reports/ → 中期報告與 presentation 草稿
- images/ → TWS 截圖、股價圖

## 使用方法
1. 每筆新 trade：在 trades/ 新建文件，copy template_trade.md 填寫。
2. 每周復盤：更新持倉狀態、反思。
3. 周一開盤前：檢查計劃、調整止損/止盈。

## 目前持倉摘要（2026年3月21日）
- BCRX: 1,000 股 @ 9.80 USD → 現價 10.05 USD (+2.42%)
- 02546.HK: 3,000 股 @ 15.63 HKD → 現價 14.82 HKD (-3.14%)

持續更新中...

## 團隊分工
- 70% Portfolio：長期價值 + 防禦配置（隊友負責）
- 30% Trade：短期事件驅動 + 動能機會（我負責）

MIT License - 僅供個人與團隊使用。
