class Solution:
    def find(self,i,j,board,word,idx):
        rows = len(board)
        cols = len(board[0])
        if idx >= len(word):
            return True
        if i+1<rows and board[i+1][j] == word[idx]:
            board[i+1][j] = "$"
            if self.find(i+1,j,board,word,idx+1):
                return True
            else:
                board[i+1][j] = word[idx]
        if i-1>=0 and board[i-1][j] == word[idx]:
            board[i-1][j] = "$"
            if self.find(i-1,j,board,word,idx+1):
                return True
            else:
                board[i-1][j] = word[idx]
        if j+1<cols and board[i][j+1] == word[idx]:
            board[i][j+1] = "$"
            if self.find(i,j+1,board,word,idx+1):
                return True
            else:
                board[i][j+1] = word[idx]
        if j-1>=0 and board[i][j-1] == word[idx]:
            board[i][j-1] = "$"
            if self.find(i,j-1,board,word,idx+1):
                return True
            else:
                board[i][j-1] = word[idx]
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    board[i][j] = "$"
                    if self.find(i,j,board,word,1):
                        return True
                    else:
                        board[i][j] = word[0]

        return False
