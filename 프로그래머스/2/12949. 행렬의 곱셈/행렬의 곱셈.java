class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = new int[arr1.length][arr2[0].length];
        int r1 = arr1.length;
        int c1 = arr1[0].length;
        int r2 = arr2.length;
        int c2 = arr2[0].length;
        
        for (int i = 0; i<r1; i++){
            for (int j = 0; j<c2; j++){
                answer[i][j] = 0;
                for (int k = 0; k<c1; k++){
                    answer[i][j] += (arr1[i][k] * arr2[k][j]);
                }
            }
        }
                    
        return answer;
    }
}