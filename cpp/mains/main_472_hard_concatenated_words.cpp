#include "lc_472_hard_concatenated_words.cpp"

int main() {
    vector<string> arr{"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"};
    auto ans = Solution().findAllConcatenatedWordsInADict(arr);
    std::cout << ans << std::endl;
}
