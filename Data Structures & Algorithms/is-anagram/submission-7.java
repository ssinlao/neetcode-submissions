class Solution {
    public boolean isAnagram(String s, String t) {
        // make two hashmaps counting word freq
        // compare two hashmaps
        HashMap<Character, Integer> map_s = new HashMap<>();
        HashMap<Character, Integer> map_t = new HashMap<>();

        for (char c: s.toCharArray()){
            map_s.put(c, map_s.getOrDefault(c, 0) + 1);
        }
            
        for (char c: t.toCharArray()) {
            map_t.put(c, map_t.getOrDefault(c, 0) + 1);
        }  
        return map_s.equals(map_t);
    }
}
