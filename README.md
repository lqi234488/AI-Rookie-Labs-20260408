# AI Rookie 2026 Labs - Po-hung's Work

## Lab 1: Environment Setup
- Compiled `llama.cpp` with CUDA 12.4 support in a Docker container.
- Resolved library dependency issues (libmtmd.so.0) via containerization.

## Lab 2: KV Cache & Agent Implementation
- Deployed `llama-server` with Qwen2.5-3B-Instruct.
- Implemented a Law Consulting Agent using System Prompts.
- Verified **KV Cache Reuse**; observed significant TTFT reduction on repeated long-context queries.

## Lab 3: KV Cache Calculator
- Developed a Python tool to estimate VRAM usage for GQA & SWA models.

## Lab 4: Trie Data Structure
- Implemented a Trie (Prefix Tree) to simulate the core logic of Prefix Caching.

## Lab 5: RAG Vector Retrieval
- Built a vector search engine using Cosine Similarity for semantic document retrieval.
