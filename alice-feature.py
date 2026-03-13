"""Alice 的数据处理模块"""

def parse_csv(filepath: str) -> list[dict]:
    """解析 CSV 文件并返回字典列表"""
    import csv
    with open(filepath) as f:
        return list(csv.DictReader(f))

def aggregate(data: list[dict], key: str) -> dict:
    """按指定字段聚合数据"""
    result = {}
    for row in data:
        k = row.get(key, "unknown")
        result[k] = result.get(k, 0) + 1
    return result
