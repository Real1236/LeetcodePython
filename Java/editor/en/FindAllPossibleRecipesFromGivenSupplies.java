  /**
You have information about n different recipes. You are given a string array 
recipes and a 2D string array ingredients. The iᵗʰ recipe has the name recipes[i], 
and you can create it if you have all the needed ingredients from ingredients[i]
. Ingredients to a recipe may need to be created from other recipes, i.e., 
ingredients[i] may contain a string that is in recipes. 

 You are also given a string array supplies containing all the ingredients that 
you initially have, and you have an infinite supply of all of them. 

 Return a list of all the recipes that you can create. You may return the 
answer in any order. 

 Note that two recipes may contain each other in their ingredients. 

 
 Example 1: 

 
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = [
"yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
 

 Example 2: 

 
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],[
"bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the 
ingredient "bread".
 

 Example 3: 

 
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"]
,["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour",
"meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the 
ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the 
ingredients "bread" and "sandwich".
 

 
 Constraints: 

 
 n == recipes.length == ingredients.length 
 1 <= n <= 100 
 1 <= ingredients[i].length, supplies.length <= 100 
 1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10 
 recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase 
English letters. 
 All the values of recipes and supplies combined are unique. 
 Each ingredients[i] does not contain any duplicate values. 
 

 Related Topics Array Hash Table String Graph Topological Sort 👍 1259 👎 74

*/
  
  package com.shuzijun.leetcode.editor.en;

  import java.util.*;

  public class FindAllPossibleRecipesFromGivenSupplies{
      public static void main(String[] args) {
          Solution solution = new FindAllPossibleRecipesFromGivenSupplies().new Solution();

          // Test 1
          // String[] recipes = new String[] {"bread"};
          // List<List<String>> ingredients = new ArrayList<>();
          // for (int i = 0; i < 1; i++)
          //     ingredients.add(new ArrayList<>());
          // ingredients.get(0).add("yeast");
          // ingredients.get(0).add("flour");
          // String[] supplies = new String[] {"yeast","flour","corn"};

          // Test 2
          String[] recipes = new String[] {"ju","fzjnm","x","e","zpmcz","h","q"};
          List<List<String>> ingredients = new ArrayList<>();
          ingredients.add(new ArrayList<>(Collections.singletonList("d")));
          ingredients.add(new ArrayList<>(Arrays.asList("hveml","f","cpivl")));
          ingredients.add(new ArrayList<>(Arrays.asList("cpivl","zpmcz","h","e","fzjnm","ju")));
          ingredients.add(new ArrayList<>(Arrays.asList("cpivl","hveml","zpmcz","ju","h")));
          ingredients.add(new ArrayList<>(Arrays.asList("h","fzjnm","e","q","x")));
          ingredients.add(new ArrayList<>(Arrays.asList("d","hveml","cpivl","q","zpmcz","ju","e","x")));
          ingredients.add(new ArrayList<>(Arrays.asList("f","hveml","cpivl")));
          String[] supplies = new String[] {"f","hveml","cpivl","d"};
          solution.findAllRecipes(recipes, ingredients, supplies);
      }
      //leetcode submit region begin(Prohibit modification and deletion)
class Solution {
    public List<String> findAllRecipes(String[] recipes, List<List<String>> ingredients, String[] supplies) {
        Map<String, Set<String>> ingredientToRecipes = new HashMap<>();
        Map<String, Integer> inDegrees = new HashMap<>();
        for (int i = 0; i < recipes.length; i++) {
            for (String singleIngredient : ingredients.get(i))
                ingredientToRecipes.computeIfAbsent(singleIngredient, x -> new HashSet<>()).add(recipes[i]);
            inDegrees.put(recipes[i], ingredients.get(i).size());
        }

        Queue<String> queue = new LinkedList<>(Arrays.asList(supplies));
        List<String> res = new ArrayList<>();
        while (!queue.isEmpty()) {
            String ingredient = queue.poll();
            if (ingredientToRecipes.containsKey(ingredient)) {
                for (String recipe : ingredientToRecipes.get(ingredient)) {
                    inDegrees.put(recipe, inDegrees.get(recipe) - 1);
                    if (inDegrees.get(recipe) == 0) {
                        res.add(recipe);
                        queue.offer(recipe);
                    }
                }
            }
        }
        return res;
    }
}
//leetcode submit region end(Prohibit modification and deletion)

  }