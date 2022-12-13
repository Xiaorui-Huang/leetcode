#include "lc_139_medium_word_break.cpp"

int main() {
    vector<string> wordDict{"apple", "pen"};
    string s = "applepenapple";
    auto ans = Solution().wordBreak(s, wordDict);
    std::cout << std::boolalpha << ans << std::endl;
}
