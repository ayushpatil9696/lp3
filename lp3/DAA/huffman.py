import heapq
from collections import Counter

def huffman_encoding(data):
    # Count frequency of each character in data
    freq_map = Counter(data)
    
    # Initialize priority queue with frequency and character
    priority_queue = [[freq, [char, ""]] for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)

    # Build Huffman tree
    while len(priority_queue) > 1:
        lo = heapq.heappop(priority_queue)  # Pop the two nodes of the lowest frequency
        hi = heapq.heappop(priority_queue)
        
        # Append '0' and '1' to the existing bit string
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        
        # Push the new node back into the priority queue
        heapq.heappush(priority_queue, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Extract Huffman codes
    huffman_codes = {char: code for char, code in heapq.heappop(priority_queue)[1:]}
    
    # Encode the data
    encoded_data = ''.join([huffman_codes[char] for char in data])
    
    return encoded_data, huffman_codes

# Test driver code
if __name__ == "__main__":
    data = "Mississippi"
    
    # Perform Huffman encoding
    encoded_data, huffman_codes = huffman_encoding(data)
    
    print("Encoded:", encoded_data)
    print("Codes:", huffman_codes)

# TIME COMPLEXITY IS O(nlogn)
# SPACE COMPLEXITY IS O(n)