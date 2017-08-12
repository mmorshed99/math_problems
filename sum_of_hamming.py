def hammingDistance(self, A):
        def bitwise_dist(A,B):
            a_str = bin(A)
            b_str = bin(B)
            a_lst = list(a_str)
            b_lst = list(b_str)
            a_lst = a_lst[2: ]
            b_lst = b_lst[2: ]
            count = 0
            if len(a_lst) != len(b_lst):
                if len(a_lst) >  len(b_lst):
                   x_small = b_lst
                   x_big = a_lst
                elif len(a_lst) < len(b_lst):
                   x_small = a_lst
                   x_big = b_lst
                diff_len = len(x_big) - len(x_small)
                for i in range(0,len(x_big)):
                    if i < diff_len:
                        if int(x_big[i]) != 0:
                          count += 1
                    else:
                      if int(x_big[i]) != int(x_small[i-diff_len]):
                          count += 1
            else:
              for i in range(0,len(a_lst)):
                 if int(a_lst[i]) != int(b_lst[i]):
                     count += 1
            return count
        count = 0
        my_sum_track = {}
        #for i in range(0,999999):
        #my_sum_track.append(-1)
        for i in range(0,len(A)):
           for j in range(0,len(A)):
             if A[i] == A[j]:
                  continue
             max_num = max(A[i],A[j])
             min_num = min(A[i],A[j])
             if str(max_num)+str(min_num) in my_sum_track.keys():
                 count += my_sum_track[str(max_num)+str(min_num)]
                 continue
             #print("I am in")
             my_sum_track[str(max_num)+str(min_num)] = bitwise_dist(max_num,min_num)
             #count += bitwise_dist(max_num,min_num)
             count += my_sum_track[str(max_num)+str(min_num)]
        return count % 1000000007     
