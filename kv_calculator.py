import json

def calculate_kv_cache(config_path, seq_len, precision_bytes=2):
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # 提取參數
    n_layers = config.get("num_hidden_layers", 0)
    # 考量 GQA/MQA，優先找 KV heads，找不到則與 Query heads 相同
    n_kv_heads = config.get("num_key_value_heads", config.get("num_attention_heads", 0))
    hidden_size = config.get("hidden_size", 0)
    n_heads = config.get("num_attention_heads", 1)
    head_dim = hidden_size // n_heads
    
    # 判斷 SWA
    swa_window = config.get("sliding_window", None)
    is_swa = swa_window is not None
    
    # 如果是 SWA 模型，實際計算長度受限於 Window Size
    effective_seq_len = min(seq_len, swa_window) if is_swa else seq_len
    
    # 公式計算 (Bytes)
    # 2 (K and V) * layers * kv_heads * head_dim * precision * seq_len
    total_bytes = 2 * n_layers * n_kv_heads * head_dim * precision_bytes * effective_seq_len
    
    # 轉換成 MiB
    total_mib = total_bytes / (1024 * 1024)
    
    return is_swa, total_mib

# 測試用
config_file = "test_config.json" 
is_swa, mib = calculate_kv_cache(config_file, 32768)
print(f"Is SWA: {is_swa}, KV Cache Size: {mib:.2f} MiB")