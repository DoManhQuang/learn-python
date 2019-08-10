def chessBoardCellColor(cell1, cell2):
    for i in range(0,len(cell1)):
        if (ord(cell1[i]) - ord(cell2[i])% 2!=0
            and (int(cell1[i+1])-int(cell1[i+1])) % 2 !=0:
            return True
        return False

