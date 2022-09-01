func countMatches(items [][]string, ruleKey string, ruleValue string) int {
 index:=0;if ruleKey=="color" {index=1} else if ruleKey=="name" {index=2};ans:=0;for _,item:=range items {if item[index]==ruleValue {ans++}};return ans
}