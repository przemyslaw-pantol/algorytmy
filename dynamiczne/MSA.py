import numpy as np

def smith_waterman(seq_1, seq_2, match=1, missmatch=-1, gap=-2):
    rows, cols = len(seq_1) + 1, len(seq_2) + 1
    score_matrix = np.zeros((rows, cols), dtype=int)
    
    for i in range(1, rows):
        for j in range(1, cols):
        
            if seq_1[i - 1] == seq_2[j - 1]:
                diagonal_score = score_matrix[i - 1][j - 1] + match
            else:
                diagonal_score = score_matrix[i - 1][j - 1] + missmatch
            
            top = score_matrix[i - 1][j] + gap
            left = score_matrix[i][j - 1] + gap
            score_matrix[i][j] = max(0, diagonal_score, top, left)

    return score_matrix

print(smith_waterman("TATGA", "TACGA"))
