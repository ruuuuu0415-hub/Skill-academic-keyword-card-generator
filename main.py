import pandas as pd

keyword_database = {
    "ANOVA": {
        "中文名稱": "變異數分析",
        "解釋": "用來檢定不同組別平均數是否存在顯著差異的統計方法。",
        "應用情境": "常用於實驗設計與品質管理。"
    }
}

keywords = ["ANOVA"]

results = []

for keyword in keywords:
    data = keyword_database[keyword]

    results.append({
        "Keyword": keyword,
        "中文名稱": data["中文名稱"],
        "解釋": data["解釋"],
        "應用情境": data["應用情境"]
    })

df = pd.DataFrame(results)

df.to_csv("output.csv", index=False, encoding="utf-8-sig")

print("成功產生 output.csv")
