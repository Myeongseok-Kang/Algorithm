import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        ArrayList<String> result = new ArrayList<>();
        HashMap<String,String> matching = new HashMap<>();
        for (String cmd: record){
            String[] cmdList = cmd.split(" ");
            if (cmdList[0].equals("Enter")){
                matching.put(cmdList[1],cmdList[2]);
            }
            else if (cmdList[0].equals("Change")){
                matching.put(cmdList[1],cmdList[2]);
            }
        }
        
        for (String cmd: record){
            String[] cmdList = cmd.split(" ");
            if (cmdList[0].equals("Enter")){
                String name = matching.get(cmdList[1]);
                result.add(name + "님이 들어왔습니다.");
            }
            else if (cmdList[0].equals("Leave")){
                String name = matching.get(cmdList[1]);
                result.add(name + "님이 나갔습니다.");
            }
        }
        String[] answer = result.toArray(new String[0]);
        
        return answer;
    }
}