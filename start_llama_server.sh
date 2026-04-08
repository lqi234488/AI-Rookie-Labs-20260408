./build/bin/llama-server \
  -m qwen2.5-3b-instruct-q4_k_m.gguf \
  -ngl 100 \
  -c 32768 \
  --host 0.0.0.0 \
  --port 8081
