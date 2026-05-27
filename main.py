import pandas as pd

keyword_database = {
    "ANOVA": {
        "中文名稱": "變異數分析",
        "解釋": "用來檢定不同組別平均數是否存在顯著差異的統計方法。",
        "應用情境": "常用於實驗設計、品質管理與製程分析。"
    },
    "Regression": {
        "中文名稱": "迴歸分析",
        "解釋": "用來分析自變數與應變數之間關係的統計方法。",
        "應用情境": "可用於預測、趨勢分析與因果關係探討。"
    },
    "Optimization": {
        "中文名稱": "最佳化",
        "解釋": "在限制條件下尋找最佳決策方案的方法。",
        "應用情境": "常用於排程、物流路徑規劃與生產管理。"
    },
    "Supply Chain": {
        "中文名稱": "供應鏈",
        "解釋": "從原料、生產、運輸到消費者之間的整體流程。",
        "應用情境": "常用於物流管理、庫存控制與企業營運分析。"
    },
    "Machine Learning": {
        "中文名稱": "機器學習",
        "解釋": "讓電腦從資料中學習規則並進行預測或分類的技術。",
        "應用情境": "可用於需求預測、品質檢測與智慧製造。"
    }
}

def load_keywords(filename="keywords.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def generate_cards(keywords):
    results = []

    for keyword in keywords:
        if keyword in keyword_database:
            data = keyword_database[keyword]
            results.append({
                "Keyword": keyword,
                "中文名稱": data["中文名稱"],
                "解釋": data["解釋"],
                "應用情境": data["應用情境"]
            })
        else:
            results.append({
                "Keyword": keyword,
                "中文名稱": "未建立資料",
                "解釋": "目前資料庫尚未收錄此關鍵字。",
                "應用情境": "請自行補充。"
            })

    return results

def main():
    keywords = load_keywords()
    cards = generate_cards(keywords)

    df = pd.DataFrame(cards)
    df.to_csv("output.csv", index=False, encoding="utf-8-sig")

    print("已成功產生 output.csv")

if __name__ == "__main__":
    main()
