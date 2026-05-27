# AI 學術關鍵字卡產生器

## 專案簡介

本專案是一個代表個人學習與報告準備流程的自動化工具。  
使用者只需要在 `keywords.txt` 中輸入學術或課堂常見關鍵字，程式即可自動產生中文名稱、解釋與應用情境，並輸出為 `output.csv`。

## 專案目的

在準備課堂報告或期末作業時，學生常需要整理大量專業術語。  
若每個名詞都手動查詢與整理，容易耗時且格式不一致。  
因此本作品透過 Python 建立一個關鍵字卡片產生器，協助使用者快速完成術語整理。

## 核心功能

1. 讀取 `keywords.txt` 關鍵字清單
2. 自動比對內建學術詞彙資料庫
3. 產生中文名稱、解釋與應用情境
4. 輸出成 `output.csv`
5. 可用 Excel 開啟，也可延伸匯入 Anki 或 Quizlet

## 專案檔案

```text
Skill-academic-keyword-card-generator/
│
├── README.md
├── main.py
├── requirements.txt
├── keywords.txt
└── skill.md

## 網頁展示

本作品已製作成可直接操作的 GitHub Pages 網頁工具。  
使用者可輸入學術關鍵字，系統會自動產生中文名稱、名詞解釋、應用情境與報告可用句型。

GitHub Pages 連結：

https://ruuuuu0415-hub.github.io/Skill-academic-keyword-card-generator/
