import java.util.*;

import static java.util.Arrays.stream;
import static java.util.Collections.sort;

public class Helpers
{
    public static Transactions getTrans(int num, String record)
    {
        String line = record.trim();
        String[] vals = line.split(" ");
        Transactions trans = new Transactions(num);

        stream(vals).map(val -> Integer.parseInt(val.trim())).forEach(trans::add);

        return trans;
    }

    public static boolean hasMin(double supp, int numTrans, int items, ItemSet itemSet)
    {
        return Double.compare(itemSet.getSupp(), supp) >= 0;
    }

    static List<ItemSet> powerSet(ItemSet set)
    {
        List<ItemSet> subsets = new ArrayList<ItemSet>();

        int i = 0;
        while (i < Math.pow(2, set.size()))
        {
            List<Integer> list = new ArrayList<>(set.size());
            for (int j = 0; j < set.size(); j++)
                if ((i & (1 << j)) > 0)
                    list.add(set.get(j));
            if (list.size() > 0)
                subsets.add((ItemSet) list);
            i++;
        }

        return subsets;

    }

    public static List<ItemSet> getCandidateItemSets(List<ItemSet> prevPassItemSets, int setSize)
    {
        Map<Integer, ItemSet> itemSetMap = getItemSets(prevPassItemSets);
        sort(prevPassItemSets);
        int prevPassItemSetsSize = prevPassItemSets.size();

        int ind = 0;
        List<ItemSet> candidateItemSets = new ArrayList<>();
        while (ind < prevPassItemSetsSize)
        {
            int index2 = ind + 1;
            while (index2 < prevPassItemSetsSize)
            {
                boolean oof = false;
                for (int i = 0; i < (setSize - 1); i++)
                    if (!Objects.equals(prevPassItemSets.get(ind).get(i), prevPassItemSets.get(index2).get(i)))
                    {
                        oof = true;
                        break;
                    }

                if (!oof)
                {
                    ItemSet newItemSet = new ItemSet();
                    if (setSize > 1)
                        for (int i1 = 0; i1 < (setSize - 1); i1++)
                            newItemSet.add(prevPassItemSets.get(ind).get(i1));
                    newItemSet.add(prevPassItemSets.get(ind).get(setSize - 1));
                    newItemSet.add(prevPassItemSets.get(index2).get(setSize - 1));
                    if (!isInSet(itemSetMap, newItemSet))
                    {
                        index2++;
                        ind++;
                        continue;
                    }
                    candidateItemSets.add(newItemSet);
                }
                else
                    break;
                index2++;
            }
            ind++;
        }

        return candidateItemSets;

    }

    private static boolean isInSet(Map<Integer, ItemSet> itemSetMap, ItemSet newItemSet)
    {
        List<ItemSet> subsets = getSubSets(newItemSet);
        for (ItemSet subset : subsets)
        {
            int hash = subset.hashCode();
            if (!itemSetMap.containsKey(hash))
                return false;
        }
        return true;
    }

    private static List<ItemSet> getSubSets(ItemSet itemSet)
    {
        List<ItemSet> subSets = new ArrayList<>();

        ItemSet newItemSet = new ItemSet(itemSet.size() - 1);
        for (int item : itemSet)
        {
            newItemSet.clear();
            for (int item2 : itemSet)
                if (item != item2)
                    newItemSet.add(item2);
            ItemSet newItemSet2 = new ItemSet();
            newItemSet2.addAll(newItemSet);
            subSets.add(newItemSet2);
        }

        return subSets;
    }

    public static Map<Integer, ItemSet> getItemSets(List<ItemSet> itemSets)
    {
        Map<Integer, ItemSet> itemSetMap = new HashMap<>();

        for (ItemSet itemSet : itemSets)
        {
            int hashCode = itemSet.hashCode();
            if (!itemSetMap.containsKey(hashCode))
                itemSetMap.put(hashCode, itemSet);
        }
        return itemSetMap;
    }
}
