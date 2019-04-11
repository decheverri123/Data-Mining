import java.util.ArrayList;
import java.util.Collections;

public class Transactions extends ArrayList<Integer>
{
    int num;

    public Transactions(int num)
    {
        this.num = num;
    }

    @Override
    public boolean add(Integer number)
    {
        super.add(number);
        Collections.sort(this);
        return true;
    }
}
