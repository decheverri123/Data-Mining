import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;

public class ItemSet extends ArrayList<Integer> implements Comparable<ItemSet>
{

    private int supp;

    public ItemSet(int supp)
    {
        this.supp = supp;
    }

    public ItemSet()
    {
    }

    public static Map<Integer, ItemSet> generateItemSetMap(List<ItemSet> itemSets)
    {
        HashMap<Integer, ItemSet> itemSetMap = new HashMap<>();

        for (ItemSet el : itemSets)
        {
            int hashCode = el.hashCode();
            if (!itemSetMap.containsKey(hashCode))
                itemSetMap.put(hashCode, el);
        }
        return itemSetMap;
    }

    public void add(int value)
    {
        if (super.contains(value))
            return;
        super.add(value);
    }

    public boolean add(Integer value)
    {
        if (super.contains(value))
            return false;
        super.add(value);
        return true;
    }

    public int getSupp()
    {
        return supp;
    }

    @Override
    public int compareTo(ItemSet set)
    {
        List<Integer> thisItems = this;
        if (thisItems.equals(set))
            return 0;

        return IntStream.range(0, thisItems.size()).map(
                i -> thisItems.get(i).compareTo(((List<Integer>) set).get(i))).filter(
                diff -> diff != 0).findFirst().orElse(0);
    }
}