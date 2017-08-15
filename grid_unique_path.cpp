//A robot is located at the top-left corner of an A x B grid
//The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked ‘Finish’ in the diagram below).
//
//How many possible unique paths are there?
//
//Input : A = 2, B = 2
//Output : 2
//
//2 possible routes : (0, 0) -> (0, 1) -> (1, 1) 
//              OR  : (0, 0) -> (1, 0) -> (1, 1)
//
int save[500][500];
int my_grid(int st_a,int st_b,int A,int B){
    if (st_a < 0 or st_b < 0) {
       return 0; }
    if (st_a == 0 and st_b == 0) {
       return 1;  }
    if (save[st_a][st_b] > -1) {
     return save[st_a][st_b];  }
    save[st_a][st_b] = my_grid(st_a-1,st_b,A,B) + my_grid(st_a,st_b-1,A,B);
    return save[st_a][st_b];
                                           }
int Solution::uniquePaths(int A, int B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    memset(save,-1,sizeof(save));
    return my_grid(A-1,B-1,A,B);
    
                                          }
