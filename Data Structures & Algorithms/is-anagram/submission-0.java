class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] s_Array = s.toCharArray();
        char[] t_Array = t.toCharArray();
        Arrays.sort(s_Array);
        Arrays.sort(t_Array);
        return Arrays.equals(s_Array, t_Array);
    }
}
