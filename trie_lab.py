class TrieNode:
    def __init__(self):
        # 使用字典存儲子節點：key 是字元，value 是 TrieNode 物件
        self.children = {}
        # 標記此節點是否為某個單字的結尾
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """在 Trie 中插入一個字串 word"""
        node = self.root
        for char in word:
            # 如果字元不在當前節點的子節點中，就建立新節點
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # 走完字串後，將最後一個節點標記為單字結尾
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """判斷字串 word 是否存在於 Trie 中"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        # 必須走完路徑，且該節點被標記為結尾才算找到完整單字
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """判斷是否有任何字串以 prefix 為開頭"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        # 只要能順利走完 prefix 的路徑，就代表存在以此為開頭的單字
        return True

# --- 投影片測試範例 ---

# 初始化 Trie
trie = Trie()

# 插入字串
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("band")

# 測試 search 功能
assert trie.search("apple") == True
assert trie.search("app") == True
assert trie.search("appl") == False

# 測試 starts_with 功能
assert trie.starts_with("app") == True
assert trie.starts_with("ban") == True
assert trie.starts_with("band") == True
assert trie.starts_with("bat") == False

print("所有測試案例皆已通過！")