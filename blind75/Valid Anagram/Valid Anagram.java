class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        HashMap<Character, Integer> counter = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            Character character = s.charAt(i);
            counter.put(character, counter.getOrDefault(character, 0) + 1);
        }

        for (int i = 0; i < t.length(); i++){
            Character character = t.charAt(i);
            if(counter.get(character) == null || counter.get(character) == 0){
                return false;
            }
            
            counter.put(character, counter.get(character) - 1);
        }

        return true;
    }
}
