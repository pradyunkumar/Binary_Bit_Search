import time

def file_to_list(f) -> list:
    byte = f.read(1)
    l = []
    while byte:
        l.append(list(byte)[0])
        byte = f.read(1)

    return l

def max_equal_subl(l1, l2):
    n = len(l1)
    m = len(l2)
    max_len = 0
    offset_i = 0
    offset_j = 0
 
    seq_len = [[0 for i in range(n + 1)] for i in range(m + 1)]
 
    # Updating the dp[][] table
    # in Bottom Up approach
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
 
            # If A[i] is equal to B[i]
            # then dp[j][i] = dp[j + 1][i + 1] + 1
            if l1[i] == l2[j]:
                seq_len[j][i] = seq_len[j + 1][i + 1] + 1
            
            if seq_len[j][i] > max_len:
                max_len = seq_len[j][i]
                offset_i = i
                offset_j = j

    return max_len, offset_i, offset_j

def max_total_subl(l_tot):
    max_tot_len = 0
    files_offsets = {}
    for i in range(10):
        for j in range(i + 1, 10):
            l, o1, o2 = max_equal_subl(l_tot[i], l_tot[j])
            if max_tot_len < l:
                max_tot_len = l
                files_offsets = {f'sample{i}': o1, f'sample{j}': o2}
            elif max_tot_len == l:
                files_offsets[f'sample{i}'] = o1
                files_offsets[f'sample{j}'] = o2
    
    return max_tot_len, files_offsets

def main():
    list_bytes = []
    start_time = time.time()
    for i in range(1, 11):
        with open(f"sample.{i}", "rb") as f: 
            list_bytes.append(file_to_list(f))

    # locations, strand_length = byte_reader(file_list)
    totlen, files_offsets = max_total_subl(list_bytes)
    written = [f"{key} at {files_offsets[key]}" for key in files_offsets]
    print(f"Max Length: {totlen} appears in {written}")
    print(f"Time Taken: {time.time() - start_time} seconds")
    # print(f"Longest byte strand is of length {strand_length} and is present at: {[l.name for l in locations]}")

if __name__ == "__main__":
    main()