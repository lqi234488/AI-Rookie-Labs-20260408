import numpy as np

def parse_vector_file(file_path):
    vectors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            
            # 1. 處理 "1. [0.12, ...]" 這種格式
            # 先拿掉編號 (找第一個 '[' 的位置)
            start_idx = line.find('[')
            end_idx = line.find(']')
            
            if start_idx != -1 and end_idx != -1:
                # 抓出括號內的內容: "0.12, 0.34, 0.88..."
                vec_str = line[start_idx + 1 : end_idx]
                # 用逗號分割並轉成 float
                vec = [float(x.strip()) for x in vec_str.split(',')]
                vectors.append(vec)
    return np.array(vectors)

def cosine_similarity_batch(query_vec, db_vectors):
    dot_product = np.dot(db_vectors, query_vec)
    norm_query = np.linalg.norm(query_vec)
    norm_db = np.linalg.norm(db_vectors, axis=1)
    # 避免分母為 0
    return dot_product / (norm_query * norm_db + 1e-9)

# 1. 讀取資料
queries = parse_vector_file('query.txt')
db_vectors = parse_vector_file('vector_db.txt')

# 2. 針對每個 query 進行 Top-4 檢索
K = 4
print(f"--- Lab 5 RAG Retrieval Results (Top-{K}) ---")

for idx, q_vec in enumerate(queries):
    scores = cosine_similarity_batch(q_vec, db_vectors)
    top_indices = np.argsort(scores)[::-1][:K]
    
    print(f"\nQuery {idx + 1}: {list(q_vec)}")
    for i in top_indices:
        # 注意：DB Index 我們顯示跟檔案一樣從 1 開始，所以是 i + 1
        print(f"  -> DB Item {i + 1} | Similarity Score: {scores[i]:.4f}")